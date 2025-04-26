from domain.repositories.comments_repository import CommentsRepository
from domain.entities.comment_entity import CommentEntity
from shared.result import Result, NoContentResult


class GetAllCommentsUseCase:
    comments_repository: CommentsRepository

    def __init__(self, comments_repository: CommentsRepository):
        self.comments_repository = comments_repository

    async def __call__(self) -> Result[list[CommentEntity]]:
        result = await self.comments_repository.get_all()
        if not result.data:
            return NoContentResult(message="No comments found")
        return result
