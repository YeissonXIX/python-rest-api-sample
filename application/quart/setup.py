from quart import Quart
from application.quart.router.quart_comments_router import create_comments_router
from application.quart.controllers.quart_comments_controller import (
    QuartCommentsController,
)
from infraestructure.motor.motor_comments_repository import MongoCommentsRepository
from infraestructure.motor.motor_client import MotorClient
from domain.use_cases.get_all_comments import GetAllCommentsUseCase


def create_app():
    app = Quart(__name__)

    _register_blueprints(app)

    return app


def _register_blueprints(app: Quart) -> None:
    motor_client = MotorClient("sample_mflix")
    comments_repository = MongoCommentsRepository(motor_client)
    get_all_comments_use_case: GetAllCommentsUseCase = GetAllCommentsUseCase(
        comments_repository
    )
    comments_controller: QuartCommentsController = QuartCommentsController(
        get_all_comments_use_case
    )
    blueprint = create_comments_router(comments_controller)
    app.register_blueprint(blueprint)
