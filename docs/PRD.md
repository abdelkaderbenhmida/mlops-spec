# Product Requirements Document — Credit Risk MLOps Platform

## Project Overview
- **Problem:** Banks lose $200B+/yr to loan defaults. Credit risk models must comply with Basel III, SR 11-7, and Fair Lending laws. Existing MLOps platforms use toy data — this platform solves the real problem.
- **Solution:** End-to-end MLOps platform for credit risk scoring: data ingestion → feature engineering → model training (XGBoost + LR baseline) → evaluation (AUC, KS, PSI, fairness) → deployment (FastAPI) → monitoring (drift, performance).
- **Success Metrics:**
  - AUC-ROC ≥ 0.80 on hold-out set
  - KS statistic ≥ 0.30 (discrimination power)
  - PSI < 0.10 (population stability)
  - Demographic parity difference < 0.10 (fairness)
  - API latency p99 < 100ms

## User Stories
1. As a **credit analyst**, I want to score a loan applicant so that I can approve/deny based on risk.
2. As a **risk manager**, I want to monitor model drift so that I can retrain before performance degrades.
3. As an **ML engineer**, I want to register and version models so that I can rollback if production issues arise.
4. As a **compliance officer**, I want fairness metrics so that the model doesn't discriminate against protected classes.
5. As a **DevOps engineer**, I want automated CI/CD so that model updates are tested before deployment.

## Core Features
- **P0 (Must have):**
  - Credit risk data generator (realistic distributions from Kaggle "Give Me Some Credit")
  - XGBoost classifier with LogisticRegression baseline
  - AUC, KS, precision/recall evaluation gates
  - Fairness audit (demographic parity on age, gender)
  - FastAPI prediction endpoint with probability + risk tier
  - MLflow experiment tracking + model registry
  - Unit tests for all ML components
- **P1 (Should have):**
  - Population Stability Index (PSI) for drift detection
  - SHAP explainability (global + local)
  - Prediction logging to PostgreSQL
  - Prometheus metrics endpoint
- **P2 (Nice to have):**
  - Champion/challenger A/B testing
  - ONNX export for edge deployment
  - Model card generation

## Constraints
- **Data:** Public datasets only (no PII). Kaggle "Give Me Some Credit" (150K rows).
- **Tech:** Python 3.12, scikit-learn, XGBoost, FastAPI, MLflow, PostgreSQL, Docker
- **Non-negotiables:** Must run locally with `docker compose up`. No cloud dependencies.

## Out of Scope
- Real-time streaming inference (batch scoring only for v1)
- Deep learning models (tree-based + linear only)
- External credit bureau integration
