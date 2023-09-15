from multipledispatch import dispatch


def product(a, b):
    p = a * b
    print(p)


def product(a, b, c):
    p = a * b * c
    print(p)


def add(datatype, *args):
    if datatype == 'int':
        ans = 0
    if datatype == 'str':
        ans = ''
    for item in args:
        ans = ans + item

    print(ans)


# passing one parameter
@dispatch(int, int)
def product(first, second):
    result = first * second
    print(result)


# passing two parameters
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)


# you can also pass data type of any value as per requirement
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)


# ov = Overload()
# ov.product(5, 4)

# add('int', 4, 5)
# add('str', 'Hello', 'Geeks')

# product(2, 3)
# product(2, 3, 2)
# product(2.2, 3.4, 2.3)
