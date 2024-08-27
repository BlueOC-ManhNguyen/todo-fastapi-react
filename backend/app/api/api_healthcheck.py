from fastapi import APIRouter, Request

from app.schemas.sche_base import ResponseSchemaBase

router = APIRouter()


@router.get("")
async def get(request: Request):
    user = request.state.user
    return {"message": f"Hello, {user.name}!"}