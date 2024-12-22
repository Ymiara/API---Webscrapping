import os
import pandas as pd
from src.services.train_test_split import test_split
from sklearn.preprocessing import LabelEncoder
import json 
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model ():
    """
    Trains a Randomforest model using the initialized parameters and saves the model.

    Returns:
    dict: {"message": "Model trained and saved successfully."}
    """
    try:

        X_train, _, y_train, _ = test_split()
        X_train = pd.read_json(X_train)
        y_train = pd.read_json(y_train)


        # Load the model parameters from the JSON file
        model_params_file = 'TP2 and  3\services\epf-flower-data-science\src\config\model_parameters.json'
        with open(model_params_file, 'r') as file:
            model_params = json.load(file)

        # Initialize the RandomFroest classifier with the model parameters
        model = RandomForestClassifier(**model_params)

        # Train the model
        model.fit(X_train, y_train)
        if not os.path.exists('TP2 and  3\services\epf-flower-data-science\src/models'):
            os.makedirs('TP2 and  3\services\epf-flower-data-science\src/models')

        # Save the trained model to the models folder
        model_filename = 'TP2 and  3\services\epf-flower-data-science\src/models/trained_model.joblib'
        joblib.dump(model, model_filename)

        return {"message": "Model trained and saved successfully"}

    except Exception as e:
        return {"error": str(e)}
    return ...