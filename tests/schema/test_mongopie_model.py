import datetime
from typing import Any
from bson import ObjectId
from mongopie.schema import MongoPieSchemaBase, MongoPieModel
from mongopie.client import MongoPieClient

import unittest

class BasicModelTest(unittest.TestCase):
    # def test_db_connected(self):
    #     assert MongoPieClient.is_avaliable()
        
    def test_model_find(self):
        class ImageAttr(MongoPieSchemaBase):
            height: int
            width: int
            
        class Image(MongoPieSchemaBase):
            name: str
            attributes: ImageAttr
            data: str
            interpretation: Any
            
        imageModel = MongoPieModel[Image]('images', Image)
        doc = imageModel.find_one()
        # print(doc)
        assert doc.name != None
        assert ObjectId.is_valid(doc.id)
        assert doc.attributes.height > 0
        assert doc.attributes.width > 0
        
        
        
        
        
        