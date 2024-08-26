import logging
from typing import Any

from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db

from app.schemas.sche_user import UserResponse
from app.models import User

logger = logging.getLogger()
router = APIRouter()

@router.get("", response_model=UserResponse)
def get() -> Any:
    try:
        users = db.session.query(User)
        return users
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))
