# Unpacking operators

The single and double asterisk unpacking operators were introduced in Python 2. As of the 3.5 release, they have become even more powerful, thanks to PEP 448. In short, the unpacking operators are operators that unpack the values from iterable objects in Python. The single asterisk operator `*` can be used on `any iterable` that Python provides, while the double asterisk operator `**` can only be used on `dictionaries`.

When you use the * operator to unpack a list and pass arguments to a function, it’s exactly as though you’re passing every single argument alone. This means that you can use multiple unpacking operators to get values from several lists and pass them all to a single function.

```python
# sum_integers_args_3.py
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

print("Example 4 - Unpacking multiple lists")
list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print("Sum: ", my_sum(*list1, *list2, *list3))
```

There are other convenient uses of the unpacking operator. For example, say you need to split a list into three different parts. The output should show the first value, the last value, and all the values in between.

```python
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b)
print(c)
```

Another use of the unpacking operator is to merge two lists together

```python
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)
```

The unpacking operator `*` is prepended to both my_first_list and my_second_list.

You can even merge two different dictionaries by using the unpacking operator **:

```python
print("Example")
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)
```

Remember that the * operator works on any iterable object. It can also be used to unpack a string.

```python
a = [*"RealPython"]
print(a)
```

```python
*a, = "RealPython"
print(a)
```
