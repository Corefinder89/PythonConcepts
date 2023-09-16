# Testing dictionary equality

When you test two OrderedDict objects for equality in a Boolean context, the order of items plays an important role. For example, if your ordered dictionaries contain the same set of items, then the result of the test depends on their order

```python
from collections import OrderedDict

letters_0 = OrderedDict(a=1, b=2, c=3, d=4)
letters_1 = OrderedDict(b=2, a=1, c=3, d=4)
letters_2 = OrderedDict(a=1, b=2, c=3, d=4)

print(letters_0 == letters_1)
print(letters_0 == letters_2)
```

In this example, `letters_1` has a slight difference in the order of its items compared to `letters_0` and `letters_2`, so the first test returns False. On the second test, `letters_0` and `letters_2` have the same set of items, which are in the same order, so the test returns `True`.

If you try this same example using regular dictionaries, then you’ll get a different result.

```python
letters_0 = dict(a=1, b=2, c=3, d=4)
letters_1 = dict(b=2, a=1, c=3, d=4)
letters_2 = dict(a=1, b=2, c=3, d=4)

print(letters_0 == letters_1)
print(letters_0 == letters_2)

print(letters_0 == letters_1 == letters_2)
```

Here, when you test two regular dictionaries for equality, you get True if both dictionaries have the same set of items. In this case, the order of items doesn’t change the final result.

Finally, equality tests between an OrderedDict object and a regular dictionary don’t take the order of items into account

```python
letters_0 = OrderedDict(a=1, b=2, c=3, d=4)
letters_1 = dict(b=2, a=1, c=3, d=4)

print(letters_0 == letters_1)
```

## Codebase

[Reference Codebase](../codes/testingdictionaryequality.py)
