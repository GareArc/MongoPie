from .db_connector import DBConnector
from pymongo import MongoClient, database

class _MongoPieClient:
    def __init__(self) -> None:
        self._db_connector = None
        
    def get_collection(self, collection: str) -> database.Collection:
        if not self.is_avaliable():
            raise Exception("MongoPieClient is not connected to database")
        return self._db_connector.get_collection(collection)
    
    def create_collection(self, name, config):
        #TODO: implement
        pass
        
    def connect(self, uri: str, db: str=None) -> None:
        if self._db_connector is not None:
            self._db_connector.set_uri(uri)
        else:
            self._db_connector = DBConnector(uri, db)
        
    def is_avaliable(self) -> bool:
        return self._db_connector is not None
    
    
    

MongoPieClient = _MongoPieClient()