# Exceptions vs syntax errors

Syntax errors occur when the parser detects an incorrect statement. Exception occurs when a syntactically correct
code results in an error

```text
print(0/0)) # Syntax error
print(1/0) # Exception
```

## Raising an exception

Raising an exception means if there is an exception that needs to be thrown explicitly based on a condition then it
is called raising an `exception`.

```python
x = 10
if x > 5:
    raise Exception("The value of x should not exceed 5. The value was %d" % x)
```

So raise is basically used to force an exception

## Try and except block handling exception

The try and except block in Python is used to catch and handle exceptions. Python executes code following the try statement as a “normal” part of the program. The code that follows the except statement is the program’s response to any

## Exceptions in the preceding try clause

```python
import sys
assert("linux" in sys.platform), "Function can run only on linux systems"

import sys
try:
    assert("linux" in sys.platform)
except AssertionError:
    print("Function can run only on linux system")

# The else clause
import sys
try:
    assert("linux" in sys.platform)
except AssertionError:
    print("Function can run only on linux system")
else:
    print(f"This is a {sys.platform} platform")
```

You can also use try except block inside the else clause

## Using the finally clause

Executing any code irrespective of any exception is done using finally clause

```python
import sys
try:
    assert("linux" in sys.platform)
except AssertionError:
    print("Function can run only on linux system")
else:
    print(f"This is a {sys.platform} platform")
finally:
    print("Running assertion to check if platform is darwin")

```

## Exception pointers

- `Raise` allows you to throw an exception at any time.
- assert enables you to verify if a certain condition is met and throw an exception if it isn’t.
- In the `try` clause, all statements are executed until an exception is encountered.
- `except` is used to catch and handle the exception(s) that are encountered in the `try` clause.
- `else` lets you code sections that should run only when no exceptions are encountered in the `try` clause.
- `finally` enables you to execute sections of code that should always run, with or without any previously encountered exceptions.
- In Python, all exceptions must be instances of a class that derives from `BaseException` class.
- To get the built-ins exceptions within python using the built in function `local()`

```python
print(dir(locals()['__builtins__']))
```

Here `locals()['__builtins__']` will return a module of built-in exceptions, functions and attributes

## Types of exceptions

### Python built in exceptions

| Exception             | Cause of error                                                                                                             |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------|
| AssertionError        | Raised when an assert statement fails.                                                                                     |
| AttributeError        | Raised when attribute assignment or reference fails.                                                                       |
| EOFError              | Raised when the input() function hits end-of-file condition.                                                               |
| FloatingPointError    | Raised when a floating point operation fails.                                                                              |
| GeneratorExit         | Raise when a generator's close() method is called.                                                                         |
| ImportError           | Raised when the imported module is not found.                                                                              |
| IndexError            | Raised when the index of a sequence is out of range.                                                                       |
| KeyError              | Raised when a key is not found in a dictionary.                                                                            |
| KeyboardInterrupt     | Raised when the user hits the interrupt key (Ctrl+C or Delete).                                                            |
| MemoryError           | Raised when an operation runs out of memory.                                                                               |
| NameError             | Raised when a variable is not found in local or global scope.                                                              |
| NotImplementedError   | Raised by abstract methods.                                                                                                |
| OSError               | Raised when system operation causes system related error.                                                                  |
| OverflowError         | Raised when the result of an arithmetic operation is too large to be represented.                                          |
| ReferenceError        | Raised when a weak reference proxy is used to access a garbage collected referent.                                         |
| RuntimeError          | Raised when an error does not fall under any other category.                                                               |
| StopIteration         | Raised by next() function to indicate that there is no further item to be returned by iterator.                            |
| SyntaxError           | Raised by parser when syntax error is encountered.                                                                         |
| IndentationError      | Raised when there is incorrect indentation.                                                                                |
| TabError              | Raised when indentation consists of inconsistent tabs and spaces.                                                          |
| SystemError           | Raised when interpreter detects internal error.                                                                            |
| SystemExit            | Raised by sys.exit() function.                                                                                             |
| TypeError             | Raised when a function or operation is applied to an object of incorrect type.                                             |
| UnboundLocalError     | Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable. |
| UnicodeError          | Raised when a Unicode-related encoding or decoding error occurs.                                                           |
| UnicodeEncodeError    | Raised when a Unicode-related error occurs during encoding.                                                                |
| UnicodeDecodeError    | Raised when a Unicode-related error occurs during decoding.                                                                |
| UnicodeTranslateError | Raised when a Unicode-related error occurs during translating.                                                             |
| ValueError            | Raised when a function gets an argument of correct type but improper value.                                                |
| ZeroDivisionError     | Raised when the second operand of division or modulo operation is zero                                                     |

## Python user defined exceptions

### Defining custom exceptions

In Python, we can define custom exceptions by creating a new class that is derived from the built-in `Exception` class.

Here's the syntax to define custom exceptions.

```python
class CustomError(Exception):
    pass
try:
    print("Execute try block")
except CustomError:
    print("Execute exception block")
```

Here, `CustomError` is a user-defined error which inherits from the Exception class.

For example,

```python
# define Python user-defined exceptions
class InvalidAgeException(Exception):
    print("Raised when the input value is less than 18")
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")

except InvalidAgeException:
    print("Exception occurred: Invalid Age")
```

### Customizing exception classes

For example,

```python
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)
```

Here, we have overridden the constructor of the Exception class to accept our own custom arguments salary and message.
Then, the constructor of the parent Exception class is called manually with the self.message argument using `super()`.
The custom self.salary attribute is defined to be used later. The inherited `__str__` method of the Exception class is
then used to display the corresponding message when SalaryNotInRangeError is raised.
