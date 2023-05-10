from mongopie.client import DBConnector
from pymongo import MongoClient, database

class _MongoPieClient:
    def __init__(self) -> None:
        self._db_connector = None
        
    def get_collection(self, collection: str) -> database.Collection:
        if not self.is_avaliable():
            raise Exception("MongoPieClient is not connected to database")
        return self._db_connector.get_collection(collection)
        
    def connect(self, uri: str, db: str=None) -> None:
        self._db_connector = DBConnector(uri, db)
        
    def is_avaliable(self) -> bool:
        return self._db_connector is not None
    
    
    

MongoPieClient = _MongoPieClient()