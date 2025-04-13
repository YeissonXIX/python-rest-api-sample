from quart import Blueprint, Response
from domain.application.comments_controller import CommentsController


def create_comments_router(comments_controller: CommentsController):
    blueprint = Blueprint("comments", __name__, url_prefix="/comments")

    @blueprint.route("/")
    async def get_all_comments():  # pyright: ignore[reportUnusedFunction]
        result = await comments_controller.get_all()
        return Response(
            response=result.model_dump_json(),
            content_type="application/json",
            status=result.status_code,
        )

    return blueprint
