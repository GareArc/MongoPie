from mongopie.schema import MongoPieSchemaBase, FieldVariable, MongoPieModel
from mongopie.client import MongoPieClient

import unittest

class BasicModelTest(unittest.TestCase):
    def test_db_connected(self):
        assert MongoPieClient.is_avaliable()
        
    def test_model_creation(self):
        class MockupSchema(MongoPieSchemaBase):
            name = FieldVariable('name', str).setAsKey().setAsRequired()
            age = FieldVariable('age', int).setAsRequired()

        test_model = MongoPieModel('test', MockupSchema())

        assert test_model is not None
        assert test_model._collection_name == 'test'
        assert isinstance(test_model._schema, MongoPieSchemaBase)
        
        # simple test for document validation, complete test in test_mongopie_schema.py
        assert test_model._schema._schema_check(document={'name': 'test', 'age': 20})
        assert not test_model._schema._schema_check(document={'name': 'test'})
        
    def test_model_find(self):
        class ImageSchema(MongoPieSchemaBase):
            pass
        
        image_model = MongoPieModel('images', ImageSchema())
        assert len(list(image_model.find())) > 0
        
        
        