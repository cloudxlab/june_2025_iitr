from __future__ import annotations

from typing import Any, Dict, List, Optional

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


MODEL_PATH = "california_housing_model.joblib"

app = FastAPI(title="California Housing Price Predictor", version="1.0.0")


# ---------- Request/Response Schemas ----------
class PredictRequest(BaseModel):
    # Each item is a feature dict: {"longitude": -122.23, "latitude": 37.88, ...}
    rows: List[Dict[str, Any]] = Field(..., min_items=1)


class PredictResponse(BaseModel):
    predictions: List[float]
    model_path: str


# ---------- Helpers ----------
def _get_expected_columns(model) -> Optional[List[str]]:
    """
    Try to infer the expected input columns from the pipeline.
    Works for many sklearn pipelines that were fit on a DataFrame.
    """
    # If pipeline was fit on DataFrame, many estimators/transformers keep feature_names_in_
    # Pipeline itself may have it, or preprocessor inside may have it
    if hasattr(model, "feature_names_in_"):
        return list(model.feature_names_in_)
    try:
        preprocess = model.named_steps.get("preprocess")
        if preprocess is not None and hasattr(preprocess, "feature_names_in_"):
            return list(preprocess.feature_names_in_)
    except Exception:
        pass
    return None


def _validate_columns(expected: Optional[List[str]], df: pd.DataFrame) -> None:
    if not expected:
        return  # Can't validate, proceed best-effort
    missing = [c for c in expected if c not in df.columns]
    if missing:
        raise HTTPException(
            status_code=422,
            detail={
                "message": "Missing required feature columns.",
                "missing_columns": missing,
                "expected_columns": expected,
            },
        )


# ---------- App lifecycle ----------
@app.on_event("startup")
def load_model() -> None:
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        raise RuntimeError(f"Failed to load model from {MODEL_PATH}: {e}")

    app.state.model = model
    app.state.expected_columns = _get_expected_columns(model)


# ---------- Endpoints ----------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": hasattr(app.state, "model"),
        "model_path": MODEL_PATH,
        "expected_columns": app.state.expected_columns,
    }


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    model = getattr(app.state, "model", None)
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    # Convert list[dict] -> DataFrame
    df = pd.DataFrame(req.rows)

    # Validate columns if we can infer them
    _validate_columns(app.state.expected_columns, df)

    try:
        preds = model.predict(df)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "Prediction failed. Check input schema/types/columns.",
                "error": str(e),
                "received_columns": list(df.columns),
            },
        )

    return PredictResponse(predictions=[float(p) for p in preds], model_path=MODEL_PATH)
