from typing import Any, Optional

class Result:
    def __init__(self, success: bool = False, data: Optional[Any] = None, error: Optional[str] = None):
        self.success = success
        self.data = data
        self.error = error