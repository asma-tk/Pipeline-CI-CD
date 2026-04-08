from pathlib import Path

import joblib
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model_path = Path(__file__).resolve().parent.parent / "model" / "model.pkl"
model = joblib.load(model_path) if model_path.exists() else None
species_map = {
    0: "setosa",
    1: "versicolor",
    2: "virginica",
}


class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@app.get("/")
def healthcheck():
    return {"status": "ok", "model_loaded": model is not None}


@app.post("/predict")
def predict(data: IrisData):
    if model is None:
        raise HTTPException(status_code=503, detail=f"Model not found at {model_path}")


    input_data = [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
    prediction = model.predict(input_data)
    prediction_id = int(prediction[0])
    return {
        "prediction": prediction_id,
        "species_name": species_map.get(prediction_id, "unknown"),
    }

