from datetime import datetime

from bson import ObjectId
from pydantic import BaseModel, Field
from pydantic.class_validators import Union


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Model(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def document(self) -> dict:
        return self.dict(by_alias=True)

    @classmethod
    def model(cls, document: Union[dict, list, None]):
        if not document:
            return document
        if type(document) is dict:
            return cls(**dict(document))
        if type(document) is list:
            return [cls(**dict(doc)) for doc in document]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str,
            datetime: lambda dt: dt.isoformat()
        }
