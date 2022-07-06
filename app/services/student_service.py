from app.database.mongo.models.base import OID
from app.database.mongo.repository.students_mongo_repository import students_repository
from app.schemas.student import StudentRequest, StudentResponse


# Add a new student into to the database
async def add_student(student_request: StudentRequest) -> StudentResponse:
    id: OID = await students_repository.create_document(document=student_request)
    student = await students_repository.get_document_by_id(id=id)
    return student


# Retrieve a student with a matching ID
async def retrieve_student(id: str) -> StudentResponse:
    student = await students_repository.get_document_by_id(id=id)
    return student


# # Update a student with a matching ID
# async def update_student(id: str, data: dict):
#     # Return false if an empty request body is sent.
#     if len(data) < 1:
#         return False
#     student = await student_collection.find_one({"_id": ObjectId(id)})
#     if student:
#         updated_student = await student_collection.update_one(
#             {"_id": ObjectId(id)}, {"$set": data}
#         )
#         if updated_student:
#             return True
#         return False
#
#
# Delete a student from the database

async def delete_student_by_id(id: str):
    await students_repository.delete_document(id=id)


async def get_user_by_id(id: str) -> StudentResponse:
    student = await students_repository.get_document_by_id(id=id)
    return student
