from datetime import date

PY_BSON_DICT: dict[type, str] = {
    int: "int",
    str: "string",
    float: "double",
    bool: "bool",
    list: "array",
    dict: "object",
    date: "date",
    type(None): "null",
}