from fastapi import FastAPI

from app.db.models import model
from app.db.session import engine

model.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
