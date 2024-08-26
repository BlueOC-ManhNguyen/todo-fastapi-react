from fastapi_sqlalchemy import db

from app.models import User

class UserService():

    @staticmethod
    def get(user_id):
        exist_user = db.session.query(User).get(user_id)
        if exist_user is None:
            raise Exception('User not exists')
        return exist_user
