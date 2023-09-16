# Inbuilt exceptions:
# Import the inspect module
import inspect as ipt


def tree_class(cls, ind=0):
    print('-' * ind, cls.__name__)
    for K in cls.__subclasses__():
        tree_class(K, ind + 3)


print("Get all the exceptions from BaseException class")
print("Inbuilt exceptions are: ")
# The inspect.getmro() will return the tuple of class which is cls's base classes.
#The next step is to create a tree hierarchy.
ipt.getclasstree(ipt.getmro(BaseException))
# function call
tree_class(BaseException)

import inspect

print("Get all the exceptions from Eceptions class")
print("The class hierarchy for built-in exceptions is:")
inspect.getclasstree(inspect.getmro(Exception))


def classtree(cls, indent=0):
    print('.' * indent, cls.__name__)
    for subcls in cls.__subclasses__():
        classtree(subcls, indent + 3)


classtree(Exception)
