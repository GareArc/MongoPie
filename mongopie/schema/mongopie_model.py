from typing import Type, Any

from pymongo.cursor import Cursor
from .mongopie_schema import MongoPieSchemaBase
from .field_variable import FieldVariable
from mongopie.client import MongoPieClient


class MongoPieModel:
    def __init__(self, name: str, schema: MongoPieSchemaBase) -> None:
        self._collection_name = name.lower()
        self._schema = schema
        
    def _schema_check(self, document: dict[str, Any]) -> bool:
        return self._schema._schema_check(document)
    
    def create_collection(self) -> None:
        if not MongoPieClient.is_avaliable():
            raise Exception("MongoPieClient is not connected to database")
        
        MongoPieClient.get_collection(self._collection_name)
        
    def find(self, query: dict=None) -> Cursor:       
        return MongoPieClient.get_collection(self._collection_name).find(query)
    
    def find_one(self, query: dict=None) -> dict:
        return MongoPieClient.get_collection(self._collection_name).find_one(query)
    
    def insert_one(self, document: dict[str, Any]) -> None:
        # schema check
        if not self._schema_check(document):
            raise Exception("Document does not match schema")
        if not MongoPieClient.is_avaliable():
            raise Exception("MongoPieClient is not connected to database")
        
        MongoPieClient.get_collection(self._collection_name).insert_one(document)
            
        
        
        
        
        
        