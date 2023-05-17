from typing import Any, Optional
from .db_connector import DBConnector
from pymongo import MongoClient, database

class _MongoPieClient:
    def __init__(self) -> None:
        self._db_connector = None
        
    def get_collection(self, collection: str) -> database.Collection:
        if not self.is_avaliable():
            raise Exception("MongoPieClient is not connected to database")
        return self._db_connector.get_collection(collection)
    
    def create_collection(self, name: str, collection_config: dict[str, Any]={}):
        #TODO: implement
        self._db_connector.db.create_collection(name=name, **collection_config)
        
    def connect(self, db: str, uri: Optional[str]=None, client: Optional[MongoClient]=None) -> None:
        if self._db_connector is not None:
            self._db_connector.bind(uri, client)
            self._db_connector.db = db
        else:
            self._db_connector = DBConnector(db, uri, client)
        
    def is_avaliable(self) -> bool:
        return self._db_connector is not None
    

MongoPieClient = _MongoPieClient()