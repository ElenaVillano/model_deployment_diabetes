from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

app = FastAPI()

diabetes_ml_model = pickle.load(open('selected_model/rf_model.pkl', 'rb'))

class DiabetesInput(BaseModel):
    embarazos: int
    glucosa: float
    presion_arterial: float
    espesor_piel: float
    insulina: float
    imc: float
    diabetes_pedigree_function: float
    edad: int


@app.get('/')
def index():
    return {'mensaje':'mi appi de diabetes'}

@app.post('/diabetes_predictions')
def procesar_prediccion_diabetes(diabetes_pred_in: DiabetesInput, status_code=201):
    # Creando un numpy array bidimensional
    # Un numpy array es un contenedor eficiente en memoria que permite realizar operaciones numéricas rápidas
    features = [np.array(input_values)]
    print('features', features)

    # Creando un dataframe a partir del array bidimensional
    features_df = pd.DataFrame(features)
    print('features_df', features_df)

    # Generando las predicciones
    prediction_values = diabetes_ml_model.predict_proba(features_df)
    print('prediction_values', prediction_values)

    # Determinando la predicción final
    final_prediction = np.argmax(prediction_values)
    print('final_prediction', final_prediction)


