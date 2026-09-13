# TODO: high - Add request validation and error handling
# TODO: medium - Implement request/response logging
# TODO: low - Add health check endpoint improvement
"""FastAPI app for Credit Risk (P1) — self-contained, trains at startup on real German Credit Data."""

import sys
import os
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _ROOT)
sys.path.insert(0, os.path.join(_ROOT, "ml"))

import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, f1_score

from preprocess import load_data, encode_features, apply_encoders, get_feature_names
from schemas import PredictRequest

UI_DIR = Path(__file__).parent.parent / "ui"
MODEL = None
FEATURE_NAMES = None
PREDICTIONS = []
MODEL_METRICS = {}
MAX_LOG = 500


def risk_tier(prob: float) -> str:
    if prob < 0.1:
        return "low"
    if prob < 0.3:
        return "medium"
    if prob < 0.6:
        return "high"
    return "critical"


def train_model():
    global MODEL, FEATURE_NAMES, MODEL_METRICS
    df = load_data()
    print(f"P1: Loaded {len(df)} records, default rate={df['target'].mean()*100:.1f}%")

    X, y = encode_features(df)
    FEATURE_NAMES = get_feature_names()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    MODEL = XGBClassifier(n_estimators=300, max_depth=6, learning_rate=0.05, subsample=0.8, random_state=42, device="cuda", tree_method="hist")
    MODEL.fit(X_train, y_train)

    proba = MODEL.predict_proba(X_test)[:, 1]
    preds = MODEL.predict(X_test)
    auc = roc_auc_score(y_test, proba)
    f1 = f1_score(y_test, preds)

    MODEL_METRICS.update({
        "model_name": type(MODEL).__name__,
        "n_estimators": MODEL.n_estimators,
        "max_depth": MODEL.max_depth,
        "learning_rate": MODEL.learning_rate,
        "subsample": MODEL.subsample,
        "random_state": MODEL.random_state,
        "auc": round(float(auc), 4),
        "f1": round(float(f1), 4),
    })
    print(f"P1: AUC={auc:.4f}, F1={f1:.4f}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    train_model()
    yield


app = FastAPI(title="Credit Risk Prediction API", version="1.0.0", lifespan=lifespan)


@app.get("/health")
async def health():
    return {"status": "ok", "model_version": "1.0", "model_loaded": MODEL is not None}


@app.post("/predict", response_model=dict)
async def predict_endpoint(request: PredictRequest):
    t0 = time.perf_counter()
    input_data = request.model_dump()
    df = pd.DataFrame([input_data])
    X = apply_encoders(df)
    prob = float(MODEL.predict_proba(X)[0][1])
    pred = 1 if prob >= 0.5 else 0
    latency_ms = (time.perf_counter() - t0) * 1000
    tier = risk_tier(prob)

    PREDICTIONS.append({
        "id": len(PREDICTIONS) + 1,
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "input": input_data,
        "prediction": pred,
        "probability": round(prob, 4),
        "risk_tier": tier,
        "latency_ms": round(latency_ms, 2),
    })
    if len(PREDICTIONS) > MAX_LOG:
        del PREDICTIONS[: len(PREDICTIONS) - MAX_LOG]

    return {"prediction": pred, "probability": round(prob, 4), "risk_tier": tier}


@app.get("/history")
async def history(limit: int = 50):
    limit = max(1, min(limit, MAX_LOG))
    return {"total": len(PREDICTIONS), "limit": limit,
            "items": list(reversed(PREDICTIONS[-limit:]))}


@app.get("/stats")
async def stats():
    n = len(PREDICTIONS)
    tiers = {t: 0 for t in ("low", "medium", "high", "critical")}
    if n == 0:
        return {"total_predictions": 0, "default_rate": 0.0,
                "risk_tier_distribution": tiers, "avg_probability": 0.0,
                "avg_latency_ms": 0.0}
    defaults = sum(1 for p in PREDICTIONS if p["prediction"] == 1)
    for p in PREDICTIONS:
        tiers[p["risk_tier"]] += 1
    return {
        "total_predictions": n,
        "default_rate": round(defaults / n, 4),
        "risk_tier_distribution": tiers,
        "avg_probability": round(sum(p["probability"] for p in PREDICTIONS) / n, 4),
        "avg_latency_ms": round(sum(p["latency_ms"] for p in PREDICTIONS) / n, 2),
    }


@app.get("/model-info")
async def model_info():
    fi = sorted(
        ({"feature": f, "importance": round(float(i), 4)}
         for f, i in zip(FEATURE_NAMES, MODEL.feature_importances_)),
        key=lambda x: x["importance"], reverse=True,
    )
    return {
        "model_name": MODEL_METRICS.get("model_name"),
        "n_estimators": MODEL_METRICS.get("n_estimators"),
        "max_depth": MODEL_METRICS.get("max_depth"),
        "learning_rate": MODEL_METRICS.get("learning_rate"),
        "subsample": MODEL_METRICS.get("subsample"),
        "metrics": {"auc": MODEL_METRICS.get("auc"), "f1": MODEL_METRICS.get("f1")},
        "feature_importance": fi,
    }


@app.get("/")
async def serve_ui():
    return FileResponse(UI_DIR / "index.html")


if UI_DIR.exists():
    app.mount("/ui", StaticFiles(directory=str(UI_DIR)), name="ui")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)