# Air Quality Index (AQI) Prediction & Forecasting – Flask Web Application

This repository contains a **Flask-based Machine Learning web application** developed to predict and forecast **Air Quality Index (AQI)** values using pollutant data and time‑series lag features.  
The project is built as a **portfolio‑ready ML deployment**, integrating trained models (`.pkl`) with a clean web interface.

---

## Project Overview

The application is divided into **two core functionalities**:

### 1️⃣ Pollutant‑Based AQI Prediction (Current AQI)
Predicts the **current AQI value** using pollutant concentrations such as:
- PM2.5  
- PM10  
- NO₂  
- SO₂  
- CO  
- O₃  
- NH₃  

A trained **Random Forest regression model** is used to estimate AQI based on historical CPCB-style data.

---

### 2️⃣ Next‑Hour AQI Forecasting
Forecasts the **AQI for the next hour** using:
- Lag‑based AQI features
- Engineered time‑series inputs

This converts the forecasting problem into a **supervised learning task**, allowing the model to learn short‑term AQI trends.

---

## Folder Structure

```
FlaskWebProject1/
│
├── static/                       # CSS and static assets
│
├── templates/                    # HTML templates
│   ├── home.html                 # Home page
│   ├── pollutant.html            # Pollutant AQI prediction page
│   ├── forecast.html             # Next-hour AQI forecasting page
│   └── result.html               # Results display page
│
├── AQI_RandomForest_Model.pkl    # Pollutant-based AQI model
├── aqi_next_hour_forecast_model.pkl
├── aqi_pollutant_features.pkl    # Feature order for Part A
├── aqi_forecast_features.pkl     # Feature order for Part B
│
├── Delhi_Stations_With_AQI_CLEAN.csv   # Dataset (used for training)
│
├── runserver.py                  # Flask application entry point
├── requirements.txt              # Python dependencies
├── FlaskWebProject1.sln           # Visual Studio solution file
└── README.md
```

---

## How to Run the Project Locally

### ✅ Prerequisites
- Python **3.9+**
- pip
- Git (optional)

---

### Step 1: Clone the Repository
```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd FlaskWebProject1
```

---

### Step 2: Create a Virtual Environment (Recommended)

**Windows**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

---

### Step 4: Run the Flask App
```bash
python runserver.py
```

You should see output similar to:
```
Running on http://127.0.0.1:5000/
```

Open your browser and visit:
👉 **http://127.0.0.1:5000/**

---

## Application Pages

- **Home Page** – Project overview and navigation  
- **Pollutant AQI Prediction** – Enter pollutant values → get AQI  
- **Next‑Hour Forecast** – Predict AQI for the upcoming hour  
- **Results Page** – Displays AQI value and category  

---

## AQI Category Mapping (CPCB Standard)

| AQI Range | Category |
|----------|----------|
| 0 – 50   | Good |
| 51 – 100 | Satisfactory |
| 101 – 200 | Moderate |
| 201 – 300 | Poor |
| 301 – 400 | Very Poor |
| 401 – 500 | Severe |

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

## Evaluation & Learning Outcomes

- Regression metrics: MAE, RMSE, R²
- Time‑series forecasting using lag features
- Real‑world AQI modeling constraints
- Model persistence and deployment using Flask
- End‑to‑end ML pipeline: data → model → web app

---

## Limitations

- Forecasting limited to short‑term (next hour)
- Depends on historical data quality
- Station‑specific trends may vary
- Not a replacement for official CPCB AQI reporting

---

## Future Improvements

- Multi‑hour / daily AQI forecasting
- REST API endpoints (JSON-based)
- Interactive charts & visualisations
- Cloud deployment (Render / Railway)
- Docker containerisation

---

## Author

**Amal Thomas**  
BSc (Hons) Artificial Intelligence  
Portfolio Project – Machine Learning & Flask Deployment

---

## License

This project is intended for **educational and portfolio purposes**.  
