from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('path/dia.csv')

# Preprocessing and model training
x = df.iloc[:, df.columns != 'Outcome']
y = df.iloc[:, df.columns == 'Outcome']
model = RandomForestClassifier(random_state=42)
model.fit(x, y.values.ravel())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        user_inputs = [float(request.form.get(field)) for field in ['glucose', 'blood_pressure', 'Pregnancies', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
        prediction = model.predict([user_inputs])
        result = "Diabetes" if prediction == 1 else "No Diabetes"
        return render_template('index.html', prediction_result=result)
    except ValueError:
        error = "Please fill in all fields with valid numbers."
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
