from ..LocystLogging import INFO, autolog, debug, error, info
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

    def getValue(self):
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
      
        old_value = self.value
        self.value = new_value
        info(f"Changed value of {self.name} from {old_value} to {new_value}")

    def delete(self):
        """
        Deletes the variable.
        """
      
        info(f"Deletion of {self.name}")
        variables.remove(self)

# ------------------------------------------------------------------------------------#

variables = []

@autolog
def value(name):
    """
    Returns the value of a variable.

    Paramaters:
     - name (str): The name of the variable.

    Returns:
     - Union[str, int, float, bool, None]: The value of the variable.
    """
  
    variable = _findVariable(name)
    return variable.getValue()

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
        error(f"[variable_edit_failure] Variable {name} not found")

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
        error(f"[variable_delete_failure] Variable {name} not found")

def returnList():
    """
    Returns every variable created.

    Returns:
     - List[strs]: A list of all variable names
    """
  
    return [var for var in variables]

def create(name, value=None):
    """
    Creates a variable with a specified name and value. Default value is None. 

    Parameters:
     - name (str): The name of the variable.
     - value (Union[str, int, float, bool, None]): The value of the variable.
    """
  
    if not isinstance(name, (str, int)):
        error(f"[variable_creation_failure] Tried to create {name}")
        return
    variable = _findVariable(name)

    if variable:
        error(f"[variable_creation_failure] Variable, {name} already exists")
        variable.edit(value)
    else:
        variables.append(Variable(name, value))
        debug(f"[variable_creation_success] '{name}' variable created")
        _memorySaver()

@autolog
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
        vars = variables[:delete_amount:]
        for variable in vars:
            variable.delete()
    elif not is_automated_call:
        vars = variables[delete_amount:]
        for variable in vars:
            variable.delete()

def _findVariable(name):
    """
    Locates a variable object.

    Parameters:
     - name (str): The name of the variable object that you're looking for

    Returns:
     - Variable: The variable object that you're looking for, else None if there isnt one
    """
  
    for variable in variables:
        if variable.name == name:
            return variable
    return None
