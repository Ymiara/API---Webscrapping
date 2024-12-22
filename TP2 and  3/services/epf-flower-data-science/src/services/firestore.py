import firebase_admin
from firebase_admin import credentials, firestore
from fastapi import HTTPException

def retrieve_parameters () :

    """
    Retrieves the parameters document from Firestore.

    This function connects to Firestore using Firebase_admin, retrieves the document named 
    'parameters' from the 'parameters' collection, and returns the document's data as a dictionary.

    Returns:
        dict: A dictionary containing the parameters from the Firestore document. 
              If the document does not exist or an error occurs, an HTTPException will be raised.
    
    Raises:
        HTTPException: If an error occurs while interacting with Firestore or if the document cannot be found.
    """

    # Initialize Firebase Admin with the service account credentials
    cred = credentials.Certificate(r"C:\Users\yohan\OneDrive\Bureau\EPF\5ème année\Data Sources\API---Webscrapping\TP2 and  3\services\epf-flower-data-science\src\config\projet-api-c0e1d-firebase-adminsdk-r7loc-8e8e50c179.json")
    firebase_admin.initialize_app(cred)

    # Initialize Firestore client
    db = firestore.client()


    try:
        # Reference to the Firestore collection 'parameters'
        parameters_ref = db.collection('parameters').document('parameters')  # Collection name is 'parameters' and document name is 'parameters'
    
        # Get all documents in the 'parameters' collection
        parameters = parameters_ref.get()
        print(parameters)
        return parameters.to_dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
def add_and_upadate_parameters(name: str, value: str) :
    """
    Adds or updates a parameter in the Firestore 'parameters' document.

    This function connects to Firestore using Firebase_admin, checks if a parameter with the specified 
    'name' exists in the 'parameters' document. If it exists, it updates the value; if it does not exist, 
    it adds the new parameter with the provided name and value.

    Args:
        name (str): The name of the parameter to be added or updated.
        value (str): The value of the parameter to be added or updated.

    Returns:
        dict: A message indicating the success of the operation, either adding or updating the parameter.

    Raises:
        HTTPException: If an error occurs while interacting with Firestore or if the document cannot be found.
    """

    cred = credentials.Certificate(r"C:\Users\yohan\OneDrive\Bureau\EPF\5ème année\Data Sources\API---Webscrapping\TP2 and  3\services\epf-flower-data-science\src\config\projet-api-c0e1d-firebase-adminsdk-r7loc-8e8e50c179.json")
    firebase_admin.initialize_app(cred)
    # Initialize Firestore client
    db = firestore.client()

    try:
        # Reference to the Firestore collection 'parameters'
        parameters_ref = db.collection('parameters').document('parameters')  # Collection name is 'parameters' and document name is 'parameters'
        parameters = parameters_ref.get()

        parameters = parameters_ref.get()

        if parameters.exists:
            # Document exists, check if the field already exists
            current_data = parameters.to_dict()
            
            if name in current_data:
                # Field exists, update it
                parameters_ref.update({
                    name: value
                })
                return {"message": f"Parameter '{name}' updated successfully."}
            else:
                # Field does not exist, create it
                parameters_ref.update({
                    name: value
                })
                return {"message": f"Parameter '{name}' added successfully."}
        else:
            # Document doesn't exist, create the document with the new parameter
            parameters_ref.set({
                name: value
            })
            return {"message": f"Parameter '{name}' added successfully to the new document."}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    