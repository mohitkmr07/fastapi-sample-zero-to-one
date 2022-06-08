from fastapi import FastAPI

from app.api.endpoints.v1 import router
from app.db.models import model
from app.db.session import engine

model.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router.api_router, prefix='/v1')


@app.get("/")
async def root():
    return {"message": "Hello World"}
