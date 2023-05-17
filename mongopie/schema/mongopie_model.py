from typing import Generic, Type, Any, TypeVar
from pymongo.results import InsertOneResult, InsertManyResult

from .mongopie_schema import MongoPieSchemaBase
from .type_dict import PY_BSON_DICT
from mongopie.client import MongoPieClient

SchemaType = TypeVar('SchemaType', bound=MongoPieSchemaBase)

class MongoPieModel(Generic[SchemaType]):
    def __init__(self, name: str, schema: SchemaType) -> None:
        self._collection_name = name.lower()
        self._schema = schema
    
    def _get_collection_validator(self, config: dict[str, Any]={}) -> dict[str, Any]:
        required_items = []
        unique_items = []
        obejct_properties = {}
        
        # add extra configs
        obejct_properties.update(config)
        
        # add property fields
        for field, var in self._schema.get_fields():
            if var._is_unique:
                unique_items.append(field)
            if var._is_required:
                required_items.append(field)
            try:
                bsonType: str = var.get_type() if isinstance(var.get_type(), str) else PY_BSON_DICT[var.get_type()]
            except Exception as e:
                raise Exception(f"Type {var.get_type()} is not supported by MongoPie.")
            
            prop = {
                'bsonType': bsonType,
            }
            # add all properties
            prop.update(var._properties)
            
            obejct_properties[field] = prop
            
        validator = {
            '$jsonSchema': {
                'bsonType': "object",
                'title': f"{self._collection_name} Validator",
                'required': required_items,
                'properties': obejct_properties
            }
        }
        
        validator['$jsonSchema'].update(config)
        
        return validator
    
    def create_collection(self, collection_configs: dict[str, Any]={}, validator_configs: dict[str, Any]={}) -> None:
        """Create a MongoDB collection for this model.

        Args:
            - collection_configs: Options for collection creation except for **validator**. 
                See [db.createCollection()](https://www.mongodb.com/docs/manual/reference/method/db.createCollection/)
            - validator_configs: Options for collection validator. 
                See how to [Specify JSON Schema Validation](https://www.mongodb.com/docs/manual/core/schema-validation/specify-json-schema/#std-label-schema-validation-json)
        """
        
        if not MongoPieClient.is_avaliable():
            raise Exception("MongoPieClient is not connected to database")
        
        config = {
            "clusteredIndex": {
                "key": {"_id": 1, "unique": True},
            },
            'validator': self._get_collection_validator(validator_configs)
        }
        config.update(collection_configs)
        
        MongoPieClient.create_collection(self._collection_name, config)
        
    def find(self, query: dict=None) -> list[SchemaType]:
        docs = list(MongoPieClient.get_collection(self._collection_name).find(query))
        # for each document, convert it to schema object
        return [self._schema.parse_obj(doc) for doc in docs]
        
    
    def find_one(self, query: dict=None) -> SchemaType:
        return self._schema.parse_obj(MongoPieClient.get_collection(self._collection_name).find_one(query))
    
    def insert_one(self, document: dict[str, Any]) -> InsertOneResult:
        if not MongoPieClient.is_avaliable():
            raise Exception("MongoPieClient is not connected to database")
        
        return MongoPieClient.get_collection(self._collection_name).insert_one(document)
    
    def insert_many(self, documents: list[dict[str, Any]]) -> InsertManyResult:
        if not MongoPieClient.is_avaliable():
            raise Exception("MongoPieClient is not connected to database")
        
        return MongoPieClient.get_collection(self._collection_name).insert_many(documents)
        
        
        
if __name__ == '__main__':
    class LOL(MongoPieSchemaBase):
        name: str
        age: int
        address: str
    
    lol = MongoPieModel[LOL]("LOL", LOL)
        
        
        
        