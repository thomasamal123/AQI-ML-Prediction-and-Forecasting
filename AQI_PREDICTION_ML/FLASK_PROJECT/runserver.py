from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

# ---------- LOAD DATA ----------
df = pd.read_csv("Delhi_3Stations_With_AQI_CLEAN.csv")
df.columns = df.columns.str.strip()
df["Station"] = df["Station"].astype(str).str.strip()

# ---------- LOAD MODELS ----------
pollutant_model = joblib.load("AQI_RandomForest_Model.pkl")
pollutant_features = joblib.load("aqi_pollutant_features.pkl")

forecast_model = joblib.load("aqi_next_hour_forecast_model.pkl")
forecast_features = list(forecast_model.feature_names_in_)

# ---------- HELPERS ----------
def aqi_category_cpcb(aqi):
    if aqi <= 50: return "Good"
    if aqi <= 100: return "Satisfactory"
    if aqi <= 200: return "Moderate"
    if aqi <= 300: return "Poor"
    if aqi <= 400: return "Very Poor"
    return "Severe"

def get_row(station, dt):
    r = df[
        (df["Station"] == station) &
        (df["year"] == dt.year) &
        (df["month"] == dt.month) &
        (df["day"] == dt.day) &
        (df["hour"] == dt.hour)
    ]
    return None if r.empty else r.iloc[0]

# ---------- ROUTES ----------
@app.route("/")
def home():
    return render_template("home.html")

# ---------- PART A ----------
@app.route("/pollutant", methods=["GET", "POST"])
def pollutant():
    defaults = {f: 0 for f in pollutant_features}
    defaults.update({
        "PM2.5": 80, "PM10": 140, "NO2": 30,
        "SO2": 10, "CO": 0.8, "Ozone": 40,
        "NH3": 25, "AT": 28, "RH": 60, "WS": 2.5
    })

    if request.method == "POST":
        X = np.array([[float(request.form[f]) for f in pollutant_features]])
        pred = round(pollutant_model.predict(X)[0], 2)

        return render_template(
            "result.html",
            mode_title="Current AQI Prediction (Part A)",
            prediction=pred,
            category=aqi_category_cpcb(pred),
            payload=request.form
        )

    return render_template("pollutant.html",
                           features=pollutant_features,
                           defaults=defaults)

# ---------- PART B ----------
@app.route("/forecast", methods=["GET", "POST"])
def forecast():
    if request.method == "POST":
        try:
            station = request.form["station"].strip()
            dt = datetime(
                int(request.form["year"]),
                int(request.form["month"]),
                int(request.form["day"]),
                int(request.form["hour"])
            )

            base = get_row(station, dt)
            if base is None:
                return render_template("forecast.html",
                    page_error="No data for selected station & time.")

            lag1 = get_row(station, dt - timedelta(hours=1))
            lag24 = get_row(station, dt - timedelta(hours=24))

            if lag1 is None or lag24 is None:
                return render_template("forecast.html",
                    page_error="Lag data unavailable for this time.")

            X = np.array([[ 
                base["PM2.5"], base["PM10"], base["NO2"], base["SO2"],
                base["CO"], base["Ozone"], base["AT"], base["BP"],
                base["RH"], base["WS"], base["WD"],
                dt.year, dt.month, dt.day, dt.hour,
                lag1["AQI_Value"], lag24["AQI_Value"],
                lag1["PM2.5"], lag24["PM2.5"]
            ]])

            pred = round(forecast_model.predict(X)[0], 2)

            next_row = get_row(station, dt + timedelta(hours=1))
            actual = None
            error = None
            if next_row is not None:
                actual = next_row["AQI_Value"]
                error = round(abs(actual - pred), 2)

            return render_template(
                "result.html",
                mode_title="Next-hour AQI Forecast (Part B)",
                prediction=pred,
                category=aqi_category_cpcb(pred),
                station=station,
                base_time=dt.strftime("%Y-%m-%d %H:00"),
                forecast_time=(dt + timedelta(hours=1)).strftime("%Y-%m-%d %H:00"),
                actual=actual,
                forecast_error=error
            )

        except Exception as e:
            return render_template("forecast.html", page_error=str(e))

    return render_template("forecast.html")

if __name__ == "__main__":
    app.run(debug=True)
