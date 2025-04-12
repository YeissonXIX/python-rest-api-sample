from http import HTTPStatus
from typing import Optional, Any


class ApiResponse:
    def __init__(
        self,
        status_code: HTTPStatus,
        data: Optional[Any] = None,
        errors: Optional[str] = None,
        message: Optional[str] = None,
    ):
        self.status_code = status_code
        self.data = data
        self.errors = errors
        self.message = message

    def to_dict(self) -> dict[str, Any]:
        res = {
            "status_code": self.status_code,
            "data": self.data,
        }
        if self.errors:
            res["errors"] = self.errors
        if self.message:
            res["message"] = self.message
        return res
