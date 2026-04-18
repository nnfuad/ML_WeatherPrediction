# 🌦️ ML Weather Prediction System

A machine learning-based weather prediction system that forecasts rainfall using structured meteorological data. The project includes data preprocessing, model training, and a deployed API for inference.

---

## 📌 Overview

This project builds a classification model to predict whether it will rain tomorrow based on historical weather features such as temperature, humidity, and wind conditions.

It also provides a REST API for real-time predictions.

---

## ⚙️ Features

* Data preprocessing and handling of missing values
* Categorical encoding for weather-related features
* Machine learning model training
* Model serialization
* REST API deployment (FastAPI / Flask)
* JSON-based prediction interface

---

## 📂 Project Structure

```
ML_WeatherPrediction/
│
├── data/                     # Dataset (if included)
├── models/                   # Trained model files
├── notebooks/                # Jupyter notebooks
├── src/                      # Source code (training + preprocessing)
├── app/                      # API (if structured separately)
│
├── main.py / app.py          # API entry point
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🧠 Model Details

* Type: Classification
* Target: RainTomorrow
* Input Features (example):

  * Location
  * Temperature (MinTemp, MaxTemp)
  * Wind Direction
  * Humidity
  * RainToday

⚠️ Note: Categorical features are encoded numerically before training.

---

## 🚀 Installation

```bash
git clone https://github.com/nnfuad/ML_WeatherPrediction.git
cd ML_WeatherPrediction
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 1. Run Training (if applicable)

```bash
python src/train.py
```

*(Adjust filename based on your repo)*

---

### 2. Run API Server

```bash
uvicorn main:app --reload
```

or

```bash
python app.py
```

---

## 🔌 API Usage

### Endpoint

```
POST /predict
```

### Example Request

```json
{
  "Location": 2,
  "WindGustDir": 5,
  "WindDir9am": 3,
  "WindDir3pm": 4,
  "RainToday": 1,
  "MinTemp": 13.4,
  "MaxTemp": 22.5,
  "Humidity9am": 71,
  "Humidity3pm": 22
}
```

### Example Response

```json
{
  "prediction": "Yes"
}
```

---

## 📊 Dataset

* Based on structured weather observations
* Includes both numerical and categorical features

⚠️ If dataset is not included:
Provide a link or mention its source (e.g., Kaggle).

---

## 📈 Model Performance

*(You should replace this section with real results)*

* Accuracy: XX%
* Precision: XX
* Recall: XX
* F1-score: XX

---

## ⚠️ Limitations (Important)

* Encoding scheme is fixed — unseen categories may break predictions
* No feature scaling (if not implemented)
* Model performance depends heavily on preprocessing consistency
* Possible data imbalance not addressed

---

## 🧪 Reproducibility Checklist

To make this project reliable:

* Save preprocessing pipeline (encoder, scaler)
* Fix random seeds
* Document feature order strictly
* Avoid hardcoded paths

---

## 🔧 Future Improvements

* Add pipeline using `sklearn.pipeline`
* Use cross-validation
* Try ensemble models (Random Forest, XGBoost)
* Add model monitoring
* Dockerize deployment

---

## 📜 License

This project is licensed under the MIT License.

---

## 👤 Author

Fuad
Electrical & Computer Engineering
Machine Learning Enthusiast
[GitHub](https://github.com/nnfuad)