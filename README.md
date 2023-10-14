# AirBnB Clone - The Console

This is a group project focused on building a command-line console for managing AirBnB objects. The project is developed in Python, utilizing object-oriented programming (OOP) principles. The project is to be completed by a team consisting of Guillaume, Graham Olusiekwin, and Caleb Nkunze. The project's timeline spans from October 9, 2023, 6:00 AM, to October 16, 2023, 6:00 AM, with the checker being released on October 14, 2023, 12:00 PM. Manual quality assurance (QA) review is mandatory upon project completion, and an auto review will be launched at the deadline.

## Concepts

For this project, you are expected to explore the following concepts:

- Python packages
- AirBnB clone

## Background Context

Welcome to the AirBnB clone project! Before you begin, please read the AirBnB concept page.

The first step in this project involves creating a command interpreter to manage AirBnB objects. This step is crucial as it sets the foundation for building a full web application: the AirBnB clone. The work you do in this initial step will be used in all subsequent projects, including HTML/CSS templating, database storage, API development, and front-end integration.

Tasks include:

- Implementing a parent class (BaseModel) for initialization, serialization, and deserialization of future instances.
- Establishing a flow for serialization/deserialization: Instance -> Dictionary -> JSON string -> file.
- Creating classes for AirBnB objects (User, State, City, Place, etc.) that inherit from BaseModel.
- Building the first abstracted storage engine for the project: File storage.
- Creating unit tests to validate all classes and the storage engine.

## What's a Command Interpreter?

The command interpreter in this project is similar to a shell, but with a specific use-case. It's designed for managing objects related to the AirBnB project. You'll be able to perform actions such as creating new objects (e.g., User or Place), retrieving objects from various sources, performing operations on objects, updating object attributes, and destroying objects.

## Resources

You are encouraged to read or watch the following resources to aid in this project:

- cmd module
- cmd module in depth
- Python packages concept page
- uuid module
- datetime
- unittest module
- args/kwargs
- Python test cheatsheet
- cmd module wiki page
- python unittest

## Learning Objectives

By the end of this project, you should be able to explain the following without assistance:

**General:**
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What Unit testing is and how to implement it in a large project
- How to serialize and deserialize a Class
- How to read and write a JSON file
- How to manage datetime
- What an UUID is
- What *args is and how to use it
- What **kwargs is and how to use it
- How to handle named arguments in a function

**Copyright - Plagiarism:**
You must come up with your own solutions to meet the learning objectives. Copying and pasting someone else's work is not allowed, and plagiarism is strictly forbidden.

## Requirements

**Python Scripts:**
- Allowed editors: vi, vim, emacs
- All your files should be interpreted/compiled on Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Your code should use pycodestyle (version 2.8.*)
- All your files must be executable
- All modules, classes, and functions should have proper documentation explaining their purpose (not just a word but a sentence or more)
- Your code should pass all relevant unit tests

**Python Unit Tests:**
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All test files should be inside a folder named `tests`
- You have to use the unittest module for your test cases
- All test files should have a `.py` extension
- All test files and folders should start with `test_`
- Your file organization in the tests folder should match your project's structure
- It is encouraged to collaborate on test cases to ensure coverage of all edge cases

**GitHub:**
- There should be one project repository per group. Cloning, forking, or otherwise duplicating a project repository with the same name before the second deadline may result in a 0% score.

## Execution

Your console should work in interactive mode and non-interactive mode, just like the Shell project in C. Sample interactive and non-interactive modes are demonstrated below:

**Interactive Mode:**
```shell
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

**Non-Interactive Mode:**
```shell
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should pass in non-interactive mode:

```shell
$ echo "python3 -m unittest discover tests" | bash
```

By following these requirements and objectives, you'll be well on your way to building a robust AirBnB console in Python. Good luck with your project!
```

  - GitHub: [Guillaume's GitHub Profile](https://github.com/guillaume)

- **Graham Olusiekwin**
