from domain.repositories.comments_repository import CommentsRepository
from infraestructure.motor.motor_client import MotorClient
from domain.entities.result import Result
from shared.encoder import JSONEncoder

class MongoCommentsRepository(CommentsRepository):
    def __init__(self, motor_client: MotorClient):
        motor_client = motor_client.get_database()
        self.collection = motor_client["comments"] 
    
    async def get_all(self) -> Result:
        try:
            cursor = self.collection.find()
            comments = await cursor.to_list(length=10)
            return Result(success=True, data=comments)
        except Exception as e:
            return Result(success=False, error=str(e))
    

