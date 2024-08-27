import logging
from datetime import datetime
from os import access
from typing import Any

from fastapi.params import Header, Depends
from starlette.responses import JSONResponse

from app.core.security import create_access_token, decode_access_token
from app.services.check_token import verify_token
from app.services.srv_user import UserService
from fastapi import APIRouter, HTTPException, Body
from starlette import status
from app.db.base import get_session
from app.schemas.sche_user import UserResponse, UserCreate, UserBase, UserLogin
from app.models import User

logger = logging.getLogger()
router = APIRouter()


@router.get("/all", response_model=None)
def getAll() -> Any:
    try:
        users = get_session().query(User).all()
        return users
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )


@router.post("/login", response_model=Any)
def login(email: str, password: str) -> Any:
    try:
        login_user = UserService.login(email, password)
        return JSONResponse(
            content={
                "token": create_access_token(login_user.id),
                "name": login_user.name,
                "email": login_user.email,
                "created_at": login_user.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": login_user.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )


@router.post("", response_model=Any)
def create(user: UserCreate):
    try:
        return UserService.create(user)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )


@router.get("/profile", response_model=Any)
def get_user(payload: dict = Depends(verify_token)):
    try:
        user = UserService.get(payload["user_id"])
        return user
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )


@router.put("/user/{user_id}", response_model=Any)
def update_user(user_id: int, user: UserBase, payload: dict = Depends(verify_token)):
    try:
        payload_id = payload["user_id"]
        if int(payload_id) != user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=payload["user_id"]
            )
        return UserService.edit(user_id, user)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )
