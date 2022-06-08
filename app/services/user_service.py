from typing import Optional, List
from uuid import UUID

from sqlalchemy.orm import Session
from starlette.requests import Request

from app.db.models.model import User
from app.db.repository.user import user_repository
from app.db.session import SessionLocal
from app.schemas.user import UserRequest, UserResponse


def create_user(user_request: UserRequest, request: Request, db: Session):
    user = User()
    user.name = user_request.name
    user.age = user_request.age
    user.context = request.url.path
    user = user_repository.create(db=db, obj_in=user)
    return user


def get_user_by_id(id: UUID, db: SessionLocal):
    user = user_repository.get_by_id(db=db, id=id)
    return user


def get_users(db: SessionLocal) \
        -> List[UserResponse]:
    users: Optional[List[User]] = user_repository.get(
        db=db)

    return users
