from dataclasses import fields
from math import exp
from typing import Any, Optional, Type
from bson.objectid import ObjectId
# from .field_variable import FieldVariable
from pydantic import BaseModel, Field    

class MongoPieSchemaBase(BaseModel):
    id: Optional[ObjectId]
    
    class Config:
        arbitrary_types_allowed = True
        fields = {
            'id': '_id'
        }
    
if __name__ == '__main__':
    class Test(MongoPieSchemaBase):
        name: str
        age: int
    
    class Test2(MongoPieSchemaBase):
        test: Test
        address: str
        
    ins = Test2(test={'name':"test", 'age':10}, address="test")
    print(ins.test.name)
    
    
    
    
    
    