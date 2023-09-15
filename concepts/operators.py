# Operators in python

"""
Operatos in python are of type
1. Arithmetic operators
2. Assignment operators
3. Comparison operators
4. Logical operators
5. Identity operators
6. Membership operators
7. Bitwise operators
"""

class Arithmeticoperators:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        # Addition
        print("The sum of the two numbers is "+str(a + b))
        # Substraction
        print("The difference of the two numbers is "+str(a - b))
        # Multiplication
        print("The multiplication of the two numbers is "+str(a * b))
        # Division
        print("The division of the two numbers is "+str(a / b))
        # Modulous
        print("The modulous of the two numbers is "+str(a % b))
        # Exponentiation
        print("The exponent of the two numbers is "+str(a ** b))
        ## Floor dvision
        print("The floor division of the two numbers is "+str(a // b))


Arithmeticoperators(15, 2)

class Assignmentoperators:
    def __init__(self, x):
        self.x = x

        # Assignment operator
        a = self.x
        print("a = " + str(a))
        a += 5
        print("a = " + str(a))
        a -= 5
        print("a = " + str(a))
        a *= 5
        print("a = " + str(a))
        a /= 5
        print("a = " + str(a))
        a %= 5
        print("a = " + str(a))
        a //= 5
        print("a = " + str(a))
        a **= 5

Assignmentoperators(5)

class Comparisonoperators:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        print(a == b)
        print(a != b)
        print(a > b)
        print(a < b)
        print(a >= b)
        print(a <= b)

Comparisonoperators(5, 4)

class Logicaloperators:
    def __init__(self, x):
        self.x = x

        print(x < 5 and x > 10)
        print(x < 5 or x < 4)
        print(not(x < 5 and x < 10))

Logicaloperators(10)

class Membershipoperators:
    def __init__(self, x):
        self.x = x

        print("banana" in x)
        print("banana" not in x)

Membershipoperators(["banana", "apple", "mango"])

class Identityoperators:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        z = x

        # returns True because z is the same object as x
        print(x is z)
        # returns False because x is not the same object as y, even if they
        # have the same content
        print(x is y)
        # to demonstrate the difference betweeen "is" and "==":
        # this comparison returns True because x is equal to y
        print(x == y)

Identityoperators(["apple", "banana"], ["apple", "banana"])
