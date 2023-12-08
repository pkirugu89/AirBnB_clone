# AirBnB Clone Project
## Description
Welcome to the AirBnB Clone project! This project is the first step towards building a full web application. The goal is to create an AirBnB clone with a command-line interface for managing various objects within the application. The command interpreter allows users to perform actions such as creating new objects, retrieving objects, updating attributes, and more.
## Command Interpreter
### How to Start
To start the command interpreter, run the console.py script:
```
$ ./console.py
```
## How to use
The command interpreter supports various commands to interact with AirBnB objects. 
Here are some basic commands:
- **create**: Create a new instance of a specified class.
- **show**: Show the string representation of an instance.
- **all**: Show all instances or all instances of a specified class.
- **update**: Update the attributes of an instance.
- **destroy**: Destroy an instance.
- **quit**: Quit the command interpreter.

## Examples
Interactive mode:
```
$ ./console.py
(hbnb) create user
```
Non-interactive Mode:
```
$ echo "create user" | ./console.py
```
For more detailed information on available commands, use the help command within the interpreter.
