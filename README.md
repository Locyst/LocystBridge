# LocystBridge

## Table of Contents
* [General Information](#general-information)
* [Features](#features)
* [Usage](#usage)
* [Project Status](#project-status)

  
## General Information
- LocystBridge is a library developed for the sharing of variables between libraries and modules
- LocystBridge provides an easy way to share a everchanging amount of variables

## Features
- LocystBridge allows for variable management with the creation, editing and deletion of variables.
- LocystBridge has a simple memory manager that makes sure that excessive amounts of memory are not being used by deletes variables when the maximum number of variables are exceeded.
- LocystBridge provides a basic way to log changes in variables

## Usage
LocystBridge could be used for the sharing of configuration data.

```
# Assume this is the main process running on a central server

import LocystBridge

# Define a function to update the shared configuration
def update_config(key, value):
    LocystBridge.bridge.createVariable(key, value)

# Assume these are worker processes running on different nodes

# Function to retrieve a configuration parameter
def get_config(key):
    return LocystBridge.bridge.returnVariableValue(key)

# Example usage
if __name__ == "__main__":
    # Update the shared configuration from the main process
    update_config("max_connections", 100)
    update_config("timeout", 30)

    # Worker process 1 reads and uses the configuration
    max_connections = get_config("max_connections")
    timeout = get_config("timeout")
    print("Worker 1 - Max Connections:", max_connections)
    print("Worker 1 - Timeout:", timeout)

    # Worker process 2 reads and uses the configuration
    max_connections = get_config("max_connections")
    timeout = get_config("timeout")
    print("Worker 2 - Max Connections:", max_connections)
    print("Worker 2 - Timeout:", timeout)
```

Output:
```
Worker 1 - Max Connections: 100
Worker 1 - Timeout: 30
Worker 2 - Max Connections: 100
Worker 2 - Timeout: 30
```

## Project Status
Project is: _in progress_

This library is actively being developed to add more features and improve already built features.
