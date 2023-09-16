from collections import OrderedDict

print("This is an example to sort an ordered dictionary using the method .move_to_end() using keys")

letters = OrderedDict(b=2, d=4, a=1, c=3)

for key in sorted(letters):
    letters.move_to_end(key)

print(letters)

print("This is an example to sort an ordered dictionary using the method .move_to_end() using values")

letters = OrderedDict(a=4, b=3, d=1, c=2)

for key, _ in sorted(letters.items(), key=lambda item: item[1]):
    letters.move_to_end(key)

print(letters)
