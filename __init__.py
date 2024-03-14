import configparser
import os

dataDir = os.path.dirname(__file__)
configFilePath = os.path.join(dataDir, 'config.ini')
config = configparser.ConfigParser()
config.read(configFilePath)

class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.old_value = None

    def get_value(self):
        """
        Returns the value of the variable.

        Returns:
         - Union[str, int, float, bool, None]: The value of the variable.
        """

        return self.value

    def edit(self, new_value):
        """
        Allows for editing of the value of a variable.

        Paramaters:
         - new_value: The new value to set the variable to.
        """
      
        self.old_value = self.value
        self.value = new_value

    def delete(self):
        """
        Deletes the variable.
        """
      
        del variables[self.name]

# ------------------------------------------------------------------------------------#

variables = {}

def value(name):
    """
    Returns the value of a variable.

    Paramaters:
     - name (str): The name of the variable.

    Returns:
     - Union[str, int, float, bool, None]: The value of the variable.
    """
  
    variable = _findVariable(name)
    return variable.get_value()

def edit(name, new_value):
    """
    Allows for editing of a variable's value.

    Paramaters:
     - name (str): The name of the variable.
     - new_value (Union[str, int, float, bool, None]): The new value to set the variable to.
    """
  
    variable = _findVariable(name)
    if variable:
        variable.edit(new_value)
    else:
        raise ValueError(f"Variable {name} not found")

def delete(name):
    """
    Deletes the variable specified.

    Paramaters:
     - name (str): The variable being deleted
    """
  
    variable = _findVariable(name)
    if variable:
        variable.delete()
    else:
        raise ValueError(f"Variable {name} not found")

def returnList():
    """
    Returns every variable created.

    Returns:
     - List[strs]: A list of all variable names
    """
  
    return list(variables.keys())

def create(name, value=None):
    """
    Creates a variable with a specified name and value. Default value is None. 

    Parameters:
     - name (str): The name of the variable.
     - value (Union[str, int, float, bool, None]): The value of the variable.
    """
  
    if not isinstance(name, (str, int)):
        raise ValueError(f"Tried to create variable {name}. Variables must be strings or intagers")
    if name in variables:
        raise ValueError(f"Variable, {name} already exists")
    
    variables[name] = Variable(name, value)
    _memorySaver()

def _memorySaver(is_automated_call=False, delete_amount=10):
    """
    Automatically deletes variables if the amount of variables goes above a certain amount.
    
    Parameters:
     - is_automated_call (bool): Whether the function was called by the create or not. If it
     was automatically called it will only delete 10 variables if there is more than 
     specificed amount else if it wasnt it will delete 10 variables.
     - delete_amount (int): The amount of variables to delete.
    """
  
    if is_automated_call and len(variables) > int(config.get('Config', 'maxVariables')):
        keys_to_delete = list(variables.keys())[:delete_amount]
        for key in keys_to_delete:
            del variables[key]
    elif not is_automated_call and len(variables) > delete_amount:
        keys_to_delete = list(variables.keys())[delete_amount:]
        for key in keys_to_delete:
            del variables[key]

def _findVariable(lookup_name):
    """
    Locates a variable object.

    Parameters:
     - name (str): The name of the variable object that you're looking for

    Returns:
     - Variable: The variable object that you're looking for, else None if there isnt one
    """
  
    if lookup_name in variables:
        return variables[lookup_name]
    return None
