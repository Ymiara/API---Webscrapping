"""API Router for Fast API."""
from fastapi import APIRouter

from src.api.routes import hello, docs, data, process, train_test_split, train_model, predict

router = APIRouter()

router.include_router(hello.router, tags=["Hello"])
router.include_router(docs.router, tags=["Docs"])
router.include_router(data.router, tags=["Data"])
router.include_router(process.router, tags=["Process"])
router.include_router(train_test_split.router, tags=["Train_Test_Split"])
router.include_router(train_model.router, tags=["Train_model"])
router.include_router(predict.router, tags=["Predict"])
