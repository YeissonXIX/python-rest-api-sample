from shared.api_response import ApiResponse
from http import HTTPStatus
from domain.repositories.comments_repository import CommentsRepository


class CommentsController:

    def __init__(self, comments_repository: CommentsRepository):
        self.comments_repository = comments_repository

    async def get_all(self) -> ApiResponse:
        result = await self.comments_repository.get_all()
        if not result.success:
            return ApiResponse(
                status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                errors=result.error,
                message="Failed to retrieve comments",
            )
        return ApiResponse(
            status_code=HTTPStatus.OK,
            data=result.data,
            message="Comments retrieved successfully",
        )
