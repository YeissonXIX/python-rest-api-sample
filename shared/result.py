from pydantic import BaseModel
from typing import TypeVar, Generic

T = TypeVar("T")


class Result(BaseModel, Generic[T]):
    success: bool = False
    data: T | None = None
    message: str | None = None


class NoContentResult(Result[T]):
    def __init__(self, message: str, data: T | None = None):
        super().__init__(
            success=False,
            message=message,
            data=data,
        )


class UnknownErrorResult(Result[T]):
    def __init__(self, message: str, data: T | None = None):
        super().__init__(
            success=False,
            message=message,
            data=data,
        )


class NotFoundErrorResult(Result[T]):
    def __init__(self, message: str, data: T | None = None):
        super().__init__(
            success=False,
            message=message,
            data=data,
        )


class NotAllowedErrorResult(Result[T]):
    def __init__(self, message: str, data: T | None = None):
        super().__init__(
            success=False,
            message=message,
            data=data,
        )


class SuccessResult(Result[T]):
    def __init__(self, message: str, data: T | None = None):
        super().__init__(
            success=True,
            message=message,
            data=data,
        )


class CreatedResult(Result[T]):
    def __init__(self, message: str, data: T | None = None):
        super().__init__(
            success=True,
            message=message,
            data=data,
        )


class InvalidDataResult(Result[T]):
    def __init__(self, message: str, data: T | None = None):
        super().__init__(
            success=False,
            message=message,
            data=data,
        )
