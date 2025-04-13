from http import HTTPStatus
from pydantic import BaseModel


class ApiResponse[T](BaseModel):
    status_code: HTTPStatus = HTTPStatus.OK
    data: T | None = None
    error: str | None = None
    message: str | None = None
