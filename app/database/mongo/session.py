import motor.motor_asyncio

from app.core.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(host=settings.MONGO_SERVER,
                                                username=settings.MONGO_USER,
                                                password=str(settings.MONGO_PASSWORD),
                                                port=settings.MONGO_PORT,
                                                maxPoolSize=50,
                                                minPoolSize=30)

database = getattr(client, settings.MONGO_DB)
