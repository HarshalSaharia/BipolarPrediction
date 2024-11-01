from flask import Flask, request, render_template
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

app = Flask(__name__)

# Load the model and scaler
with open('randomForest.pkl', 'rb') as model_file:
    rf_model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Retrieve input values from the form
        schizophrenia = float(request.form['schizophrenia'])
        depressive = float(request.form['depressive'])
        anxiety = float(request.form['anxiety'])
        eating = float(request.form['eating'])

        # Create a DataFrame for the input values
        input_data = pd.DataFrame([{
            'Schizophrenia disorders': schizophrenia,
            'Depressive disorders': depressive,
            'Anxiety disorders': anxiety,
            'Eating disorders': eating
            
        }])
       # Scale the input data
        input_scaled = scaler.transform(input_data)

        # Predict the value
        predicted_value = rf_model.predict(input_scaled)

        # Render the template with the predicted value
        return render_template('home.html', prediction=predicted_value[0])

     

    return render_template('home.html', prediction=None)


if __name__ == '__main__':
    app.run(debug=True)

