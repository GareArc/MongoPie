import datetime
from bson import ObjectId
from mongopie.schema import MongoPieSchemaBase, FieldVariable, MongoPieModel
from mongopie.client import MongoPieClient

import unittest


class BasicSchemaTest(unittest.TestCase):
    def test_schema_parse(self):
        class LOL(MongoPieSchemaBase):
            name: str
            age: int
            address: str
            
        lol_ins = LOL.parse_obj({'_id': ObjectId('551960df461a2ea940e51ddb'), 'name':"test", 'age':10, 'address':"test"})
        assert lol_ins.name == "test"
        assert lol_ins.age == 10
        assert lol_ins.address == "test"
        assert lol_ins.id == ObjectId('551960df461a2ea940e51ddb')
        
    def test_schema_parse_nested(self):
        class Inner(MongoPieSchemaBase):
            inner: str
            
        class LOL(MongoPieSchemaBase):
            name: str
            age: int
            address: str
            nest: Inner
            
        lol_ins = LOL.parse_obj({'_id': ObjectId('551960df461a2ea940e51ddb'), 'name':"test", 'age':10, 'address':"test", 'nest': {'inner': 'test'}})
        assert lol_ins.name == "test"
        assert lol_ins.age == 10
        assert lol_ins.address == "test"
        assert lol_ins.id == ObjectId('551960df461a2ea940e51ddb')
        assert lol_ins.nest.inner == 'test'