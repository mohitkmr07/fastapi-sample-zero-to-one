from fastapi import APIRouter

from app.api.endpoints.v1 import api_user, api_student

api_router = APIRouter(tags=["APIS"])
api_router.include_router(api_user.api_router, prefix="/users")
api_router.include_router(api_student.api_router, prefix="/students")
