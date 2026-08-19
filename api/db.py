"""Database configuration and models for the credit risk prediction API."""
import os
from datetime import datetime

from sqlalchemy import JSON, DateTime, Integer, String, create_engine, Column
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    input_json = Column(JSON, nullable=False)
    prediction = Column(Integer, nullable=False)
    probability = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


def get_database_url() -> str:
    """Construct database URL from environment variables."""
    sqlite_path = os.environ.get("SQLITE_DB", os.path.join(os.path.dirname(__file__), "..", "predictions.db"))
    if os.environ.get("DB_HOST"):
        host = os.environ["DB_HOST"]
        port = os.environ.get("DB_PORT", "5432")
        user = os.environ.get("DB_USER", "postgres")
        password = os.environ.get("DB_PASSWORD", "postgres")
        database = os.environ.get("DB_NAME", "mlops")
        return f"postgresql://{user}:{password}@{host}:{port}/{database}"
    return f"sqlite:///{sqlite_path}"


def get_engine():
    """Create and return SQLAlchemy engine."""
    return create_engine(get_database_url(), pool_pre_ping=True)


def get_session():
    """Create and return a database session."""
    engine = get_engine()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()


def init_db():
    """Initialize the database tables."""
    engine = get_engine()
    Base.metadata.create_all(bind=engine)