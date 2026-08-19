"""Pydantic schemas for the credit risk prediction API (German Credit Data)."""
from pydantic import BaseModel, Field
from typing import Literal


class PredictRequest(BaseModel):
    checking_status: Literal[
        "A11", "A12", "A13", "A14"
    ] = Field(..., description="Status of existing checking account")
    duration: int = Field(..., ge=1, le=72, description="Duration in months")
    credit_history: Literal[
        "A30", "A31", "A32", "A33", "A34"
    ] = Field(..., description="Credit history")
    purpose: Literal[
        "A40", "A41", "A42", "A43", "A44", "A45", "A46", "A47", "A48", "A49", "A410"
    ] = Field(..., description="Credit purpose")
    credit_amount: int = Field(..., ge=250, le=20000, description="Credit amount")
    savings_status: Literal[
        "A61", "A62", "A63", "A64", "A65"
    ] = Field(..., description="Savings account/bonds")
    employment: Literal[
        "A71", "A72", "A73", "A74", "A75"
    ] = Field(..., description="Present employment since")
    installment_rate: int = Field(..., ge=1, le=4, description="Installment rate as % of disposable income")
    personal_status: Literal[
        "A91", "A92", "A93", "A94", "A95"
    ] = Field(..., description="Personal status and sex")
    other_parties: Literal[
        "A101", "A102", "A103"
    ] = Field(..., description="Other debtors/guarantors")
    residence_since: int = Field(..., ge=1, le=4, description="Present residence since")
    property_magnitude: Literal[
        "A121", "A122", "A123", "A124"
    ] = Field(..., description="Property magnitude")
    age: int = Field(..., ge=18, le=100, description="Age in years")
    other_payment_plans: Literal[
        "A141", "A142", "A143"
    ] = Field(..., description="Other payment plans")
    housing: Literal[
        "A151", "A152", "A153"
    ] = Field(..., description="Housing situation")
    existing_credits: int = Field(..., ge=1, le=4, description="Number of existing credits at this bank")
    job: Literal[
        "A171", "A172", "A173", "A174"
    ] = Field(..., description="Job classification")
    num_dependents: int = Field(..., ge=1, le=2, description="Number of people liable for maintenance")
    own_telephone: Literal[
        "A191", "A192"
    ] = Field(..., description="Own telephone")
    foreign_worker: Literal[
        "A201", "A202"
    ] = Field(..., description="Foreign worker")

    class Config:
        json_schema_extra = {
            "example": {
                "checking_status": "A11",
                "duration": 6,
                "credit_history": "A34",
                "purpose": "A43",
                "credit_amount": 1169,
                "savings_status": "A65",
                "employment": "A75",
                "installment_rate": 4,
                "personal_status": "A93",
                "other_parties": "A101",
                "residence_since": 4,
                "property_magnitude": "A121",
                "age": 67,
                "other_payment_plans": "A143",
                "housing": "A152",
                "existing_credits": 2,
                "job": "A173",
                "num_dependents": 1,
                "own_telephone": "A192",
                "foreign_worker": "A201"
            }
        }


class PredictResponse(BaseModel):
    prediction: int = Field(..., description="0=Good (repaid), 1=Bad (default)")
    probability: float = Field(..., description="Probability of default")
    risk_tier: str = Field(..., description="Risk tier: low/medium/high/critical")


class HealthResponse(BaseModel):
    status: str = "ok"
    model_version: str | None = None
    model_loaded: bool = False


class PredictionRecord(BaseModel):
    id: int
    timestamp: str
    input: dict
    prediction: int
    probability: float
    risk_tier: str
    latency_ms: float


class StatsResponse(BaseModel):
    total_predictions: int
    default_rate: float
    risk_tier_distribution: dict
    avg_probability: float
    avg_latency_ms: float


class ModelInfoResponse(BaseModel):
    model_name: str
    n_estimators: int
    max_depth: int
    metrics: dict
    feature_importance: list[dict]