from bson.objectid import ObjectId
from datetime import datetime
from .types import MongoDocuments, Document


def serialize_mongo_documents(documents: MongoDocuments) -> MongoDocuments:
    def serialize(obj: Document) -> Document:
        for key, value in obj.items():
            if isinstance(value, ObjectId):
                obj[key] = str(value)
            if isinstance(value, datetime):
                obj[key] = value.isoformat()
        return obj

    if isinstance(documents, list):
        return [serialize(item) for item in documents]
    return serialize(documents)
