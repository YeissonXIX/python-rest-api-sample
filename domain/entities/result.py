from pydantic import BaseModel


class Result[T](BaseModel):
    success: bool = False
    data: T | None = None
    message: str | None = None
