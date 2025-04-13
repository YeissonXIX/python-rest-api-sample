from pydantic import BaseModel, Field
from datetime import datetime


class CommentEntity(BaseModel):
    id: str = Field(alias="_id")
    name: str
    email: str
    movie_id: str
    text: str
    date: datetime
