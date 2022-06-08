from http import HTTPStatus
from typing import Optional, List
from uuid import UUID

from fastapi import APIRouter, Depends
from pydantic import conint
from sqlalchemy.orm import Session
from starlette.requests import Request

from app.db.deps import get_db
from app.db.models.model import User
from app.schemas.user import UserResponse, UserRequest
from app.services import user_service

api_router = APIRouter()


@api_router.post("", response_model=UserResponse, status_code=HTTPStatus.CREATED)
async def create_user(user_request: UserRequest, request: Request, db: Session = Depends(get_db)) -> UserResponse:
    user: Optional[User] = user_service.create_user(user_request=user_request,
                                                    request=request, db=db)
    return user


@api_router.get("", response_model=List[UserResponse])
async def get_users(db: Session = Depends(get_db)) -> List[UserResponse]:
    return user_service.get_users(db=db)


@api_router.get("/{id}", response_model=UserResponse)
async def get_user_by_id(id: UUID,
                         db: Session = Depends(get_db)
                         ) -> UserResponse:
    return user_service.get_user_by_id(id=id, db=db)
