from quart import Quart
from infraestructure.quart.comments_router import create_comments_router
from domain.application.comments_controller import CommentsController
from infraestructure.motor.motor_comments_repository import MongoCommentsRepository
from infraestructure.motor.motor_client import MotorClient

def create_app():
    app = Quart(__name__)

    _register_blueprints(app)

    return app

def _register_blueprints(app: Quart) -> None:
    motor_client = MotorClient("sample_mflix")
    comments_repository = MongoCommentsRepository(motor_client)
    comments_controller = CommentsController(comments_repository)
    blueprint = create_comments_router(comments_controller)
    app.register_blueprint(blueprint)
