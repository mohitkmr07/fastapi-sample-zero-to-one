from http import HTTPStatus
from http.client import INTERNAL_SERVER_ERROR

import uvicorn
from fastapi import FastAPI
from starlette.responses import JSONResponse

from app.api.endpoints.v1 import router
from app.cache.redis import initialize_redis
from app.core.exceptions import RequestError, RequestErrorHandler
from app.db.models import model
from app.db.session import engine

model.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router.api_router, prefix='/v1')


@app.exception_handler(RequestError)
async def request_error_internal(request, exc):
    reh = RequestErrorHandler(exc=exc)
    return reh.process_message()


@app.exception_handler(Exception)
async def custom_http_exception_handler(request, exc):
    return JSONResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
        content={"message": INTERNAL_SERVER_ERROR},
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def create_redis():
    await initialize_redis()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, proxy_headers=True, forwarded_allow_ips="*", debug=True,
                use_colors=True, env_file=".env")
