from typing import Any

from fastapi import APIRouter, HTTPException, Depends
import logging

from starlette import status

from app.db.base import get_session
from app.models import Task
from app.schemas.sche_task import TaskBase, TaskResponse
from app.services.check_token import verify_token
from app.services.srv_task import TaskService

logger = logging.getLogger()
router = APIRouter()


@router.get("/{category_id}", response_model=None)
def get(category_id: int) -> Any:
    try:
        users = get_session().query(Task).all()
        return users
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )


@router.post("/{category_id}", response_model=None)
def create(category_id: int, task: TaskBase, payload: dict = Depends(verify_token)):
    db = get_session()
    try:
        return TaskService.create(category_id, task)
    except Exception as e:
        raise Exception(e)
    finally:
        db.close()


@router.put("/{task_id}", response_model=None)
def update(
    task_id: int, task: TaskBase, payload: dict = Depends(verify_token)
) -> TaskResponse:
    try:
        return TaskService.update(task_id, task)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )


@router.delete("/{task_id}", response_model=None)
def delete(task_id: int, payload: dict = Depends(verify_token)):
    try:
        return TaskService.delete(task_id)
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )


@router.get("", response_model=None)
def getAll() -> Any:
    try:
        tasks = get_session().query(Task).all()
        return tasks
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=logger.error(e)
        )
