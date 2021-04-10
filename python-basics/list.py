a = ["Delta", "Tango", "Charlie"]

# Adding an element to the end of a list
a.append("Zulu")
# Adding an element to a particular index position
a.insert(4,"Alpha")

# Removing an element from the list. Element can be removed using sel, remove and pop. Del is a keyword where as
# pop and remove are inbuilt functions. Remove takes the value as an input to remove element from the list.
# pop and del takes index element to remove an element
del a[1]
a.pop(0)
a.remove('Charlie')

# Sorting an element from the list
a.sort()

print(a)

# Extending
# Extending a list is adding another list to the current list of elements. The extend function takes list as an input
lis1 = [1,2,3,4]
lis2 = [5,6,7,8]
lis1.extend(lis2)

print(lis1)

# Slicing and striding a list
print(lis1[0:2:2])

# Displaying elements within a list
for i in range(0, len(lis1)):
    print(lis1[i], end=",")

# list comparison
a = [1,2,3,4]
b = [4,3,2,1]

a == b
a is b

[1,2,3,4] == [4,3,2,1]

# Removing all the elements from the list
lis1.clear()
print(lis1)
