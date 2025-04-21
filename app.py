from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os
from sklearn.ensemble import GradientBoostingRegressor
app = Flask(__name__)


model_path = 'solar_rf_model.pkl'
if not os.path.exists(model_path):
    data = pd.read_csv('Solar_DNI.csv')
    data.columns = [col.split(',')[0].replace('"', '') for col in data.columns]

    # Initialize and train the Gradient Boosting Regressor
    model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    model.fit(data[['LAT', 'LONG']], data['AnnDNI'])

    # Save the trained model
    joblib.dump(model, model_path)
else:
    # Load the saved model
    model = joblib.load(model_path)
@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        try:
            lat = float(request.form['latitude'])
            long = float(request.form['longitude'])
            if -90 <= lat <= 90 and -180 <= long <= 180:
                prediction = round(model.predict([[lat, long]])[0], 2)
        except:
            pass
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)