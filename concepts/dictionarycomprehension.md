# Dictionary comprehension

A dictionary comprehension takes the form *{key: value for (key, value) in iterable}*

Here we have two lists named keys and value and we are iterating over them with the help of zip() function.

```python
# Python code to demonstrate dictionary
# comprehension

# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

# but this line shows dict comprehension here
myDict = { k:v for (k,v) in zip(keys, values)}

# We can use below too
# myDict = dict(zip(keys, values))

print (myDict)
```
