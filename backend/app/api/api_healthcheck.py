from fastapi import APIRouter, HTTPException, Request, status

from app.schemas.sche_base import ResponseSchemaBase

router = APIRouter()


@router.get("")
async def get(request: Request):
    user = request.state.user
    if(not user):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invaid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {"message": f"Hello, {user.name}!"}