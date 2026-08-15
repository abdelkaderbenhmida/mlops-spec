"""Pydantic schemas for the churn prediction API."""
from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    tenure: int = Field(..., ge=0, le=100, description="Customer tenure in months")
    monthly_charges: float = Field(..., ge=0, le=500, description="Monthly charges")
    total_charges: float = Field(..., ge=0, le=10000, description="Total charges")
    contract: str = Field(..., description="Contract type")
    payment_method: str = Field(..., description="Payment method")

    class Config:
        json_schema_extra = {
            "example": {
                "tenure": 12,
                "monthly_charges": 65.5,
                "total_charges": 786.0,
                "contract": "Month-to-month",
                "payment_method": "Electronic check",
            }
        }


class PredictResponse(BaseModel):
    prediction: int = Field(..., description="Predicted class (0=No Churn, 1=Churn)")
    probability: float = Field(..., description="Probability of churn")


class HealthResponse(BaseModel):
    status: str = "ok"
    model_version: str | None = None


class PredictionRecord(BaseModel):
    id: int
    input_json: dict
    prediction: int
    probability: float
    created_at: str