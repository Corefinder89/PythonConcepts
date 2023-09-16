from collections import OrderedDict

numbers = OrderedDict()

numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3

print("Example 1")
print(numbers)

numbers = OrderedDict([("one", 1), ("two", 2), ("three", 3)])
print("Example 2")
print(numbers)

letters = OrderedDict({("a", 1), ("b", 2), ("c", 3)})
print("Example 3")
print(letters)

numbers = OrderedDict(one=1, two=2, three=3)
print("Example 4 - inserting an item to an ordered dictionary")
print(numbers)
numbers["four"] = 4
print(numbers)

numbers = OrderedDict(one=1, two=2, three=3)
print("Example 5 - deleting and inserting the same object to an orderd dictionary")
del numbers["one"]
print("Before")
print(numbers)
numbers["one"] = 1
print("After")
print(numbers)

numbers = OrderedDict(one=1, two=2, three=3)
print("Example 5 - Updating an object in the ordered dictionary")
numbers["one"] = 1.0
print(numbers)
numbers.update(two=2.0)
print(numbers)

# Iterating over dictionaries
print("Example 6 - iterating over dictionaries using different methods")
numbers = OrderedDict(one=1, two=2, three=3)

# Iterate over the keys directly
for key in numbers:
    print(key, "->", numbers[key])

# Iterate over the items using .items()
for key, value in numbers.items():
    print(key, "->", value)

# Iterate over the keys using .keys()
for key in numbers.keys():
    print(key, "->", numbers[key])

# Iterate over the values using .values()
for value in numbers.values():
    print(value)

# Iterating over dictionaries in reversed order
print("Example 6 - iterating over dictionaries using different methods in the reverse order")
numbers = OrderedDict(one=1, two=2, three=3)

# Iterate over the keys directly
for key in reversed(numbers):
    print(key, "->", numbers[key])

# Iterate over the items using .items()
for key, value in reversed(numbers.items()):
    print(key, "->", value)

# Iterate over the keys using .keys()
for key in reversed(numbers.keys()):
    print(key, "->", numbers[key])

# Iterate over the values using .values()
for value in reversed(numbers.values()):
    print(value)

print("Example 7 - explaining move_to_end() using key")
numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)
numbers.move_to_end("one")
print(numbers)

print("Example 8 - explaining move_to_end() using last")
numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)
print("Before using last=False")
numbers.move_to_end("one")
print(numbers)
print("After using last=False")
numbers.move_to_end("one", last=False)
print(numbers)

print("Example 9 - Pop items from an ordered dictionary in LIFO")
numbers = OrderedDict(one=1, two=2, three=3)
print(numbers.popitem())
print(numbers.popitem())
print(numbers.popitem())

print("Example 10 - Pop items from an ordered dictionary in FIFO")
numbers = OrderedDict(one=1, two=2, three=3)
print(numbers.popitem(last=False))
print(numbers.popitem(last=False))
print(numbers.popitem(last=False))

print("Example 10 - Merging two ordered dictionaries")
physicists = OrderedDict(newton="1642-1726", einstein="1879-1955")
biologists = OrderedDict(darwin="1809-1882", mendel="1822-1884")

scientists = physicists | biologists
print(scientists)

print("Example 11 - Updating an ordered dictionary")
physicists = OrderedDict(newton="1642-1726", einstein="1879-1955")

physicists_1 = OrderedDict(newton="1642-1726/1727", hawking="1942-2018")
physicists |= physicists_1
print(physicists)
