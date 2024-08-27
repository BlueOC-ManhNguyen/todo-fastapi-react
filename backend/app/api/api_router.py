from fastapi import APIRouter

from app.api import api_user, api_healthcheck, api_login

router = APIRouter()

router.include_router(api_healthcheck.router, tags=["health-check"], prefix="/healthcheck")
router.include_router(api_user.router, tags=["user"], prefix="/users")
router.include_router(api_login.router, tags=["login"], prefix="/login")
