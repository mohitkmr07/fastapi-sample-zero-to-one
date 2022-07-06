import uuid
from datetime import datetime
from typing import Optional, cast

import sqlalchemy.sql.schema
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_serializer import SerializerMixin

Base = declarative_base()
metadata = Base.metadata


class CustomSerializerMixin(SerializerMixin):
    serialize_types = (
        (UUID, lambda x: str(x)),
    )


class CommonBase:
    __tablename__ = 'common_base'
    # change your schema here
    # __table_args__ = ({'schema': 'core_schema'})

    id = cast(UUID(as_uuid=True),
              Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True))  # type: ignore
    created_by = cast(Optional[str], Column(String))
    created_at = cast(datetime, Column(DateTime(timezone=False), default=datetime.utcnow))
    updated_by = cast(Optional[str], Column(String))
    updated_at = cast(datetime, Column(DateTime(timezone=False), default=datetime.utcnow, onupdate=datetime.utcnow))
    context = cast(Optional[str], Column(String))


class Address(Base, CommonBase, SerializerMixin):
    __tablename__ = 'address'
    details = cast(int, Column(String(100), nullable=False))


class User(Base, CommonBase, SerializerMixin):
    __tablename__ = 'user'

    age = cast(int, Column(Integer))
    name = cast(int, Column(String(100), nullable=False))
    address_id = cast(UUID(as_uuid=True), Column(sqlalchemy.sql.schema.ForeignKey(Address.id), nullable=False))  # type: ignore

    address = relationship(Address)
