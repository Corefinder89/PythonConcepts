# Python args and kwargs: Demystified

## Passing multiple arguments to a function

`*args` and `**kwargs` allow you to pass multiple arguments or keyword arguments to a function.

`*args` allows you to pass a varying number of positional arguments.

```python
# sum_integers_args.py
def my_sum(*args):
    result = 0

    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))
```

you’re passing three different positional arguments. my_sum() takes all the parameters that are provided in the input and packs them all into a single iterable object named `args`.

Note that args is just a name. You’re not required to use the name args. You can choose any name that you prefer, such as `integers`.

Bear in mind that the iterable object you’ll get using the unpacking operator * is not a list but a `tuple`.

## Using the Python kwargs variable in function definition

`**kwargs` works just like *args, but instead of accepting positional arguments it accepts keyword (or **named**) arguments.

```python
def concatenate(**kwargs):
    result = ""

    for arg in kwargs.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
```

Like args, kwargs is just a name that can be changed to whatever you want. Again, what is important here is the use of the `unpacking operator (**)`.

So, the previous example could be written like this

```python
def concatenate(**words):
    result = ""
    for arg in words.values():
        result += arg
    return result

print(concatenate(a="Real", b="Python", c="Is", d="Great", e="!"))
```

Note that in the example above the iterable object is a standard dict. If you iterate over the dictionary and want to return its values, like in the example shown, then you must use .values().

## Ordering arguments in a function

you have to bear in mind that order counts. Just as non-default arguments have to precede default arguments, so *args must come before **kwargs.

To recap, the correct order for your parameters is:

- Standard arguments
- *args arguments
- **kwargs arguments
