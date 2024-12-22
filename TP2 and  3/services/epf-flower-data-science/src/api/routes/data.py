from fastapi import APIRouter
from src.services.data import  load_data

router = APIRouter()

# New endpoint: Load the Iris dataset and return it as JSON
@router.get("/load-data")
def load_data_route():
    return load_data()

