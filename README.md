# Java to Python Code Converter

This project provides a tool to convert Java code into Python code by first converting Java classes into JSON schema and then generating equivalent Python class definitions from the JSON schema. The aim is to make the conversion process easy and understandable for users of all levels, especially beginners.

## Overview

The project consists of three main scripts:

1. **'main.py'**: The main script implementing the conversion process.
2. **'json_schema_to_python.py'**: Contains functions to process JSON schemas and generate Python class definitions.
3. **'java_to_json_schema.py'**: Contains functions to parse Java code and convert it into a JSON schema.

## File Descriptions

### 'main.py'

This script serves as the main entry point for the project. It performs the following steps:

1. **Reads Java code from a specified file**: The script opens a Java file and reads its content into a string variable. This allows the script to process and convert the Java code.
2. **Converts the Java code into a JSON schema using `java_to_json_schema`**: The Java code is parsed and converted into a JSON schema. A JSON schema is a format that defines the structure of JSON data, making it easier to map Java classes to Python classes.
3. **Processes the JSON schema using `post_process_json_schema`**: This step involves refining the JSON schema to ensure it accurately represents the Java code structure.
4. **Generates Python class definitions from the JSON schema using `json_schema_to_python_classes`**: The processed JSON schema is used to generate Python class definitions that mirror the structure and properties of the original Java classes.
5. **Writes the generated Python code to a specified output file**: The final step involves writing the generated Python code to a file, making it ready for use.

### 'json_schema_to_python.py'

This module provides functions to process JSON schemas and generate Python class definitions.

#### Functions

- **`post_process_json_schema(json_schema)`**: This function refines the JSON schema to ensure it is accurate and ready for conversion to Python classes. It might involve adding default values, handling special cases, or cleaning up the schema.
- **`json_schema_to_python_classes(json_schema)`**: This function takes the refined JSON schema and generates Python class definitions. It iterates over each class in the schema and creates corresponding Python code.
- **`generate_python_class(class_name, schema)`**: This function generates the actual Python code for a single class. It constructs the class definition, including the `__init__` method, which initializes the class properties based on the schema.

### 'java_to_json_schema.py'

This module contains functions to parse Java code and convert it into a JSON schema using the `javalang` library.

#### Functions

- **`java_to_json_schema(java_code)`**: This function parses the Java code and converts it into a JSON schema. It identifies the classes and fields in the Java code and maps them to a structured JSON schema format.
- **`java_type_to_json_type(java_type)`**: This function maps Java types to JSON types. For example, it converts Java types like `String` and `int` to JSON types like `string` and `integer`.

### 'output.py'

This file contains an example of a generated Python class from the JSON schema. It helps users understand what the final Python code will look like.

## Usage

To use this project, follow these steps:

1. **Place your Java file in the `input` directory**: This step involves placing the Java file you want to convert into the designated input directory. This makes it easier for the script to locate and read the file.
2. **Update the `java_file_path` and `python_file_path` variables in 'main.py' with your file names**: Open 'main.py' and specify the path to your Java file and the desired output path for the Python file. This ensures the script reads from and writes to the correct locations.
3. **Run the 'main.py' script to generate the Python code**: Execute the 'main.py' script using a Python interpreter. This triggers the conversion process and generates the Python code.

```sh
python main.py
```

## Requirements

- **Python 3.x**: Ensure you have Python version 3 or higher installed on your system. This project is designed to work with Python 3.x.
- **`javalang` library**: This library is used to parse Java code. You need to install it using the following command:

```sh
pip install javalang
```

## Installation

To set up the project, follow these steps:

1. **Clone the repository**: Use git to clone the repository to your local machine.

```sh
git clone https://github.com/your-username/java-to-python-converter.git
```

2. **Navigate to the project directory**: Change your working directory to the project folder.

```sh
cd java-to-python-converter
```

3. **Install the required library**: Use pip to install the `javalang` library.

```sh
pip install javalang
```


### Detailed Explanation of 'main.py'

In 'main.py', the script performs several important tasks:

1. **Imports necessary modules**: It imports functions from 'java_to_json_schema.py' and 'json_schema_to_python.py' to handle the conversion process.

2. **Defines the `convert_java_to_python` function**: This function orchestrates the entire conversion process. It takes the paths to the input Java file and output Python file as arguments.

3. **Reads the Java code**: The function opens the specified Java file and reads its content into a string variable. This allows the script to work with the entire Java code as a single string.

4. **Converts Java to JSON schema**: The Java code string is passed to the `java_to_json_schema` function, which parses the code and generates a JSON schema representing the structure of the Java classes.

5. **Processes the JSON schema**: The generated JSON schema is then processed by the `post_process_json_schema` function to ensure it accurately represents the Java code's structure.

6. **Generates Python classes**: The processed JSON schema is passed to the `json_schema_to_python_classes` function, which generates the corresponding Python class definitions.

7. **Writes the Python code to a file**: The generated Python code is written to the specified output file, completing the conversion process.

### Detailed Explanation of 'json_schema_to_python.py'

This module contains several key functions:

- **`post_process_json_schema(json_schema)`**: This function refines the JSON schema to handle any special cases or clean up the structure. It ensures the schema is ready for conversion to Python classes.

- **`json_schema_to_python_classes(json_schema)`**: This function iterates over each class in the JSON schema and generates Python class definitions. It constructs the class definitions based on the schema properties.

- **`generate_python_class(class_name, schema)`**: This function generates the Python code for a single class. It constructs the class definition, including an `__init__` method that initializes the class properties based on the schema. The generated code is then returned as a string.

### Detailed Explanation of 'java_to_json_schema.py'

This module is responsible for parsing Java code and converting it into a JSON schema:

- **`java_to_json_schema(java_code)`**: This function uses the `javalang` library to parse the Java code. It identifies the classes and fields in the code and constructs a JSON schema representing the structure of the Java classes.

- **`java_type_to_json_type(java_type)`**: This function maps Java types to JSON types. It uses a predefined mapping to convert Java types like `String` and `int` to JSON types like `string` and `integer`.

### Example Output ('output.py')

The 'output.py' file contains an example of the generated Python class definitions. This file helps users understand the format and structure of the generated Python code. The example shows a Python class with an `__init__` method that initializes the class properties based on the schema.
