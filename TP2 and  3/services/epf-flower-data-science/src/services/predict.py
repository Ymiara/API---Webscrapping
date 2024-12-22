import joblib
from src.services.train_test_split import test_split
import pandas as pd



def predict(data):
    """
    Loads the trained RandomForest model and makes predictions on the provided DataFrame.

    Args:
    Data (DataFrame): DataFrame containing the features for prediction.

    Returns:
    str: JSON representation of the predicted labels.
    """
    model_save_path = 'TP2 and  3\services\epf-flower-data-science\src/models/trained_model.joblib'

    try:
        model = joblib.load(model_save_path)
    except FileNotFoundError:
        return {"error": "Trained model not found."}
    y_pred = pd.DataFrame(model.predict(data))
    

    return {"prediction": y_pred[0]}

