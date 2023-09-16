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
from collections import OrderedDict

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
from collections import OrderedDict

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
from collections import OrderedDict

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
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
numbers["one"] = 1.0
print(numbers)
numbers.update(two=2.0)
print(numbers)
```

If you update the value of a given key in an ordered dictionary, then the key isn’t moved but assigned the new value in place. In the same way, if you use .update() to modify the value of an existing key-value pair, then the dictionary remembers the position of the key and assigns the updated value to it.

### Iterating over an OrderedDict

Just like with regular dictionaries, you can iterate through an OrderedDict object using several tools and techniques. You can iterate over the keys directly, or you can use dictionary methods, such as `.items()`, `.keys()`, and `.values()`

```python
from collections import OrderedDict

# Iterating over dictionaries
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
```

The first for loop iterates over the keys of numbers directly. The other three loops use dictionary methods to iterate over the items, keys, and values of numbers.

## Iterating in Reveresed order with reversed()

Another important feature that OrderedDict has provided since `Python 3.5` is that its items, keys, and values support reverse iteration using `reversed()`. This feature was added to regular dictionaries in `Python 3.8`. So, if your code uses it, then your backward compatibility is much more restricted with normal dictionaries.

You can use reversed() with the items, keys, and values of an OrderedDict object

```python
from collections import OrderedDict

# Iterating over dictionaries in reversed order
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
```

Every loop in this example uses `reversed()` to iterate through different elements of an ordered dictionary in reverse order.

Regular dictionaries also support reverse iteration. However, if you try to use `reversed()` with a regular dict object in a Python version lower than `3.8`, then you get a `TypeError`.

## Enhanced methods of OrderedDict

Since Python 3.6, regular dictionaries have kept their items in the same order that they were inserted into the underlying dictionary. This limits the usefulness of OrderedDict, as you’ve seen so far. However, OrderedDict provides some unique features that you can’t find in a regular dict object.

With an ordered dictionary, you have access to the following extra and enhanced methods:

- `.move_to_end()` is a new method added in Python 3.2 that allows you to move an existing item either to the end or to the beginning of the dictionary.

- `.popitem()` is an enhanced variation of its `dict.popitem()` counterpart that allows you to remove and return an item from either the end or the beginning of the underlying ordered dictionary.

OrderedDict and dict also behave differently when they’re tested for equality. Specifically, when you compare ordered dictionaries, the order of items matters. That’s not the case with regular dictionaries.

Finally, OrderedDict instances provide an attribute called `.__dict__` that you can’t find in a regular dictionary instance. This attribute allows you to add custom writable attributes to an existing ordered dictionary.

### Reordering items with move_to_end()

One of the more remarkable differences between dict and OrderedDict is that the latter has an extra method called .move_to_end(). This method allows you to move existing items to either the end or the beginning of the underlying dictionary, so it’s a great tool for reordering a dictionary.

When you use `.move_to_end()`, you can supply two arguments:

- `key` holds the key that identifies the item you want to move. If key doesn’t exist, then you get a KeyError.

- `last` holds a boolean value that defines to which end of the dictionary you want to move the item at hand. It defaults to `True`, which means that the item will be moved to the end, or right side, of the dictionary. `False` means that the item will be moved to the front, or left side, of the ordered dictionary.

Here’s an example of how to use .move_to_end() with a key argument and relying on the default value of last

```python
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)
numbers.move_to_end("one")
print(numbers)
```

When you call .move_to_end() with a key as an argument, you move the key-value pair at hand to the end of the dictionary. That’s why ('one', 1) is in the last position now. Note that the rest of the items remain in the same original order.

If you pass False to last, then you move the item to the beginning

```python
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)
print(numbers)
print("Before using last=False")
numbers.move_to_end("one")
print(numbers)
print("After using last=False")
numbers.move_to_end("one", last=False)
print(numbers)
```

## Removing items with popitems()

Another interesting feature of OrderedDict is its enhanced version of `.popitem()`. By default, .popitem() removes and returns an item in `LIFO` (Last-In/First-Out) order. In other words, it removes items from the right end of the ordered dictionary

```python
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

print(numbers.popitem())
print(numbers.popitem())
print(numbers.popitem())
```

Here, you remove all the items from numbers using .popitem(). Every call to this method removes a single item from the end of the underlying dictionary. If you call .popitem() on an empty dictionary, then you get a KeyError. Up to this point, .popitem() behaves the same as in regular dictionaries.

In OrderedDict, however, .popitem() also accepts a Boolean argument called last, which defaults to True. If you set last to False, then .popitem() removes the items in FIFO (First-In/First-Out) order, which means that it removes items from the beginning of the dictionary.

```python
from collections import OrderedDict

numbers = OrderedDict(one=1, two=2, three=3)

print(numbers.popitem(last=False))
print(numbers.popitem(last=False))
print(numbers.popitem(last=False))
```

With last set to False, you can use .popitem() to remove and return items from the beginning of an ordered dictionary. In this example, the last call to .popitem() raises a KeyError because the underlying dictionary is already empty.

## Merging and updating dictionaries with operators

Python 3.9 added two new operators to the dictionary space. Now you have merge `(|)` and update `(|=)` dictionary operators. These operators also work with OrderedDict instances

```python
from collections import OrderedDict

physicists = OrderedDict(newton="1642-1726", einstein="1879-1955")
biologists = OrderedDict(darwin="1809-1882", mendel="1822-1884")

scientists = physicists | biologists
print(scientists)
```

As its name suggests, the merge operator merges the two dictionaries into a new one that contains the items of both initial dictionaries. If the dictionaries in the expression have common keys, then the rightmost dictionary’s values will prevail.

The update operator is handy when you have a dictionary and want to update some of its values without calling .update()

```python
from collections import OrderedDict

physicists = OrderedDict(newton="1642-1726", einstein="1879-1955")

physicists_1 = OrderedDict(newton="1642-1726/1727", hawking="1942-2018")
physicists |= physicists_1
print(physicists)
```
