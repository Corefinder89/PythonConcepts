# Ordered dictionary

It’s a dictionary subclass specially designed to remember the order of items, which is defined by the insertion order of keys.

## Choosing between OrderedDict and dict

For years, Python dictionaries were unordered data structures. Python developers were used to this fact, and they relied on lists or other sequences when they needed to keep their data in order. With time, developers found a need for a new type of dictionary, one that would keep its items ordered.

Back in 2008, `PEP 372` introduced the idea of adding a new dictionary class to collections. Its main goal was to remember the order of items as defined by the order in which keys were inserted. That was the origin of OrderedDict.

Core Python developers wanted to fill in the gap and provide a dictionary that could preserve the order of inserted keys. That, in turn, allowed for a more straightforward implementation of specific algorithms that rely on this property.

`OrderedDict` was added to the standard library in `Python 3.1`. Its API is essentially the same as `dict`. However, `OrderedDict` iterates over keys and values in the same order that the keys were inserted. If a new entry overwrites an existing entry, then the order of items is left unchanged. If an entry is deleted and reinserted, then it will be moved to the end of the dictionary.

`Python 3.6` introduced a new implementation of dict. This new implementation represents a big win in terms of memory usage and iteration efficiency. Additionally, the new implementation provides a new and somewhat unexpected feature: dict objects now keep their items in the same order they were introduced.

## Importance of using ordered dictionary

- **Intent signaling**: If you use OrderedDict over dict, then your code makes it clear that the order of items in the dictionary is important. You’re clearly communicating that your code needs or relies on the order of items in the underlying dictionary.

- **Control over the order of items**: If you need to rearrange or reorder the items in a dictionary, then you can use `.move_to_end()` and also the enhanced variation of `.popitem()`.

- **Equality test behaviour**: If your code compares dictionaries for equality, and the order of items is important in that comparison, then `OrderedDict` is the right choice.

There’s at least one more reason to continue using OrderedDict in your code: **backward compatibility**. Relying on regular dict objects to preserve the order of items will break your code in environments that run versions of Python older than 3.6.

## Creating OrderedDictobjects

Being a dict subclass means that it inherits all the methods a regular dictionary provides. Unlike `dict`, `OrderedDict` isn’t a built-in type, so the first step to create OrderedDict objects is to import the class from collections. There are several ways to create ordered dictionaries. Most of them are identical to how you create a regular dict object. For example, you can create an empty OrderedDict object by instantiating the class without arguments:

```python
from collections import OrderedDict

numbers = OrderedDict()

numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3

print(numbers)
```

In this case, you first import `OrderedDict` from `collections`. Then you create an empty ordered dictionary by instantiating OrderedDict without providing arguments to the constructor.

You can add key-value pairs to the dictionary by providing a key in square brackets ([]) and assigning a value to that key. When you reference numbers, you get an iterable of key-value pairs that holds items in the same order they were inserted into the dictionary.

You can also pass an iterable of items as an argument to the constructor of OrderedDict

```python
numbers = OrderedDict([("one", 1), ("two", 2), ("three", 3)])
print(numbers)

letters = OrderedDict({("a", 1), ("b", 2), ("c", 3)})
print(letters)
```

When you use a sequence, such as a list or a tuple, the order of the items in the resulting ordered dictionary matches the original order of items in the input sequence. If you use a set, like in the second example above, then the final order of items is unknown until the OrderedDict is created.

## Managing items in an OrderedDict

Since `OrderedDict` is a mutable data structure, you can perform mutating operations on its instances. You can insert new items, update and remove existing items, and so on. If you insert a new item into an existing ordered dictionary, then the item is added to the end of the dictionary.

### Inserting an item to an ordered dictionary

```python
numbers = OrderedDict(one=1, two=2, three=3)
print("Before")
print(numbers)
numbers["four"] = 4
print("After")
print(numbers)
```

The newly added item, ('four', 4), is placed at the end of the underlying dictionary, so the order of the existing items remains unaffected, and the dictionary keeps the insertion order.

### Deleting and inserting an item to an ordered dictionary

```python
numbers = OrderedDict(one=1, two=2, three=3)
print("Example 5 - deleting and inserting the same object to an orderd dictionary")
del numbers["one"]
print("Before")
print(numbers)
numbers["one"] = 1
print("After")
print(numbers)
```

If you remove the ('one', 1) item and insert a new instance of the same item, then the new item is added to the end of the underlying dictionary.

### Updating an item to an ordered dictionary

```python
numbers = OrderedDict(one=1, two=2, three=3)
numbers["one"] = 1.0
print(numbers)
numbers.update(two=2.0)
print(numbers)
```

If you update the value of a given key in an ordered dictionary, then the key isn’t moved but assigned the new value in place. In the same way, if you use .update() to modify the value of an existing key-value pair, then the dictionary remembers the position of the key and assigns the updated value to it.

### Iterating over an OrderedDict

Just like with regular dictionaries, you can iterate through an OrderedDict object using several tools and techniques. You can iterate over the keys directly, or you can use dictionary methods, such as `.items()`, `.keys()`, and `.values()`
