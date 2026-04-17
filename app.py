from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model & scaler
model = joblib.load("weather_model.joblib")
scaler = joblib.load("scaler.joblib")

# Initialize FastAPI
app = FastAPI(title="Weather Prediction API")

# Input schema (example features – adjust if needed)
class WeatherInput(BaseModel):
    Location: int
    WindGustDir: int
    WindDir9am: int
    WindDir3pm: int
    RainToday: int
    MinTemp: float
    MaxTemp: float
    Humidity9am: float
    Humidity3pm: float
    Pressure9am: float
    Pressure3pm: float
    Temp9am: float
    Temp3pm: float

@app.get("/")
def home():
    return {"message": "Weather Prediction API is running"}

@app.post("/predict")
def predict_weather(data: WeatherInput):
    
    # Convert input to array
    input_data = np.array([[
        data.Location,
        data.WindGustDir,
        data.WindDir9am,
        data.WindDir3pm,
        data.RainToday,
        data.MinTemp,
        data.MaxTemp,
        data.Humidity9am,
        data.Humidity3pm,
        data.Pressure9am,
        data.Pressure3pm,
        data.Temp9am,
        data.Temp3pm
    ]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    result = "Rain Tomorrow" if prediction[0] == 1 else "No Rain Tomorrow"

    return {
        "prediction": result
    }