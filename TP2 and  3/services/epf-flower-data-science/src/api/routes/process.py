from fastapi import APIRouter, HTTPException
from src.services.process import process_data

router = APIRouter()

@router.get("/process")
def process_data_route():
    return process_data()
