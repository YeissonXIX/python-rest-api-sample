from fastapi import FastAPI, Response
from domain.application.comments_controller import CommentsController
from infraestructure.motor.motor_comments_repository import MongoCommentsRepository
from infraestructure.motor.motor_client import MotorClient
from shared.api_response import ApiResponse
from domain.entities.comment_entity import CommentEntity


def create_app():
    app = FastAPI()

    motor_client = MotorClient("sample_mflix")
    comments_repository = MongoCommentsRepository(motor_client)
    comments_controller = CommentsController(comments_repository)

    @app.get("/comments")
    async def get_all_comments(  # pyright: ignore[reportUnusedFunction]
        response: Response,
    ) -> ApiResponse[list[CommentEntity]]:
        result = await comments_controller.get_all()
        response.status_code = result.status_code
        return result

    return app
