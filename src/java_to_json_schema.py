import javalang

def java_to_json_schema(java_code):
    tree = javalang.parse.parse(java_code)
    classes = [node for path, node in tree if isinstance(node, javalang.tree.ClassDeclaration)]

    json_schema = {}
    for class_decl in classes:
        class_name = class_decl.name
        json_schema[class_name] = {
            "type": "object",
            "properties": {},
            "required": []
        }

        for field in class_decl.fields:
            for decl in field.declarators:
                field_name = decl.name
                field_type = field.type.name
                json_schema[class_name]["properties"][field_name] = {"type": java_type_to_json_type(field_type)}
                if not decl.initializer:
                    json_schema[class_name]["required"].append(field_name)

    return json_schema

def java_type_to_json_type(java_type):
    mapping = {
        "String": "string",
        "int": "integer",
        "Integer": "integer",
        "float": "number",
        "double": "number",
        "boolean": "boolean",
    }
    return mapping.get(java_type, "string")
