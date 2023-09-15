# Dictionary in python

Dictionary is another composite data type provided by python which is similar to a list, like a collection of objects

## Difference between a list and a dictionary

- Both are mutable.
- Both are dynamic. They can grow and shrink as needed.
- Both can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.
- Dictionaries differ from lists primarily in how elements are accessed:
  - List elements are accessed by their position in the list, via indexing.
  - Dictionary elements are accessed via keys.

## Defining a dictionary
Dictionaries are Python’s implementation of a data structure that is more generally known as an associative array (
Associative arrays, also called maps or dictionaries, are an abstract data type that can hold data in (key, value) pairs
). A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}).
A colon (:) separates each key from its associated value:

```
d = {
     <key>: <value>,
     <key>: <value>,
       .
       .
       .
     <key>: <value>
}
```
The following defines a dictionary that maps a location to the name of its corresponding states

```python
locations = {
    "Bengaluru": "Karnataka",
    "Kolkata": "West Bengal",
    "Bhopal": "Madhya Pradesh",
    "Mumbai": "Maharashtra",
    "Bhubaneswar": "Odhisa",
    "Chennai": "Tamil Nadu"
}
```

You can also construct a dictionary using the built in function called dict(). The argument to dict() should be a 
sequence of key-value pairs. A list of tuples works well for this

```
d = dict([
     (<key>, <value>),
     (<key>, <value),
       .
       .
       .
     (<key>, <value>)
])
```
So the dictionary locations can also be defined as

```python
locations = dict([
    ("Bengaluru", "Karnataka"),
    ("Kolkata", "West Bengal"),
    ("Bhopal", "Madhya Pradesh"),
    ("Mumbai", "Maharashtra"),
    ("Bhubaneswar", "Odhisa"),
    ("Chennai", "Tamil Nadu")
])
```
If the values are simple strings it can also be defined like this

```python
locations = dict(
    Bengaluru="Karnataka",
    Kolkata="West Bengal",
    Bhopal="Madhya Pradesh",
    Mumbai="Maharashtra",
    Bhubaneswar="Odhisa",
    Chennai="Tamil Nadu"
)
```

## Accessing dictionary values

A value is retrieved from a dictionary by specifying its corresponding key in square brackets ([])

```
locations["Bengaluru"]
locations["Kolkata"]
```

If you refer to a key that is not in the dictionary, Python raises a KeyError exception

## Adding an object to a dictionary

Adding an entry to an existing dictionary is simply a matter of assigning a new key and value:

`locations["Hyderabad"]="Andhra Pradesh"`

## Update an entry to a dictionary

If you want to update an entry, you can just assign a new value to an existing key:

`locations["Bhubaneswar"]="Orissa"`

## Deleting an entry

To delete an entry, use the del statement, specifying the key to delete:

`del locations["Chennai"]`

## Dictionary Keys vs. List Indices

The interpreter raises the same exception, KeyError, when a dictionary is accessed with either an undefined key or by a numeric index.
In the latter case, [1] looks like a numerical index, but it isn’t

`d = {0: 'a',1: 'b', 2: 'c', 3: 'd'}`

In the expressions d[1], d[0], and d[2], the numbers in square brackets appear as though they might be indices. But they have nothing to do with the order of the items in the dictionary.
Python is interpreting them as dictionary keys.

## Building a dictionary incrementally

You can start by creating an empty dictionary, which is specified by empty curly braces. Then you can add new keys and values one at a time:

```
person = {}
person["fname"] = "Soumyajit"
person["lname"] = "Basu"
person["age"] = 31
person["spouse"] = "Soumi"
person["pets"] = {"dog":"Fido", "cat":"sox"}
person["family_members"] = ["mother", "father", "uncle", "sister"]
```

## Get the value of a sub list using list index

`person["family_members"][1]`

## Get the value of a sub dictionary

`person["pets"]["cat"]`

## Restrictions on dictionary keys

- First, a given key can appear in a dictionary only once. Duplicate keys are not allowed. A dictionary maps each key to a corresponding value, so it doesn’t make sense to map a particular key more than once.
- Second, when you assign a value to an already existing dictionary key, it does not add the key a second time, but replaces the existing value:
- Third, if you specify a key a second time during the initial creation of a dictionary, the second occurrence will override the first
- Fourth, neither a list nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutable

## Operators in dictionary

The in and not in operators return True or False according to whether the specified operand occurs as a key in the dictionary

```python
locations = {
    "Bengaluru": "Karnataka",
    "Kolkata": "West Bengal",
    "Bhopal": "Madhya Pradesh",
    "Mumbai": "Maharashtra",
    "Bhubaneswar": "Odhisa",
    "Chennai": "Tamil Nadu"
}
```

`"Chennai" in locations
"Indore" in locations`

## Built in functions

### Clear

clear() -> empties a dictionary of all key-value pairs 

`locations.clear()`

### Get

get() -> returns the value of a key if exists in a dictionary 

`locations.get("Bengaluru")`

### Items

items() -> returns a list of key-value pairs in a dictionary. 

`locations.items()`. 

This returns a list of tuples containing the key-value pairs in items `locations.items()`

### Keys

keys() -> returns a list of all keys within a dictionary 

`locations.keys()`

### Values

values() -> returns a list of all values mapped to the keys within a dictionary 

`locations.values()`

### Pop

pop() -> removes a key from a dictionary if it is present and returns its value. `pop()` raises a KeyError exception if <key> is not found. If `<key>` is not in d, and the optional <default> argument is specified,
then that value is returned, and no exception is raised:

`locations.pop("Bengaluru")
locations.pop("something", False)`

### Popitem

popitem -> popitem() removes the last key-value pair added from d and returns it as a tuple 

`locations.popitem()`. If locations is empty, locations.popitem() raises a KeyError exception

### Update

update -> Merges a dictionary with another dictionary or with an iterable of key-value pairs. 
If <obj> is a dictionary, d.update(<obj>) merges the entries from <obj> into d.

`For each key in <obj>`

1. If the key is not present in d, the key-value pair from <obj> is added to d.
2. If the key is already present in d, the corresponding value in d for that key is updated to the value from <obj>.

`d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}`

`d1.update(d2)`

In this example, key 'b' already exists in d1, so its value is updated to 200, the value for that key from d2. However, there is no key 'd' in d1, so that
key-value pair is added from d2. <obj> may also be a sequence of key-value pairs, similar to when the `dict()` function is used to define a dictionary. 
For example, <obj> can be specified as a list of tuples

`d1 = {'a': 10, 'b': 20, 'c': 30}`

`d1.update([('b', 200), ('d', 400)])`

Or the values to merge can be specified as a list of keyword arguments

`d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update(b=200, d=400)`
