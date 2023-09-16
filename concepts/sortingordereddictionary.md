# Sorting

## Sorting an ordered dictionary using keys

`.move_to_end()` can be used to sort an ordered dictionary by keys.

```python
from collections import OrderedDict

print("This is an example to sort an ordered dictionary using the method .move_to_end()")

letters = OrderedDict(b=2, d=4, a=1, c=3)

for key in sorted(letters):
    letters.move_to_end(key)

print(letters)
```

In this example, you first create an ordered dictionary, letters. The for loop iterates over its sorted keys and moves every item to the end of the dictionary. When the loop finishes, your ordered dictionary has its items sorted by keys.

## Sorting an ordered dictionary using values

```python
from collections import OrderedDict

letters = OrderedDict(a=4, b=3, d=1, c=2)

print("This is an example to sort an ordered dictionary using the method .move_to_end() using values")

for key, _ in sorted(letters.items(), key=lambda item: item[1]):
    letters.move_to_end(key)

print(letters)
```

In this code, you use a lambda function that returns the value of each key-value pair in letters. The call to `sorted()` uses this lambda function to extract a comparison key from each element of the input iterable, `letters.items()`. Then you use `.move_to_end()` to sort letters.

## Codebase

[Reference Codebase](../codes/sortingordereddictionary.py)
