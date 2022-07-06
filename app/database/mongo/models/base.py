"""
    I preferred using DB postfix for db models.
    It will not be confused with response objects - if you will need anything other than a simple CRUD.
"""
from typing import Optional

from bson import ObjectId
from pydantic.main import BaseModel


class MongoModel(BaseModel):
    # class Config(BaseConfig):
    #     json_encoders = {
    #         datetime: lambda dt: dt.isoformat(),
    #         ObjectId: lambda oid: str(oid),
    #     }
    pass


class OID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if v == '':
            raise TypeError('ObjectId is empty')
        if ObjectId.is_valid(v) is False:
            raise TypeError('ObjectId invalid')
        return str(v)


class DocumentModel(dict):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

        @classmethod
        def alias_generator(cls, string: str) -> str:
            """ Camel case generator """
            temp = string.split('_')
            return temp[0] + ''.join(ele.title() for ele in temp[1:])


class Student(DocumentModel):
    __collection_name__ = 'students'
    id: Optional[OID]
    name: Optional[str]
    email: Optional[str]
    course: Optional[str]
    gpa: Optional[float]
