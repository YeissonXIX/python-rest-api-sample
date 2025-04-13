from abc import ABC, abstractmethod
from domain.entities.result import Result
from domain.entities.comment_entity import CommentEntity


class CommentsRepository(ABC):

    @abstractmethod
    async def get_all(self) -> Result[list[CommentEntity]]:
        pass
