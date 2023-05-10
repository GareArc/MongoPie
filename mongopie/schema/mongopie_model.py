from typing import Type
from mongopie.schema import MongoPieSchemaBase, FieldVariable
from mongopie.client import MongoPieClient


class MongoPieModel:
    def __init__(self, name: str, schema: Type[MongoPieSchemaBase]) -> None:
        self._collection_name = name.capitalize()
        self._schema = schema
        
        
    def find(self, query: dict=None) -> list:        
        return MongoPieClient.get_collection(self._collection_name).find(query)
    
    def find_one(self, query: dict=None) -> dict:
        return MongoPieClient.get_collection(self._collection_name).find_one(query)
    
    def insert_one(self, document: MongoPieSchemaBase) -> None:
        # check if document is the same type as schema
        if not isinstance(document, self._schema):
            raise Exception('document is not the same type as schema')
        
        # find all fields in schema
        post = {}
        for field_name, obj in document.get_fields():
            post[field_name] = obj.value
        
        
        
        
        
        