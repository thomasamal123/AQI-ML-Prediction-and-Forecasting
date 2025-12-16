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
