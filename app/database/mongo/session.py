import motor.motor_asyncio

MONGO_DETAILS = "mongodb://test:test123@localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS,
                                                maxPoolSize=10,
                                                minPoolSize=10)

database = client.test_db
