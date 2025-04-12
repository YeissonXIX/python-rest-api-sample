from bson.objectid import ObjectId
from datetime import datetime

def to_json(response: dict | list) -> dict | list:
    def serialize(obj: dict) -> dict:
        for key, value in obj.items():
            if isinstance(value, ObjectId):
                obj[key] = str(value)
            if isinstance(value, datetime):
                obj[key] = value.isoformat()
        return obj

    if isinstance(response, list):
        return [serialize(item) for item in response]
    return serialize(response)