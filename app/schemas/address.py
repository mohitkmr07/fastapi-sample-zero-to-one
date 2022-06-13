from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class AddressResponse(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    details: str

    class Config:
        orm_mode = True
