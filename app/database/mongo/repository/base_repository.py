from abc import abstractmethod
from typing import List, TypeVar, Generic, Type

from bson import ObjectId
from pymongo.results import InsertOneResult

from app.database.mongo.models.base import OID, DocumentModel
from app.database.mongo.session import database

DocumentModelType = TypeVar("DocumentModelType", bound=DocumentModel)


class BaseDocumentRepository(Generic[DocumentModelType]):
    __collection__ = None

    def __init__(self, model: Type[DocumentModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
        self.__collection__ = model.__collection_name__

    @property
    def collection(self):
        if self.__collection__ is None:
            raise ValueError('collection name is invalid')
        return self.__collection__

    @abstractmethod
    async def get_all_documents(self) -> List[DocumentModelType]:
        return await database[self.collection].find().to_list(None)

    @abstractmethod
    async def get_document_by_id(self, id: OID) -> DocumentModelType:
        return await database[self.collection].find_one({'_id': ObjectId(id)})

    @abstractmethod
    async def create_document(self, document: DocumentModelType) -> OID:
        result: InsertOneResult = await database[self.collection].insert_one(document.__dict__)
        return result.inserted_id

    @abstractmethod
    async def update_document(self, id: OID, obj_in: DocumentModelType):
        # update = self.document()
        # del update['_id'], update['updated_at']
        # await database[self.collection].update_one({'_id': id}, {'$set': update})
        # return await self.get({'_id': id})
        pass

    @abstractmethod
    async def delete_document(self, id: OID):
        return await database[self.collection].delete_one({'_id': ObjectId(id)})
