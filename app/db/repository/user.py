from typing import Optional, List
from uuid import UUID

from sqlalchemy.orm import Session

from app.cache.redis import CachedEntity, CachableEntity
from app.db.models.model import User
from app.db.repository.base import BaseRepository


class UserRepository(BaseRepository[User]):

    # extra queries that can be over written
    def get_by_name(self, db: Session, name: str) -> Optional[List[User]]:
        return db.query(self.model).filter(self.model.name == name).all()


user_repository = UserRepository(User)


class UserCachedRepository(UserRepository):
    @CachedEntity('id')
    async def get_by_id(self, db: Session, id: UUID) -> Optional[User]:
        return db.query(self.model).filter(self.model.id == id).first()

    @CachableEntity('id')
    async def create(self, db: Session, *, obj_in: Optional[User]) -> Optional[User]:
        obj_in = super().create(db=db, obj_in=obj_in)
        return obj_in


user_cached_repository = UserCachedRepository(User)
