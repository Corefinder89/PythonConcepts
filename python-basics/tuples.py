# Python Tuples
# Python provides another type that is an ordered collection of objects, called a tuple.

# Defining and using tuples
# Tuples are identical to lists in all respects, except for the following properties:
# 1. Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
# 2. Tuples are immutable.
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
t
t[0]
t[-1]
t[1::2]

# Everything for lists which is that they are ordered, they can contain arbitrary objects,
# they can be indexed and sliced, they can be nested—is true of tuples as well.
# But they can’t be modified
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
t[2] = 'Bark!'

# Why use a tuple instead of a list?
# 1. Program execution is faster when manipulating a tuple than it is for the
# equivalent list. (This is probably not going to be noticeable when the list or tuple is small.)
# 2. Sometimes you don’t want data to be modified. If the values in the collection
# are meant to remain constant for the life of the program, using a tuple instead of a list guards against accidental modification.
# 3. There is another Python data type that you will encounter shortly called a dictionary,
# which requires as one of its components a value that is of an immutable type.
# A tuple can be used for this purpose, whereas a list can’t be.

# Tuple ambiguity
# When you are defining a tuple you can enter an empty tuple or with any value inside a tuple python
# recognises it as a tuple during interpretation. But what happens when you are trying to define a tuple
# with one item
t = (2)
type(t)
t = ("string")
type(t)
# It will consider the type to be either a int object or string object since parentheses are also used
# in operator precendence in expressions
# So to overcome this you need to add a trailing , after the item. For example
t = (2)
can be represented as t = (2,)
t = ("string")
can be represented as t = ("string",)
# This is called a singleton tuple

# Tuple assignment packing and unpacking
# Tuple packing is assigning items to a single object
t = ('foo', 'bar', 'baz', 'qux')
# Tuple unpacking can be done by
(s1,s2,s3,s4)=t
# When unpacking, the number of variables on the left must match the number of values in the tuple

# Packing and unpacking can be combined into one statement to make a compound assignment
(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')

# Tuples are faster than list
# In python we have two types of objects. 1. Mutable, 2. Immutable.
# In python lists comes under mutable objects and tuples comes under immutable objects.
# Tuples are stored in a single block of memory. Tuples are immutable so, It doesn't
# require extra space to store new objects.
# Lists are allocated in two blocks: the fixed one with all the Python object
# information and a variable sized block for the data.
# It is the reason creating a tuple is faster than List.
# It also explains the slight difference in indexing speed is faster than lists,
# because in tuples for indexing it follows fewer pointers.
