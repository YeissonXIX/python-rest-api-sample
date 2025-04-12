from http import HTTPStatus
from typing import Optional, Any


class ApiResponse:
    def __init__(self, code: HTTPStatus, data: Optional[Any] = None, errors: Optional[str] = None):
        self.code = code
        self.data = data
        self.errors = errors

    def to_dict(self) -> dict[str, Any]:
        res = {
            "code": self.code,
            "data": self.data 
        }
        if self.errors:
            res["errors"] = self.errors
        return res
