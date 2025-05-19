Solar Energy Prediction Web App

This project is a Flask‑based web application that predicts solar energy potential (specifically Direct Normal Irradiance – DNI) for any geographic location the user supplies. It combines a Gradient Boosting Machine‑learning model with an easy‑to‑use web interface so renewable‑energy enthusiasts, engineers, and researchers can quickly estimate available solar resources.

✨ Features

Coordinate Input Form – Users enter latitude & longitude in the browser; no installation required.

Gradient Boosting Regressor – Trained on historical meteorological & satellite data to predict DNI.

RESTful Prediction Endpoint – The web form submits to /predict and returns JSON & on‑page results.

Container‑ready – Dockerfile and requirements.txt included for reproducible deployment.

Extensible – Clean, modular code (data‑prep → model → Flask views) makes swapping models or adding extra weather variables simple.

📊 Model Details

Algorithm: GradientBoostingRegressor (scikit‑learn)

Input features: latitude, longitude, day‑of‑year, elevation, clearness index

Target: Daily average DNI (W/m²)

Metrics: R² ≈ 0.91 on hold‑out set
