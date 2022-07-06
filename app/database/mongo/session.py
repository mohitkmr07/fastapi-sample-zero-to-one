import motor.motor_asyncio

MONGO_DETAILS = "mongodb://test:test123@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS,
                                                maxPoolSize=10,
                                                minPoolSize=10)

database = client.test_db
#
# student_collection = database.get_collection("students_collection")


# helpers

#
# def student_helper(student) -> dict:
#     return {
#         "id": str(student["_id"]),
#         "email": student["email"],
#         "course_of_study": student["course_of_study"],
#         "year": student["year"],
#         "GPA": student["gpa"],
#     }
