from http import HTTPStatus

from fastapi import APIRouter
from starlette.requests import Request

from app.schemas.student import StudentRequest, StudentResponse
from app.services import student_service

api_router = APIRouter()


@api_router.post("", response_model=StudentResponse, status_code=HTTPStatus.CREATED)
async def create_student(student_request: StudentRequest, request: Request) -> StudentResponse:
    return await student_service.add_student(student_request=student_request)


@api_router.get("/{id}", response_model=StudentResponse, status_code=HTTPStatus.OK)
async def get_student_by_id(id: str, request: Request) -> StudentResponse:
    return await student_service.get_user_by_id(id=id)


@api_router.delete("/{id}", status_code=HTTPStatus.OK)
async def delete_user_by_id(id: str, request: Request):
    await student_service.delete_student_by_id(id=id)
