# LocystBridge

LocystBridge is a Python library that provides functionalities for managing variables and their values. It allows users to create, edit, delete, and retrieve variables with ease, making it convenient to handle variable operations across multiple files.

## How to Use

- Clone the repository.
- Import the `create`, `edit`, `delete`, `value`, `returnList` functions into your Python environment.
- Follow the example code below to create new variables menus and interact with them.

## Usage

```python
from LocystBridge import create, edit, delete, value, returnList

# Create a variable
create("my_variable", 42)

# Get the value of the variable
print("Value of 'my_variable':", value("my_variable"))

# Edit the variable
edit("my_variable", 100)

# Get the updated value
print("Updated value of 'my_variable':", value("my_variable"))

# Create multiple variables
create("var1", "value1")
create("var2", "value2")
create("var3", "value3")

# Get a list of all variables
print("List of variables:", returnList())

# Delete the variable
delete("my_variable")

# Try to get the value after deletion
print("Value of 'my_variable' after deletion:", value("my_variable")) # Raises error
```

## Features

- **Create**: Create new variables with specified names and values.
- **Value**: Retrieve the value of a variable by its name.
- **Edit**: Modify the value of an existing variable.
- **Delete**: Remove a variable from the collection.
- **Return List**: Obtain a list of all variable names currently stored.

## Configuration

The `LocystBridge` module provides the following functionalities:

- `create(name, value=None)`: Creates a variable with a specified name and value.
- `value(name)`: Retrieves the value of a variable by its name.
- `edit(name, new_value)`: Modifies the value of an existing variable.
- `delete(name)`: Deletes a variable specified by its name.
- `returnList()`: Returns a list of all variable names currently stored.

## To-do

- Enhance error handling and edge case scenarios.
- Extend functionality to support additional variable operations if required.
- Improve documentation and examples for better understanding and usability.
