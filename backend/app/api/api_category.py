from typing import Any

from fastapi import APIRouter, Depends, HTTPException
import logging

from starlette import status
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from app.db.base import get_session
from app.models import Category
from app.schemas.sche_category import CategoryBase, CategoryBaseResponse
from app.services.check_token import verify_token
from app.services.srv_category import CategoryService

logger = logging.getLogger()
router = APIRouter()


@router.get("", response_model=None)
def get(payload: dict = Depends(verify_token)) -> Any:
    try:
        user_id = payload["user_id"]
        categories = CategoryService.get(user_id)
        return JSONResponse(content={"categories": categories})
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )


@router.post("", response_model=None)
def create(category: CategoryBase, payload: dict = Depends(verify_token)) -> Any:
    try:
        user_id = payload["user_id"]
        return CategoryService.create(user_id, category)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )


@router.put("/{category_id}", response_model=None)
def update(
    category_id: int, category: CategoryBase, payload: dict = Depends(verify_token)
) -> Any:
    try:
        user_id = payload["user_id"]
        if int(user_id) != category.user_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error()
            )
        return CategoryService.update(category_id, category)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )


@router.delete("/{category_id}", response_model=None)
def delete(category_id: int) -> Any:
    try:
        return CategoryService.delete(category_id)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )


@router.get("/all", response_model=None)
def getAll() -> Any:
    try:
        categories = get_session().query(Category).all()
        return categories
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )
