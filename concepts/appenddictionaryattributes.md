# Appending new attributes to a dictionary instance

OrderedDict objects have a `.__dict__` attribute that you can’t find in regular dictionary objects.

```python
from collections import OrderedDict

letters = OrderedDict(b=2, d=4, a=1, c=3)
print(letters.__dict__)
```

In the first example, you access the `.__dict__` attribute on the ordered dictionary letters. Python internally uses this attribute to store writable instance attributes. The second example shows that regular dictionary objects don’t have a `.__dict__` attribute.

You can use the ordered dictionary’s `.__dict__` attribute to store dynamically created writable instance attributes. There are several ways to do this. For example, you can use a dictionary-style assignment, like in `ordered_dict.__dict__["attr"] = value`. You can also use the dot notation, like in `ordered_dict.attr = value`.

Here’s an example of using `.__dict__` to attach a new function to an existing ordered dictionary

```python
from collections import OrderedDict
letters = OrderedDict(b=2, d=4, a=1, c=3)

letters.sorted_keys = lambda: sorted(letters.keys())
print(vars(letters))

print(letters.sorted_keys())

letters["e"] = 5

print(letters.sorted_keys())
```

Now you have a `.sorted_keys()` lambda function attached to your letters ordered dictionary. Note that you can inspect the content of `.__dict__` either by accessing it directly with the dot notation or by using `vars()`

```text
Note: This kind of dynamic attribute is added to a particular instance of a given class. In the above example, that instance is letters. This affects neither other instances nor the class itself, so you only have access to .sorted_keys() through letters.
```

You can use this dynamically added function to iterate through the dictionary keys in sorted order without altering the original order in letters

## Codebase

[Reference codebase](../codes/dictionaryattribute.py)
