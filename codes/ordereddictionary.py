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
