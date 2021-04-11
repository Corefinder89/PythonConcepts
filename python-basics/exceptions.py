# Exceptions vs syntax errors
# Syntax errors occur when the parser detects an incorrect statement
# Exception occurs when a syntactically correct code results in an error
print(0/0)) # Syntax error
print(1/0) # Exception

# Raising an exception
# raising an exception means if there is an exception that needs to be thrown explicitly
# based on a condition then it is called raising an exception
x = 10
if x > 5:
    raise Exception("The value of x should not exceed 5. The value was %d" % x)
# So raise is basically used to force an exception

# Try and except block handling exception
# The try and except block in Python is used to catch and handle exceptions.
# Python executes code following the try statement as a “normal” part of the program.
# The code that follows the except statement is the program’s response to any
# exceptions in the preceding try clause.

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

# You can also use try except block inside the else clause

# Using the finally clause
# Executing any code irrespective of any exception is done using finally clause
import sys
try:
    assert("linux" in sys.platform)
except AssertionError:
    print("Function can run only on linux system")
else:
    print(f"This is a {sys.platform} platform")
finally:
    print("Running assertion to check if platform is darwin")


# Exception pointers
# 1. raise allows you to throw an exception at any time.
# 2. assert enables you to verify if a certain condition is met and throw an
# exception if it isn’t.
# 3. In the try clause, all statements are executed until an exception is
# encountered.
# 4. except is used to catch and handle the exception(s) that are encountered
# in the try clause.
# 5. else lets you code sections that should run only when no exceptions are
# encountered in the try clause.
# 6. finally enables you to execute sections of code that should always run,
# with or without any previously encountered exceptions.
# 7. In Python, all exceptions must be instances of a class that derives from
# BaseException class.
# 8. To get the built-ins exceptions within python using the built in function
# local() - print(dir(locals()['__builtins__'])). locals()['__builtins__'] will
# return a module of built-in exceptions, functions and attributes

# Types of exceptions
# https://www.programiz.com/python-programming/exceptions
