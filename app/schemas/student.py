from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, EmailStr, BaseConfig

from app.database.mongo.models.base import MongoModel, OID


class StudentResponse(MongoModel):
    id: OID = Field(alias="_id")
    name: str = Field(...)
    email: str = Field(...)
    course: str = Field(...)
    gpa: float = Field(..., le=4.0)

    class Config(BaseConfig):
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "course": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
            }
        }


class StudentRequest(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    course: Optional[str]
    gpa: Optional[float]

    class Config:
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "name": "Jane Doe",
                "email": "jdoe@example.com",
                "course": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
            }
        }
