import pandas as pd
from sklearn.model_selection import train_test_split
from src.services.process import process_data


def test_split():
    """
    Splits the preprocessed dataset into training and testing sets.

    Returns:
    tuple: JSON representation of the training and testing sets.
    """
    data  = pd.read_json(process_data())
    features = data.drop(columns=["Species","Id"])
    labels = data["Species"]

    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

    return X_train.to_json(orient="records"), X_test.to_json(orient="records"),y_train.to_json(orient="records"),y_test.to_json(orient="records")