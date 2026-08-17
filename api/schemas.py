"""Pydantic schemas for the credit risk prediction API."""
from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    age: int = Field(..., ge=18, le=100, description="Applicant age")
    income: float = Field(..., ge=0, description="Annual income")
    monthly_income: float = Field(..., ge=0, description="Monthly income")
    debt_ratio: float = Field(..., ge=0, description="Total debt / total income")
    revolving_utilization: float = Field(..., ge=0, le=100, description="Credit card utilization %")
    num_open_credit_lines: int = Field(..., ge=0, description="Number of open credit lines")
    num_dependents: int = Field(..., ge=0, le=20, description="Number of dependents")
    num_30_59_days_late: int = Field(..., ge=0, description="Times 30-59 days past due")
    num_60_89_days_late: int = Field(..., ge=0, description="Times 60-89 days past due")
    num_90_days_late: int = Field(..., ge=0, description="Times 90+ days past due")
    num_mortgages: int = Field(..., ge=0, description="Number of mortgage loans")
    number_real_estate_loans: int = Field(..., ge=0, description="Number of real estate loans")

    class Config:
        json_schema_extra = {
            "example": {
                "age": 35,
                "income": 65000.0,
                "monthly_income": 5416.67,
                "debt_ratio": 0.35,
                "revolving_utilization": 45.2,
                "num_open_credit_lines": 6,
                "num_dependents": 1,
                "num_30_59_days_late": 0,
                "num_60_89_days_late": 0,
                "num_90_days_late": 0,
                "num_mortgages": 1,
                "number_real_estate_loans": 1,
            }
        }


class PredictResponse(BaseModel):
    prediction: int = Field(..., description="0=Repaid, 1=Default")
    probability: float = Field(..., description="Probability of default")
    risk_tier: str = Field(..., description="Risk tier: low/medium/high/critical")


class HealthResponse(BaseModel):
    status: str = "ok"
    model_version: str | None = None


class PredictionRecord(BaseModel):
    id: int
    input_json: dict
    prediction: int
    probability: float
    risk_tier: str
    created_at: str
