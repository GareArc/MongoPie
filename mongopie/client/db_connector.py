import pymongo
from pymongo import MongoClient, database
import pymongo

class DBConnector:
    def __init__(self, uri: str, db: str=None) -> None:
        self._client = MongoClient(uri)
        self._db = db
        
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
    
    def set_uri(self, uri: str) -> None:
        if self._client is not None:
            self._client.close()
        self._client = MongoClient(uri)
    
    
        
    
        
    
        
    