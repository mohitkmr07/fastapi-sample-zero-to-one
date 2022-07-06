"""
    I preferred using DB postfix for db models.
    It will not be confused with response objects - if you will need anything other than a simple CRUD.
"""
from typing import Optional

from bson import ObjectId


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
    _id: Optional[OID]


class Student(DocumentModel):
    __collection__ = 'students'
    name: Optional[str]
    email: Optional[str]
    course: Optional[str]
    gpa: Optional[float]
