from collections import OrderedDict

letters = OrderedDict(b=2, d=4, a=1, c=3)

letters.sorted_keys = lambda: sorted(letters.keys())
print("Adding attribute to an existing dictionary instance")
print(vars(letters))

print("Using the attribute")
print(letters.sorted_keys())

letters["e"] = 5

print("Adding attribute to an exsiting attribute instance")
print(letters.sorted_keys())

print("Iterating through the dictionary keys in sorted order without altering the original order in letters")
for key in letters.sorted_keys():
    print(key, "->", letters[key])

print(letters)
