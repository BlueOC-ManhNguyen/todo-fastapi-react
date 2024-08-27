from setuptools.extern import names

from app.db.base import get_session
from app.models import Category
from app.schemas.sche_category import CategoryBaseResponse


class CategoryService:
    @staticmethod
    def get(user_id):
        db = get_session()
        try:
            categories = db.query(Category).filter(Category.user_id == user_id).all()
            if categories is None or len(categories) == 0:
                raise Exception("No Categories")
            return categories
        except Exception as e:
            raise Exception(e)
        finally:
            db.close()

    @staticmethod
    def create(user_id, category):
        db = get_session()
        try:
            db_category = Category(name=category.name, user_id=user_id)
            db.add(db_category)
            db.commit()
            return "Create successfully"
        except Exception as e:
            raise Exception(e)
        finally:
            db.close()

    @staticmethod
    def update(category_id, category):
        db = get_session()
        try:
            updated_category = db.query(Category).get(category_id)
            if updated_category is None:
                raise Exception("Category not exists")
            updated_category.name = category.name
            db.commit()
            return CategoryBaseResponse.model_validate(updated_category)
        except Exception as e:
            raise Exception(e)
        finally:
            db.close()

    @staticmethod
    def delete(category_id):
        db = get_session()
        try:
            delete_category = db.query(Category).get(category_id)
            if delete_category is None:
                raise Exception("User not exists")
            db.delete(delete_category)
            db.commit()
            return "Delete successfully"
        except Exception as e:
            raise Exception(e)
        finally:
            db.close()
