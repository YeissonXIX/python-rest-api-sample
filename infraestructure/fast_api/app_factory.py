from fastapi import FastAPI, Response, status
from domain.application.comments_controller import CommentsController
from infraestructure.motor.motor_comments_repository import MongoCommentsRepository
from infraestructure.motor.motor_client import MotorClient


def create_app():
    app = FastAPI()

    motor_client = MotorClient("sample_mflix")
    comments_repository = MongoCommentsRepository(motor_client)
    comments_controller = CommentsController(comments_repository)

    @app.get("/comments")
    async def get_all_comments(response: Response):
        result = await comments_controller.get_all()
        response.status_code = result.status_code
        return result.to_dict()

    return app
