# Introduction

The repository contains the advance and the basic concepts of python along with some basic coding examples. These concepts are the core of the language python and should be well versed. I have tried covering as much as possible. In case if there are gaps please fell free to add topics and their respective documentation to this repo. Please adhere to the documentation structure. Concepts are written down in a mark down file under the `concepts` directory along with code examples that are written in the `codes` directory. The topics follow a nested structure as you can see below. Sub topics nested below the main topics has an indenation of 4 spaces (a tab). Please follow the [readme conventions](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax). Please follow the [readme rules](https://github.com/markdownlint/markdownlint/blob/main/docs/RULES.md) mentioned to avoid style errors while writing.

## Steps to start contributing

- Please clone the repo from [GitHub](https://github.com/Corefinder89/PythonConcepts)
- Please install `pre-commit package` from pip using `pip install pre-commit`.
    - Once istalled run the command `pre-commit install` to install all the respective `pre-commit hooks`.
    - Pre commit will be used to make sure that the commits up to the standard.
    - The same set of linters are running in the workflow as well. So, in case the standards are not met the commits will not get merged to the `master` branch.
- Once the checks are successful please raise a PR and get it reviewed before merging to master.
- Please ensure your informations are correct and add a code reference to each and every topic.

## Index

- [Object-oriented programming concepts in python](concpets/object-oriented-concepts.md)
- [Namespaces and scope in python](concepts/namespacesandscopes.md)
    - [Global vs Local variable](concepts/variabletypesinpython.md)
- [Overloading in python](concepts/overloading.md)
    - [Method overloading in python](concepts/methodoverloading.md)
- [Special variables in python]
- [Demystifying args and kwargs in python](concepts/arguments.md)
    - [Unpacking operator](concepts/unpackingoperator.md)
- [Method resolution order]
- [Dictionary in python](concepts/dictionary.md)
    - [Dictionary comprehension](concepts/dictionarycomprehension.md)
    - [Ordered dictionary](concepts/ordereddictionary.md)
- [Shallow vs deep copy in python](concepts/shallowdeepcopy.md)
- [Python descriptors]
- [Implementing an interface in python]
- [List in python]
- [Tuples in python]
- [String operations in python]
- [Reduce in python]
- [Map in python]
- [Filters in python]
- [Anonymous functions in pyhton]
- [Exceptions vs errors in python](concepts/exceptions.md)
    - [Exception / error hierarchy in python](concepts/exceptionerrorhierarchy.md)
- [Context manager in python]
- [Closure in python]
- [Data class in python]
- [Meta class in python]
- [Database connection with python]
- [Zip function in python]
