from application.fast_api.controllers.fastapi_comments_controller import (
    FastapiCommentsController,
)
from fastapi import APIRouter

router = APIRouter()


def create_comments_router(comments_controller: FastapiCommentsController):

    @router.get("/")
    async def get_all_comments():  # pyright: ignore[reportUnusedFunction]
        return await comments_controller.get_all()

    return router
