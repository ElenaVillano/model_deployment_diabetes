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

class PredictionOut(BaseModel):
    tiene_diatebes: bool

@app.get('/')
def index():
    return {'mensaje':'mi appi de diabetes'}


@app.post('/diabetes-predictions')
def procesar_prediccion_diabetes(diabetes_pred_in: DiabetesInput,
                                 status_code = 201,
                                 response_model = PredictionOut):
    input_values = [diabetes_pred_in.embarazos,
                    diabetes_pred_in.glucosa,
                    diabetes_pred_in.presion_arterial,
                    diabetes_pred_in.espesor_piel,
                    diabetes_pred_in.insulina,
                    diabetes_pred_in.imc,
                    diabetes_pred_in.diabetes_pedigree_function,
                    diabetes_pred_in.edad]

    # Creando un numpy array bidimensional
    # Un numpy array es un contenedor eficiente en memoria que permite realizar operaciones numéricas rápidas
    features = [np.array(input_values)]

    # Creando un dataframe a partir del array bidimensional
    features_df = pd.DataFrame(features)

    # Generando las predicciones
    prediction_values = diabetes_ml_model.predict_proba(features_df)

    # Determinando la predicción final
    final_prediction = np.argmax(prediction_values)

    out = PredictionOut(final_prediction)

    return out