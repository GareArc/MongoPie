

class FieldVariable:
    _is_key: bool = False
    _is_unique: bool = False
    _is_required: bool = False
    _default_value = None
    
    
    def __init__(self, name, type): 
        self._name = name
        self._type = type
        
    def setAsKey(self) -> 'FieldVariable':
        self._is_key = True
        self._is_unique = True
        self._is_required = True
        return self
        
    def setAsUnique(self) -> 'FieldVariable':
        self._is_unique = True
        self._is_required = True
        return self
        
    def setAsRequired(self) -> 'FieldVariable':
        self._is_required = True
        return self
        
    def setDefaultValue(self, value) -> 'FieldVariable':
        self._default_value = value
        return self
    
        
        
if __name__ == '__main__':
    test = FieldVariable('name', str).setAsKey().setAsRequired()
    # print(test.value)
    # test.value = 'lol2'
    # print(test.value)