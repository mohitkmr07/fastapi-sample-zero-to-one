from operator import and_
from typing import Optional
from uuid import UUID

from app.db.models.model import User
from app.db.repository.base import BaseRepository
from app.db.session import SessionLocal


class UserRepository(BaseRepository[User, User, User]):

    # extra queries that can be over written
    def get_by_name(self, db: SessionLocal, tenant_app_id: UUID, external_id: str) -> Optional[User]:
        return db.query(self.model).filter(and_(self.model.tenant_app_id == tenant_app_id,
                                                self.model.external_id == external_id)).first()


user_repository = UserRepository(User)
