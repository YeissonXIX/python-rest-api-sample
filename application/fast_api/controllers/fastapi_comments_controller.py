from shared.api_response import ApiResponse
from http import HTTPStatus
from domain.use_cases.get_all_comments_use_case import GetAllCommentsUseCase
from domain.entities.comment_entity import CommentEntity
from shared.result import NoContentResult
from typing import final


@final
class FastapiCommentsController:

    def __init__(self, get_all_comments_use_case: GetAllCommentsUseCase):
        self.get_all_comments_use_case = get_all_comments_use_case

    async def get_all(self) -> ApiResponse[list[CommentEntity]]:
        result = await self.get_all_comments_use_case()
        if isinstance(result, NoContentResult):
            return ApiResponse(
                status_code=HTTPStatus.NO_CONTENT,
                message=result.message,
            )

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
