# AirBnB clone - The console

> This directory contains all the tasks of the project "00x00. AirBnB clone - The console" at [Holberton School](https://www.holbertonschool.com "Holberton School.")

![GitHub repo size](https://img.shields.io/github/repo-size/luismvargasg/AirBnB_clone?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/luismvargasg/AirBnB_clone?style=for-the-badge) ![GitHub contributors](https://img.shields.io/github/contributors/luismvargasg/AirBnB_clone?style=for-the-badge) [![Luis Miguel Vargas](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Fluismvargasg1)](https://twitter.com/luismvargasg1) [![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FCristiand187)](https://twitter.com/Cristiand187)

## Table of Contents

- [AirBnB clone - The console](#airbnb-clone---the-console)
	- [Table of Contents](#table-of-contents)
	- [Project General Objectives](#project-general-objectives)
	- [Project Description](#project-description)
	- [Command Interpreter Description](#command-interpreter-description)
		- [How to start it](#how-to-start-it)
		- [How to use it](#how-to-use-it)
		- [Examples](#examples)
	- [Directory Files Description](#directory-files-description)
	- [Prerequisites](#prerequisites)
	- [Built With](#built-with)
	- [AUTHORS](#authors)
	- [License](#license)
	- [Acknowledgments](#acknowledgments)

## Project General Objectives

* How to create a Python package.
* How to create a command interpreter in Python using the cmd module.
* What is Unit testing and how to implement it in a large project.
* How to serialize and deserialize a Class.
* How to write and read a JSON file.
* How to manage datetime.
* What is an UUID.
* What is *args and how to use it.
* What is **kwargs and how to use it.
* How to handle named arguments in a function.

## Project Description

The Airbnb clone is one of the main projects at Holberton School, it's a long term project that we need to accomplish by building up trough a series of small modules or pieces. This project is thinking as a whole for a software developer, to learn and become a full-stack developer, gluing alltogether the infrastructure of the Airbnb from back to front, including databases, static and dynamic content, web frameworks, APIs, and web infrastructure.
The first step that we need to build is "the console" or the command interpreter, this is meant to be a tool to validate or manipulate the storage system, through the console we are gonna be able of:
*  Create our data model.
* Manage (create, update, destroy, etc) objects.
* Store and persist objects to a file (JSON file)

This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”.

## Command Interpreter Description

A command interpreter is a program designed to read lines of text "commands" entered by the user, after read the line the interpreter "understand" and "execute" the command giving to the user the response of what he expects, it could be printing some information, moving some file or anything else. In our case, by using our console we are going to be able to manage the objects of our project:

* Create a new object (ex: a new User or a new Place).
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…).
* Update attributes of an object.
* Destroy an object.

### How to start it

The first step is to clone this repository to download all the needed files to run this console. All files are already in executable mode, and all the folders contains the __init__.py file to covert this folders into packages.

Then you need to execute in your console the executable file console.py:
```
user@ubuntu:~/AirBnB$ ./console.py
```

The command prompt is started and it should show the next line:

```
(hbnb)
```

If you type help you can see the documented commands you can use inside the console:
```
user@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
user@ubuntu:~/AirBnB$
```

### How to use it

Once you are into the console you can use it in two ways:

**Interactive Mode:**

```
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

```
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

### Examples

Here we are going to show you some examples of how to use it, if you don't see here some example of a command you can use the **help** command plus the command you are interested for to see more information.

```
user:~/AirBnB_clone$ ./console.py
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
(hbnb)help EOF
EOF command to exit the program
(hbnb)help show
Prints the string representation of an instance based on the class
        name and id. Ex: $ show BaseModel 1234-1234-1234.

(hbnb)all
["[BaseModel] (c2b13498-612b-402d-8867-c651d8a3e300) {'id': 'c2b13498-612b-402d-8867-c651d8a3e300', 'created_at': datetime.datetime(2020, 7, 1, 6, 6, 58, 992599), 'updated_at': datetime.datetime(2020, 7, 1, 6, 6, 58, 992620)}", "[BaseModel] (06d0b1de-64bd-4d09-a4d8-8bab4946ab79) {'id': '06d0b1de-64bd-4d09-a4d8-8bab4946ab79', 'created_at': datetime.datetime(2020, 7, 1, 6, 5, 12, 270928), 'updated_at': datetime.datetime(2020, 7, 1, 6, 5, 12, 271022)}", "[BaseModel] (0c487f26-6f60-42e6-9562-4da485c8f36c) {'id': '0c487f26-6f60-42e6-9562-4da485c8f36c', 'created_at': datetime.datetime(2020, 7, 1, 6, 6, 53, 321446), 'updated_at': datetime.datetime(2020, 7, 1, 6, 6, 53, 321471)}"]
(hbnb)show c2b13498-612b-402d-8867-c651d8a3e300
** class doesn't exist **
(hbnb)show BaseModel c2b13498-612b-402d-8867-c651d8a3e300
[BaseModel] (c2b13498-612b-402d-8867-c651d8a3e300) {'id': 'c2b13498-612b-402d-8867-c651d8a3e300', 'created_at': datetime.datetime(2020, 7, 1, 6, 6, 58, 992599), 'updated_at': datetime.datetime(2020, 7, 1, 6, 6, 58, 992620)}
(hbnb)
(hbnb)update
** class name missing **
(hbnb)update BaseName
** class doesn't exist **
(hbnb)quit
user:~/AirBnB_clone$
```

If you want to create a new BaseModel you can type:
```
(hbnb)create
** class name missing **
(hbnb)create BaseModel
0c5ac80d-58f4-45f0-b824-b0c2e677f2bb
(hbnb)
```
Notice that if you miss one required argument, the program gives you an advise of what you are missing.
If you want to show the object you just made you can type:
```
(hbnb)show BaseModel 0c5ac80d-58f4-45f0-b824-b0c2e677f2bb
[BaseModel] (0c5ac80d-58f4-45f0-b824-b0c2e677f2bb) {'updated_at': datetime.datetime(2020, 7, 2, 0, 44, 16, 864379), 'created_at': datetime.datetime(2020, 7, 2, 0, 44, 16, 864364), 'id': '0c5ac80d-58f4-45f0-b824-b0c2e677f2bb'}
(hbnb)
```

## Directory Files Description

| **File** | **Description** |
|----------|-----------------|
| [File Storage](./models/engine/file_storage.py) | Module that serializes instances in a JSON file and deserializes JSON file to instances. |
| [Console](./console.py) | Program that contains the entry point of the command interpreter. |
| [BaseModel](./models/base_model.py) | Class BaseModel that defines all common attributes/methods for other classes. |
| [Amenity](./models/amenity.py) | File that contains the Amenity class that inherit from BaseModel. |
| [City](./models/city.py) | File that contains the City class that inherit from BaseModel. |
| [Place](./models/place.py) | File that contains the Place class that inherit from BaseModel. |
| [Review](./models/review.py) | File that contains the Review class that inherit from BaseModel. |
| [State](./models/state.py) | File that contains the State class that inherit from BaseModel. |
| [User](./models/user.py) | File that contains the User class that inherit from BaseModel. |
| [AUTHORS](./AUTHORS) | File that contains the AUTHORS of this project. |
| [TESTS](./tests) | Directory that contains all the Unittest files to test the different classes and methods. |

## Prerequisites

This program was made and tested using Ubuntu 14.04.3 LTS and Python 3.4.3 So we recommend you to test this command interpreter under this conditions.

## Built With

* Ubuntu 14.04.3 LTS Running on a Virtual Machine "Vagrant"
* GNU Emacs 24.3.1
* Python 3.4.3

## AUTHORS

**Luis Miguel Vargas**

* [Github @luismvargasg](https://github.com/luismvargasg)
* [LinkedIn - Luis Miguel Vargas](https://www.linkedin.com/in/luismvargasg/)

**Cristian Pineda Vargas**

* [Github @Cristiand187](https://github.com/Cristiand187)
* [LinkedIn - Cristian Pineda Vargas](https://www.linkedin.com/in/cristian-david-pineda-vargas-b28a49b1/) 

## License

Opensource project.

## Acknowledgments

* Project made at Holberton School - Colombia.