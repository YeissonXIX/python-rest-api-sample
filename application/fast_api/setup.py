from fastapi import FastAPI
from application.fast_api.controllers.fastapi_comments_controller import (
    FastapiCommentsController,
)
from application.fast_api.router.fastapi_router import create_comments_router
from infraestructure.motor.motor_comments_repository import MongoCommentsRepository
from infraestructure.motor.motor_client import MotorClient
from domain.use_cases.get_all_comments_use_case import GetAllCommentsUseCase


def create_app():
    app = FastAPI()

    motor_client = MotorClient("sample_mflix")
    comments_repository = MongoCommentsRepository(motor_client)
    get_all_comments_use_case = GetAllCommentsUseCase(comments_repository)
    comments_controller = FastapiCommentsController(get_all_comments_use_case)

    app.include_router(create_comments_router(comments_controller))

    return app
