from quart import Blueprint, Response, jsonify
from domain.application.comments_controller import CommentsController
from shared.encoder import JSONEncoder


def create_comments_router(comments_controller: CommentsController):
    blueprint = Blueprint("comments", __name__, url_prefix="/comments")

    @blueprint.route("/")
    async def get_all_comments():
        result = await comments_controller.get_all()
        return Response(
            response=result.to_dict(),
            content_type="application/json",
            status=result.status_code,
        )

    return blueprint
