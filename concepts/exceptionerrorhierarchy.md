# Python Exception/Error hierarchy

Python Exception hierarchy consists of various built-in exceptions. This hierarchy is used to handle various types of exceptions, as the concept of inheritance also comes into picture.

In Python, all the built-in exceptions must be the instances of a class derived from `BaseException`.

This Exception or Error hierarchy can be printed by importing the Python's `inspect module`. Using the inspect module, one can perform type checking, retrieve the source code of a method, inspects classes and functions, and examine interpreter stack.

```python
inspect.getclasstree(classes, unique = False)
```

## Get the hierarchy of BaseException class

```python
# Inbuilt exceptions:
# Import the inspect module
import inspect as ipt
def tree_class(cls, ind = 0):
    print ('-' * ind, cls.__name__)
    for K in cls.__subclasses__():
        tree_class(K, ind + 3)
print ("Inbuilt exceptions is: ")
# The inspect.getmro() will return the tuple of class which is cls's base classes.
#The next step is to create a tree hierarchy.
ipt.getclasstree(ipt.getmro(BaseException))
# function call
tree_class(BaseException)
```

In this example, we only printed the hierarchy of `BaseException` class.

## Get the hierarchy of Exception class

```python
import inspect
print("The class hierarchy for built-in exceptions is:")
inspect.getclasstree(inspect.getmro(Exception))
def classtree(cls, indent=0):
    print('.' * indent, cls.__name__)
    for subcls in cls.__subclasses__():
        classtree(subcls, indent + 3)
classtree(Exception)
```
