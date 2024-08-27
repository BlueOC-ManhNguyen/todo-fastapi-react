from setuptools.extern import names

from app.db.base import get_session
from app.models import Category, Task
from app.schemas.sche_task import TaskResponse


class TaskService:
    @staticmethod
    def get(category_id):
        db = get_session()
        try:
            tasks = db.query(Task).filter(Task.category_id == category_id).all()
            if tasks is None or len(tasks) == 0:
                raise Exception("No Tasks")
            return tasks
        except Exception as e:
            raise Exception(e)
        finally:
            db.close()

    @staticmethod
    def create(category_id, task):
        db = get_session()
        try:
            tasks = db.query(Task).filter(Task.category_id == category_id).all()
            if tasks is None or len(tasks) == 0:
                raise Exception("No Tasks")
            task_DB = Task(
                title=task.title,
                description=task.description,
                due_date=task.due_date,
                category_id=category_id,
            )
            db.add(task_DB)
            db.commit()
            return "Create successfully"
        except Exception as e:
            raise Exception(e)
        finally:
            db.close()

    @staticmethod
    def update(task_id, task) -> TaskResponse:
        db = get_session()
        try:
            updated_tasks = db.query(Task).get(task_id).all()
            if updated_tasks is None:
                raise Exception("Task not exists")
            updated_tasks.title = task.title
            updated_tasks.description = task.description
            updated_tasks.category_id = task.category_id
            updated_tasks.due_date = task.due_date
            updated_tasks.status = task.status
            db.commit()
            return TaskResponse.model_validate(updated_tasks)
        except Exception as e:
            raise Exception(e)
        finally:
            db.close()

    @staticmethod
    def delete(task_id):
        db = get_session()
        try:
            task = db.query(Task).get(task_id)
            db.delete(task)
            db.commit()
            return task
        except Exception as e:
            raise Exception(e)
        finally:
            db.close()
