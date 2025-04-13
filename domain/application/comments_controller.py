from shared.api_response import ApiResponse
from http import HTTPStatus
from domain.repositories.comments_repository import CommentsRepository
from domain.entities.comment_entity import CommentEntity


class CommentsController:
    comments_repository: CommentsRepository

    def __init__(self, comments_repository: CommentsRepository):
        self.comments_repository = comments_repository

    async def get_all(self) -> ApiResponse[list[CommentEntity]]:
        result = await self.comments_repository.get_all()
        if not result.success:
            return ApiResponse(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                error=result.message,
                message="Failed to retrieve comments",
            )
        return ApiResponse(
            status_code=HTTPStatus.OK,
            data=result.data,
            message="Comments retrieved successfully",
        )
