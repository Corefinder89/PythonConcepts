# Defining a set
# Python’s built-in set type has the following characteristics:
# Sets are unordered.
# Set elements are unique. Duplicate elements are not allowed.
# A set itself may be modified, but the elements contained in the set must be
# of an immutable type.

# So a set can be created using the built-in set() function
# set(<iter>). Iter is an iterable that includes list or tuple
x = set(["foo", "bar", "baz", "foo", "qux"])
x = set(("foo", "bar", "baz", "foo", "qux"))

# Strings are also iterable, so a string can be passed to set() as well.
# You have already seen that list(s) generates a list of the characters in
# the string s. Similarly, set(s) generates a set of the characters in s

s = "string1"
list(s)
set(s)

# The resulting sets are unordered: the original order, as specified in the
# definition, is not necessarily preserved. Additionally, duplicate values are
# only represented in the set once.

# Set comparison
You can compare 2 sets in order to get results. For example
list1 = ["String1", "String1", "String2", "String3", "String4"]
list2 = ["String1", "String2", "String3", "String4"]
set(list1) == set(list2)

# Note:
# The argument to set() is an iterable. It generates a list of elements to be
# placed into the set.
# But a dictionary or a list cannot be a part of the set element. This is because
# a list or a dictionary are mutable objects.

# Set size and membership
# You can check the size of a set using the len function
len(x1)

"bar" in x1
"qux" not in x2

# Set union
# Given two sets, x1 and x2, the union of x1 and x2 is a set consisting
# of all elements in either set
x1 = {"foo", "bar", "baz"}
x2 = {"baz", "qux", "quux"}
# The union of x1 and x2 is {"foo", "bar", "baz", "qux", "quux"}
x1 | x2
# Set union can also be obtained with the .union() method. The method is invoked
# on one of the sets, and the other is passed as an argument
x1.union(x2)

# When you use the | operator, both operands must be sets. The .union() method,
# on the other hand, will take any iterable as an argument, convert it to a set,
# and then perform the union. For example

x1 | ("foo", "bar", "tango")
# This will give an error

# But on the other hand if we use the function union()
x1.union(("foo", "bar", "tango"))

# More than two sets may be specified with either the operator or the method
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
a.union(b, c, d)
a | b | c | d

# Intersection of two sets
# Return the set of elements common to both x1 and x2
x2 = {"baz", "qux", "quux"}
x1.intersection(x2)
x1 & x2

# You can specify multiple sets with the intersection method and operator, just
# like you can with set union
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
a.intersection(b, c, d)
a & b & c & d

# Difference between two sets
# Return all elements which are present in the set x1 but not in x2
x1 = {"foo", "bar", "baz"}
x2 = {"baz", "qux", "quux"}
x1.difference(x2)
x1 - x2

# Multiple operations can be done on difference using
a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}
a.difference(b, c)
a - b - c
    
