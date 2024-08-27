from app.core.security import get_password_hash, decode_access_token, verify_password
from app.db.base import get_session
from app.models import User
from app.schemas.sche_user import UserResponse, UserCreate


class UserService:
    @staticmethod
    def login(email, password):
        db = get_session()
        try:
            exist_user = db.query(User).filter(User.email == email).first()
            if exist_user is None:
                raise Exception("Not Found")
            if verify_password(password, exist_user.password):
                raise Exception("Wrong password")
            return UserResponse.model_validate(exist_user)
        except Exception as e:
            raise Exception(e)
        finally:
            db.close()

    @staticmethod
    def get(user_id) -> UserResponse:
        db = get_session()
        try:
            exist_user = db.query(User).get(user_id)
            if exist_user is None:
                raise Exception("User not exists")
            return UserResponse.model_validate(exist_user)
        except Exception as e:
            raise Exception(e)
        finally:
            db.close()

    @staticmethod
    def edit(id, user) -> UserResponse:
        db = get_session()
        try:
            updated_user = db.query(User).get(id)
            if updated_user is None:
                raise Exception("User not exists")
            updated_user.name = user.name
            db.commit()
            return UserResponse.model_validate(updated_user)
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def create(user: UserCreate):
        db = get_session()
        try:
            db_user = User(
                name=user.name,
                email=user.email,
                password=get_password_hash(user.password),
            )
            db.add(db_user)
            db.commit()
            return "Create successfully"
        except Exception as e:
            raise Exception(e)
        finally:
            db.close()

    @staticmethod
    def check_token(token):
        decode_token = decode_access_token(token)
