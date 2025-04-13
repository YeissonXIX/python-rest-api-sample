from typing import Any


type Document = dict[str, Any]

type MongoDocuments = Document | list[Document]
