import os
from java_to_json_schema import java_to_json_schema
from json_schema_to_python import post_process_json_schema, json_schema_to_python_classes

def convert_java_to_python(java_file_path, python_file_path):
    with open(java_file_path, 'r') as java_file:
        java_code = java_file.read()

    json_schema = java_to_json_schema(java_code)
    json_schema = post_process_json_schema(json_schema)
    python_code = json_schema_to_python_classes(json_schema)

    with open(python_file_path, 'w') as python_file:
        python_file.write(python_code)

if __name__ == "__main__":
    java_file_path = os.path.join('input', 'example.java')
    python_file_path = os.path.join('output', 'output.py')
    convert_java_to_python(java_file_path, python_file_path)
