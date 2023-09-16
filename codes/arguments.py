# sum_integers_args.py
def my_sum(*args):
    result = 0
    print("Example - 1: Using *args (positional arguments)")
    for x in args:
        result += x
    return result


print("Sum: ", my_sum(1, 2, 3))


def my_sum(*integers):
    result = 0
    print("Example 2 - Using integer keyword in place of args")
    for x in integers:
        result += x
    return result


print("Sum: ", my_sum(1, 2, 3))


def concatenate(**kwargs):
    result = ""
    print("Example 3 - Using the **kwargs (keyword arguments)")
    for arg in kwargs.values():
        result += arg
    return result


print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))


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

# extract_list_body.py
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print("Example 5 - Extracting list objects")

print(a)
print(b)
print(c)

print("Example 6 - merging two lists together")
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)

print("Example 7 - merging two dictionaries")
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)

print("Example 8 - Unpacking string method 1 (converting a string to list)")
# string_to_list.py
a = [*"RealPython"]
print(a)

print("Example 9 - Unpacking string method 1 (converting a string to list)")
# string_to_list.py
*a, = "RealPython"
print(a)
