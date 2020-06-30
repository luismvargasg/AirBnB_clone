# AirBnB clone - The console

> This directory contains all the tasks of the project "00x00. AirBnB clone - The console" at [Holberton School](https://www.holbertonschool.com "Holberton School.")

![GitHub repo size](https://img.shields.io/github/repo-size/luismvargasg/AirBnB_clone?style=for-the-badge) ![GitHub last commit](https://img.shields.io/github/last-commit/luismvargasg/AirBnB_clone?style=for-the-badge) ![GitHub contributors](https://img.shields.io/github/contributors/luismvargasg/AirBnB_clone?style=for-the-badge) [![Luis Miguel Vargas](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2Fluismvargasg1)](https://twitter.com/luismvargasg1) [![Twitter URL](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FCristiand187)](https://twitter.com/Cristiand187)

## Table of Contents

- [AirBnB clone - The console](#airbnb-clone---the-console)
	- [Table of Contents](#table-of-contents)
	- [Project Description](#project-description)
	- [Command Interpreter Description](#command-interpreter-description)
		- [How to start it](#how-to-start-it)
		- [How to use it](#how-to-use-it)
		- [Examples](#examples)
	- [Project General Objectives](#project-general-objectives)
	- [Directory Files Description](#directory-files-description)
	- [Prerequisites](#prerequisites)
	- [Built With](#built-with)
	- [AUTHORS](#authors)
	- [License](#license)
	- [Acknowledgments](#acknowledgments)

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

### How to use it

**Interactive Mode:**

**Non-Interactive Mode:**

### Examples

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

## Directory Files Description

| **File** | **Description** |
|----------|-----------------|
| [BaseModel](./models/base_model.py) | Class BaseModel that defines all common attributes/methods for other classes |
| [File Storage](./models/engine/file_storage.py) | Serialized instances in a JSON file |

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