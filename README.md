
# Predicting Bipolar Disorder Prevalence Using Machine Learning

This project aims to leverage machine learning algorithms to predict the prevalence of bipolar disorders based on various mental health indicators. The dataset used includes information on schizophrenia, depressive, anxiety, and eating disorders across multiple countries and years. By employing Random Forest Regressor, we aim to build a robust model that can provide accurate predictions and insights into the relationships between different mental health disorders.



## Installation

1. Clone the repository:

```bash
 git clone https://github.com/HarshalSaharia/BipolarPrediction
```
2. Create and activate a virtual environment:

```bash
  conda create -p venv python==3.7 -y
```
```bash
  conda activate venv /
```
3. Install the dependencies:

```bash
  pip install -r requirements.txt
```
    
## Usage
Use VSCode IDE 

Add all the cloned files into venv kernel.
```bash
  pip install notebook
```
Open jupyter notebook:
```bash
  jupyter notebook LinearRegression_and_RandomForestRegressor.ipynb
```


Run the LinearRegression_and_RandomForestRegressor.ipynb.
## Flask app
Run the Flask application:
```bash
  python app.py
```
After running app.py open your web browser and go to http://127.0.0.1:5000

## Deployment 
Google App Engine (GAE)
Google App Engine is a fully managed platform for building and deploying web applications. It allows developers to focus on writing code without worrying about the underlying infrastructure. GAE automatically manages scaling, load balancing, and application performance, enabling quick deployment and maintenance of applications in a serverless environment.

The application is deployed on Google App Engine. You can access it here.
https://bipolardetection.de.r.appspot.com/


## License

MIT License

