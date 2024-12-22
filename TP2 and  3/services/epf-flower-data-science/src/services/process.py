from src.services.data import  load_data

def process_data():
    """
    Preprocesses the loaded dataset by replacing specific strings.

    Returns:
    str: JSON representation of the preprocessed dataset.
    """
    data = load_data()
    data = data.replace("Iris-", "")

    return data