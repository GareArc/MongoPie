from typing import Dict, List, Optional, Tuple, Type
from bson.objectid import ObjectId
from field_variable import FieldVariable

class MongoPieSchemaBase:
    # _id: Optional[ObjectId] = None
    
    def __init__(self) -> None:
        pass
    
    def get_fields(self) -> List[Tuple[str, Type[FieldVariable]]]:
        return [(name, schema) for name, schema in self.__class__.__dict__.items() if isinstance(schema, FieldVariable)]
    
    
if __name__ == '__main__':
    class temp(MongoPieSchemaBase):
        a = FieldVariable('a', str)
        def __init__(self) -> None:
            super().__init__()
        
    ins = temp()
    print(ins.get_fields())
    
    
    
    
    
    