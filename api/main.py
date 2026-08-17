"""FastAPI application for credit risk prediction API."""
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

from db import get_session, init_db, Prediction
from model import load_model, predict, risk_tier, get_model_version
from schemas import PredictRequest, PredictResponse, HealthResponse, PredictionRecord


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    load_model()
    yield


app = FastAPI(title="Credit Risk Prediction API", version="1.0.0", lifespan=lifespan)

Instrumentator().instrument(app).expose(app, endpoint="/metrics")


@app.get("/health", response_model=HealthResponse)
async def health():
    return HealthResponse(status="ok", model_version=get_model_version())


@app.post("/predict", response_model=PredictResponse)
async def predict_endpoint(request: PredictRequest):
    try:
        input_data = request.model_dump()
        prediction, probability = predict(input_data)
        tier = risk_tier(probability)

        session = get_session()
        record = Prediction(
            input_json=input_data,
            prediction=prediction,
            probability=str(probability),
        )
        session.add(record)
        session.commit()
        session.close()

        return PredictResponse(prediction=prediction, probability=probability, risk_tier=tier)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/predictions", response_model=list[PredictionRecord])
async def get_predictions(limit: int = 100):
    session = get_session()
    records = session.query(Prediction).order_by(Prediction.created_at.desc()).limit(limit).all()
    session.close()
    return [
        PredictionRecord(
            id=r.id,
            input_json=r.input_json,
            prediction=r.prediction,
            probability=float(r.probability),
            created_at=r.created_at.isoformat(),
        )
        for r in records
    ]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)