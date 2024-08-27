from fastapi import Depends, Request, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.db.base import SessionLocal, get_db
from app.models.model_user import User  # Import your User model
from app.services.auth import verify_token, get_current_user  # Assuming these are defined in app.main

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Middleware to verify token before each request
async def verify_token_middleware(request: Request, call_next):
    # Skip verification for the token endpoint or any other paths that shouldn't require authentication
    if request.url.path in ["/login/token", "/docs", "/register"]:
        return await call_next(request)

    token = request.headers.get("Authorization")
    if not token:
        request.state.user = None
        return await call_next(request)

    # Remove the "Bearer " prefix
    token = token.split(" ")[1] if " " in token else token

    try:
        db: Session = SessionLocal()
        name = verify_token(token, HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        ))

        user = db.query(User).filter(User.name == name).first()
        if not user:
            return await call_next(request)

        # Attach the user to the request for later use in your route handlers
        request.state.user = user

    except JWTError:
        request.state.user = None
        return await call_next(request)

    return await call_next(request)