from fastapi import APIRouter
from src.services.train_test_split import  test_split
router = APIRouter()


@router.get("/train_test_split")
def test_split_route():
    return test_split()