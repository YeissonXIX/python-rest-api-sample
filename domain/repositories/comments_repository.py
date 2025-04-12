from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from domain.entities.result import Result

class CommentsRepository(ABC):
    
    @abstractmethod
    async def get_all(self) -> Result:
        pass
    