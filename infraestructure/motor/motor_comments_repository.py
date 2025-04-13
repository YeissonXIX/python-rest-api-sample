from typing import override, cast
from domain.repositories.comments_repository import CommentsRepository
from infraestructure.motor.motor_client import MotorClient
from domain.entities.result import Result
from domain.entities.comment_entity import CommentEntity
from motor.motor_asyncio import AsyncIOMotorCollection, AsyncIOMotorCursor
from shared.encoder import serialize_mongo_documents
from shared.types import Document, MongoDocuments


class MongoCommentsRepository(CommentsRepository):

    collection: AsyncIOMotorCollection[Document]

    def __init__(self, client: MotorClient) -> None:
        self.collection = client.get_database()["comments"]

    @override
    async def get_all(self) -> Result[list[CommentEntity]]:
        try:
            cursor: AsyncIOMotorCursor[Document] = self.collection.find({})
            doc_comments: list[Document] = await cursor.to_list(length=10)
            raw_comments: MongoDocuments = serialize_mongo_documents(doc_comments)

            return Result(
                success=True,
                data=[
                    CommentEntity(**comment)
                    for comment in cast(list[Document], raw_comments)
                ],
                message="Comments retrieved successfully",
            )
        except Exception as e:
            return Result(success=False, message=str(e))
