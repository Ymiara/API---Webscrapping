from fastapi import APIRouter
from src.services.train_model import train_model

router = APIRouter()

@router.get("/train_model")
def train_route():
    return train_model()
