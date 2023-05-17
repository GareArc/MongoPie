from typing import Optional
import pymongo
from pymongo import MongoClient, database
from pymongo.server_api import ServerApi
import pymongo

class DBConnector:
    def __init__(self, db: str, uri: Optional[str]=None, client: Optional[MongoClient]=None) -> None:
        self._set_client(uri, client)    
        self._db = db
        
    def _set_client(self, uri: Optional[str]=None, client: Optional[MongoClient]=None) -> MongoClient:
        if uri is None and client is not None:
            self._client = client
        elif uri is not None and client is None:
            self._client = MongoClient(uri, server_api=ServerApi('1'))
        else:
            raise Exception("Either uri or client must be set")
        
    @property
    def db(self) -> database.Database:
        return self._client[self._db]
    
    @db.setter
    def db(self, db: str) -> None:
        self._db = db
    
    def get_collection(self, collection: str) -> database.Collection:
        if self._db is None:
            raise Exception("Database not set")
        elif collection not in self.db.list_collection_names():
            raise Exception("Collection not found")
        return self.db[collection]
    
    def bind(self, uri: Optional[str]=None, client: Optional[MongoClient]=None) -> None:
        if self._client is not None:
            self._client.close()
        self._set_client(uri, client)
    
    
        
    
        
    
        
    