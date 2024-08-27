import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from starlette.middleware.cors import CORSMiddleware

from app.api.api_router import router
from app.models import Base
from app.db.base import engine
from app.core.config import settings
from app.helpers.exception_handler import CustomException, http_exception_handler
from app.middleware.verify_token_middleware import verify_token_middleware

Base.metadata.create_all(bind=engine)


def get_application() -> FastAPI:
    application = FastAPI()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URI)
    application.middleware("http")(verify_token_middleware)
    application.include_router(router, prefix=settings.API_PREFIX)
    application.add_exception_handler(CustomException, http_exception_handler)

    return application


app = get_application()
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
