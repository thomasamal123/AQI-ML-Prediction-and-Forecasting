# Air Quality Index (AQI) Prediction & Forecasting  
**Machine Learning Project (with Flask Deployment Demo)**

This repository contains a **complete end‑to‑end machine learning project** focused on understanding, modelling, and predicting **Air Quality Index (AQI)** using real-world air pollution data.  
The core contribution of this work lies in **data analysis, feature engineering, model building, and short‑term forecasting**. A Flask application is included only to **demonstrate deployment** of the trained models.

---

## Project Overview

Air Quality Index (AQI) is a composite indicator influenced by multiple pollutants and temporal patterns.  
This project addresses AQI prediction through **two clearly separated but related ML problems**:

### **Part A — AQI Estimation (Same‑Hour Prediction)**
> *Given pollutant concentrations at a particular hour, estimate the AQI for that same hour.*

### **Part B — AQI Forecasting (Next‑Hour Prediction)**
> *Given recent AQI behaviour, forecast the AQI for the next hour.*

This separation allows the project to demonstrate both **static regression modelling** and **time‑dependent forecasting using supervised learning**.

---

## Why the Project Is Divided into Two Parts

| Aspect | Part A | Part B |
|-----|------|------|
| Problem Type | Regression | Time‑series forecasting (supervised) |
| Input | Pollutant values | Lag‑based AQI features |
| Output | Current AQI | Next‑hour AQI |
| Learning Focus | Pollutant‑AQI relationship | Temporal AQI behaviour |

This structure mirrors real‑world AQI systems where **estimation and forecasting are distinct tasks**.

---

## Dataset Description

- **Source:** Cleaned CPCB‑style air quality dataset  
- **Location:** Delhi monitoring stations  
- **Granularity:** Hourly observations  

### Key Feature Groups
- **Time Features:** Date, hour, day, month
- **Pollutants:** PM2.5, PM10, NO₂, SO₂, CO, O₃, NH₃
- **Meteorological Parameters:** Temperature, humidity, wind speed (where available)
- **Station Metadata:** Station ID and location info
- **Derived Columns:** AQI sub‑indices and categorical labels

The notebook includes **explicit column‑by‑column explanations** and justification for feature selection.

---

## Part A — AQI Estimation (Same‑Hour AQI)

### Problem Formulation
- **Type:** Supervised regression
- **Target:** AQI numeric value
- **Inputs:** Pollutant concentrations and selected environmental features

### Data Processing
- Missing value handling
- Removal of non‑predictive identifiers
- Feature correlation analysis
- Target isolation and feature selection

### Model Used
- **Random Forest Regressor**

**Why Random Forest?**
- Captures non‑linear pollutant interactions
- Robust to noise and outliers
- Strong performance on tabular environmental data
- Minimal distributional assumptions

### Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## Part B — AQI Forecasting (Next‑Hour Prediction)

### Forecasting Approach

Instead of classical time‑series models (ARIMA), forecasting is reframed as a **supervised ML problem** using **lag features**.

### Lag Feature Engineering
Examples:
- AQI at time *t*
- AQI at *t−1*, *t−2*
- Optional pollutant lag values

This allows the model to learn **short‑term AQI momentum and trends**.

### Model Characteristics
- Predicts AQI at *t + 1 hour*
- Trained with time‑aware data splitting
- Suitable for real‑time inference pipelines

### Forecasting Scope
- Short‑term only (next hour)
- Designed for interpretability and deployment readiness

---

## AQI Categorisation

Predicted AQI values are optionally mapped to **CPCB standard categories**:

| AQI Range | Category |
|------|------|
| 0–50 | Good |
| 51–100 | Satisfactory |
| 101–200 | Moderate |
| 201–300 | Poor |
| 301–400 | Very Poor |
| 401–500 | Severe |

---

## Model Artefacts

Saved for reproducibility and deployment:

- `AQI_RandomForest_Model.pkl` — Pollutant‑based AQI model  
- `aqi_next_hour_forecast_model.pkl` — Forecasting model  
- `aqi_pollutant_features.pkl` — Feature order (Part A)  
- `aqi_forecast_features.pkl` — Feature order (Part B)

> **Feature order consistency is critical** to avoid incorrect predictions.

## Model Files (Large File Handling)

Due to GitHub’s 25 MB file size limitation, the trained Random Forest AQI model could not be uploaded directly to this repository.

The model files are hosted externally on Google Drive and must be downloaded before running the project.

🔗 **Download model files here:**  
https://drive.google.com/drive/folders/1T6Y6beTGZDETiooL7PJ6ifO0bjMEbXTX?usp=drive_link

⚠️ Note:  
The notebook and Flask application will not run correctly unless the model files are downloaded and placed in the `MODELS/` directory as shown above.



---

## Key Learnings from This Project

- AQI estimation and AQI forecasting are **fundamentally different ML problems**
- Lag‑based supervised ML works well for short‑horizon forecasting
- Environmental data is noisy and non‑linear
- ML complements but does not replace official AQI calculation frameworks
- Deployment readiness requires strict feature consistency

---

## Limitations

- Forecasting limited to next‑hour horizon
- Station‑specific effects are simplified
- No live sensor ingestion
- Not a substitute for official CPCB AQI computation

---

## Flask Deployment (Secondary Component)

A **Flask web application** is provided separately to:
- Load trained models
- Accept user inputs
- Display predictions via a simple UI

> The Flask layer exists **only to demonstrate deployment**.  
> A separate README inside the Flask folder explains how to run it.

## Flask deployment details are documented here:
FlaskWebProject1/README.md


---

## Repository Contents

- `AIR_QUALITY_INDEX_ML_MINI_PROJECT.ipynb` — Complete ML workflow notebook  
- `*.pkl` — Trained models and feature artefacts  
- `FlaskWebProject1/` — Deployment demo (separate README)

---

## Author

**Amal Thomas**  
BSc (Hons) Artificial Intelligence  

Focus Areas:
- Machine Learning
- Environmental Data Analytics
- Time‑Series Forecasting
- Model Deployment

---

## License

This project is intended for **academic and portfolio demonstration purposes**.
