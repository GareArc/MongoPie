from typing import Any, Type
from bson.objectid import ObjectId
from .field_variable import FieldVariable

class MongoPieSchemaBase:
    # _id: Optional[ObjectId] = None
    
    def __init__(self) -> None:
        pass
    
    def get_fields(self) -> list[tuple[str, Type[FieldVariable]]]:
        return [(name, schema) for name, schema in self.__class__.__dict__.items() if isinstance(schema, FieldVariable)]
    
    def _schema_check(self, document: dict[str, Any]) -> bool:
        fields = self.get_fields()
        
        # check if all fields are valid in document
        for field_name in document.keys():
            if field_name not in [name for name, schema in fields]:
                return False

        # check if all required fields are present
        # also check validation of inner schemas
        for field_name, var in fields:
            # For inner schemas, call _schema_check (recursively)
            if var.get_type() == Type[MongoPieSchemaBase]:
                if not document[field_name]._schema_check(document[field_name]):
                    return False
            
            # For normal fields
            # check if required field is present
            if var._is_key or var._is_required or var._is_unique:
                if field_name not in document.keys():
                    return False
            # check if field is of correct type
            if not isinstance(document[field_name], var.get_type()):
                return False
        return True
    
if __name__ == '__main__':
    class temp(MongoPieSchemaBase):
        a = FieldVariable('a', str)
        def __init__(self) -> None:
            super().__init__()
        
    ins = temp()
    print(ins.get_fields())
    
    
    
    
    
    