from abc import ABC, abstractmethod
from shared.result import Result
from domain.entities.comment_entity import CommentEntity


class CommentsRepository(ABC):

    @abstractmethod
    async def get_all(self) -> Result[list[CommentEntity]]:
        pass
