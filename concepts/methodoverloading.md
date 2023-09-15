# Method overloading in python

Two or more methods have the same name but different numbers of parameters or different types of parameters, or both. These methods are called overloaded methods and the phenomenon is called `method overloading`.

Like other languages, python does not support method overloading by default. But there are different ways of achieving method overloading in python.

## Limitiations of method overloading in python

The problem with method overloading in Python is that we may overload the methods but can only use the latest defined method.

For example

```python
# First product method.
# Takes two argument and print their
# product


def product(a, b):
    p = a * b
    print(p)

# Second product method
# Takes three argument and print their
# product


def product(a, b, c):
    p = a * b*c
    print(p)

# Uncommenting the below line shows an error
# This will throw an error for missing positional argument

# product(4, 5)


# This line will call the second product method
product(4, 5, 5)
```

In the above code, we have defined two product methods we can only use the second product method, as python does not support method overloading. We may define many methods of the same name and different arguments, but we can only use the latest defined method. Calling the other method will produce an error. Like here calling `product(4,5)` will produce an error as the latest defined product method takes three arguments.

## Different ways to overload a method in python

### Method 1 [Not optimised]

We can use the arguments to make the same function work differently i.e. as per the arguments.

```python
# Function to take multiple arguments
def add(datatype, *args):

    # if datatype is int initialize answer as 0
    if datatype == 'int':
        answer = 0

    # if datatype is str
    # initialize answer as ''
    if datatype == 'str':
        answer = ''

    # Traverse through the arguments
    for x in args:

        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'Geeks')
```

### Method 2 [Not optimised]

We can achieve method overloading in python by user defined function using “None” keyword as default parameter.

Code explanation:

The first parameter of  “add” method is set to None. This will give us the option to call it with or without a parameter.

When we pass arguments to the add method (Working):

- The method checks if both the parameters are available or not.
- As we have already given default parameter values as “None”, if any of the value is not passed it will remain “None”.
- Using If-Else statements, we can achieve method overloading by checking each parameter as single statement.

```python
# code
def add(a=None, b=None):
    # Checks if both parameters are available
    # if statement will be executed if only one parameter is available
    if a != None and b == None:
        print(a)
    # else will be executed if both are available and returns addition of two
    else:
        print(a+b)


# two arguments are passed, returns addition of two
add(2, 3)
# only one argument is passed, returns a
add(2)
```

The problem with above methods is that, it makes code more complex with multiple if/else statement and is not the desired way to achieve the method overloading.

### Method 3 [Optimised]

By using multiple dispatch decorator

Multiple dispatch decorator can be installed using pip

`pip3 install multipledispatch`

```python
from multipledispatch import dispatch

# passing one parameter
@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)

# passing two parameters
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)

# you can also pass data type of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)

# calling product method with 2 arguments
product(2, 3) # this will give output of 6

# calling product method with 3 arguments but all int
product(2, 3, 2) # this will give output of 12

# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3) # this will give output of 17.985999999999997
```

In backend, `dispatcher` creates an object which stores different implementation and on runtime, it selects the appropriate method as the type and number of parameters passed.
