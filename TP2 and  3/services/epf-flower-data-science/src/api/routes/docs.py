from fastapi.responses import RedirectResponse
from fastapi import Request
from fastapi import APIRouter

# Redirect the root endpoint to the Swagger documentation

router = APIRouter()

@router.get("/", include_in_schema=False)
def redirect_to_swagger(request: Request):
    return RedirectResponse(url="/docs")