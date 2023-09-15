# Dictionary comprehension

A dictionary comprehension takes the form *{key: value for (key, value) in iterable}*

Here we have two lists named keys and value and we are iterating over them with the help of zip() function.

```python
# Python code to demonstrate dictionary comprehension

# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

# but this line shows dict comprehension here
myDict = { k:v for (k,v) in zip(keys, values)}

# We can use below too
# myDict = dict(zip(keys, values))

print (myDict)
```

## Using fromkeys() method

fromkeys() method returns a dictionary with specific keys and values

```python
dic=dict.fromkeys(range(5), True)

print(dic)
```

## Using dictionary comprehension

```python
# Python code to demonstrate dictionary creation using list comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)
```

## Using conditional statements in dictionary comprehension

We can use Dictionary comprehensions with if and else statements and with other expressions too.

```python
# Python code to demonstrate dictionary comprehension using if.
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)
```

## Using nested dictionary comprehension

```python
# given string
l="GFG"

# using dictionary comprehension
dic = {
    x: {y: x + y for y in l} for x in l
}

print(dic)
```
