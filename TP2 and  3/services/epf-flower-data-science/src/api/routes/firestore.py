from fastapi import APIRouter, HTTPException
from src.services.firestore import  retrieve_parameters,add_and_upadate_parameters
from pydantic import BaseModel
router = APIRouter()

@router.get("/get_parameters")
def get_parameters_route():
    return retrieve_parameters()


# Définir la structure de l'entrée avec Pydantic
class Parameter(BaseModel):
    name: str
    value: str  


@router.post("/add_and_update_parameters")
async def update_parameters_route(parameter: Parameter) :
    """
    Add a new parameter to Firestore if it doesn't already exist.
    """
    try:
        # Call the function to add the parameter
        add_and_upadate_parameters(parameter.name, parameter.value)
        return {"message": "Parameter added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))