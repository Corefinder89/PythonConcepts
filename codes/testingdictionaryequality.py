from collections import OrderedDict

print("Example to check equality between two ordered dictionaries")
letters_0 = OrderedDict(a=1, b=2, c=3, d=4)
letters_1 = OrderedDict(b=2, a=1, c=3, d=4)
letters_2 = OrderedDict(a=1, b=2, c=3, d=4)

print(letters_0 == letters_1)
print(letters_0 == letters_2)

print("Example to check equality between dictionaries")
letters_0 = dict(a=1, b=2, c=3, d=4)
letters_1 = dict(b=2, a=1, c=3, d=4)
letters_2 = dict(a=1, b=2, c=3, d=4)

print(letters_0 == letters_1)
print(letters_0 == letters_2)

print(letters_0 == letters_1 == letters_2)

print("Example to check equality between ordered dictionary and dictionary")
letters_0 = OrderedDict(a=1, b=2, c=3, d=4)
letters_1 = dict(b=2, a=1, c=3, d=4)

print(letters_0 == letters_1)
