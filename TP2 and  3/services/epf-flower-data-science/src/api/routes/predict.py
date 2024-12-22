from fastapi import APIRouter
from src.services.predict import  predict
from src.services.process import process_data
router = APIRouter()
import numpy as np
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd


# Définir la structure de l'entrée avec Pydantic
class PredictionInput(BaseModel):
    data: list[float]  # Liste de dictionnaires représentant les données en entrée

@router.post("/predict")
async def predict_endpoint(input_data: PredictionInput):
    try:
        # Convertir les données reçues en DataFrame
        df = pd.DataFrame(input_data.data)
        print(df)
        features_array = np.array(df).reshape(1, -1)
        model_columns = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
        df_pred = pd.DataFrame(features_array, columns=model_columns)
        # Créer un DataFrame avec les colonnes attendues

        # Appeler la fonction de prédiction (en supposant qu'elle est déjà définie)
        predictions = predict(df_pred)
        return predictions
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))