# Diabetes Prediction Web App

## Description

This project is a web application for predicting diabetes using machine learning. The application uses a Random Forest Classifier to predict whether an individual has diabetes based on several input parameters such as glucose level, blood pressure, BMI, age, etc.

## Features

- User-friendly web interface for entering input parameters.
- Real-time diabetes prediction based on user input.
- Animated preloader displayed while processing the prediction.
- Audio feedback for the prediction result (Diabetes or No Diabetes).
- Error handling for missing input values.

## Prerequisites

- Python 3.x
- Flask
- Pandas
- Scikit-learn

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/diabetes-prediction-webapp.git
cd diabetes-prediction-webapp
```

2. Install the required packages:

```bash
pip install Flask pandas scikit-learn
```

3. Ensure the following directory structure:

```
/path/to/project/
    /static
        /audio
            diabetes.mp3
            no_diabetes.mp3
        /images
            preloader.gif
    /templates
        index.html
    dia.csv
    app.py
```

4. Place the dataset (`dia.csv`), audio files (`diabetes.mp3`, `no_diabetes.mp3`), and preloader GIF (`preloader.gif`) in the appropriate directories as shown above.

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Enter the required input parameters and click the "Predict" button to get the diabetes prediction result.

## Project Structure

- `app.py`: The main Flask application file.
- `dia.csv`: The dataset used for training the Random Forest model.
- `index.html`: The HTML template for the web interface.
- `static/audio`: Directory containing the audio files for prediction results.
- `static/images`: Directory containing the preloader GIF.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

You can copy this content into a `README.md` file and adjust any paths, descriptions, or additional details specific to your project. Make sure to replace the placeholder URL (`https://github.com/yourusername/diabetes-prediction-webapp.git`) with the actual URL of your GitHub repository.
