from quart import Blueprint, Response, jsonify
from domain.application.comments_controller import CommentsController
from shared.encoder import JSONEncoder

def create_comments_router(comments_controller: CommentsController):
    blueprint = Blueprint("comments", __name__, url_prefix="/comments")

    @blueprint.route("/")
    async def get_all_comments():
        res = await comments_controller.get_all()
        return Response(
            response=JSONEncoder().encode(res.to_dict()),
            content_type="application/json",
            status=res.code
        )

    return blueprint
