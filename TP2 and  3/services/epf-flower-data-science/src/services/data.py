import pandas as pd


def load_data():
    """
    Loads the Iris dataset from the saved CSV file.

    Returns:
    str: JSON representation of the loaded dataset.
    """
    file_path = "TP2 and  3\services\epf-flower-data-science\src\data\Iris.csv" 
    df = pd.read_csv(file_path)
    return df.to_json(orient="records")


