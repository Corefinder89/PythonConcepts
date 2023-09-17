# Namespaces and scopes in python

An **assignment statement** creates a **symbolic name** that you can use to reference an object. The statement x = 'foo' creates a symbolic name x that refers to the string object 'foo'.

In a program of any complexity, you’ll create hundreds or thousands of such names, each pointing to a specific object.

## Namespaces in python

A namespace is a collection of currently defined symbolic names along with information about the object that each name references. You can think of a namespace as a *dictionary* in which the keys are the object names and the values are the objects themselves. Each key-value pair maps a name to its corresponding object. In a Python program, there are four types of namespaces:

- Built-In
- Global
- Enclosing
- Local

These have differing lifetimes. As Python executes a program, it creates namespaces as necessary and deletes them when they’re no longer needed. Typically, many namespaces will exist at any given time.

## The Built-In namespace

The built-in namespace contains the names of all of Python’s built-in objects. These are available at all times when Python is running. You can list the objects in the built-in namespace using `dir(__builtins__)`

The Python interpreter creates the built-in namespace when it starts up. This namespace remains in existence until the interpreter terminates.

## The Global namespace

The **global namespace** contains any names defined at the level of the main program. Python creates the global namespace when the main program body starts, and it remains in existence until the interpreter terminates.

Strictly speaking, this may not be the only global namespace that exists. The interpreter also creates a global namespace for any **module** that your program loads with the import statement.

## The Local and Enclosing namespace

the interpreter creates a new namespace whenever a function executes. That namespace is local to the function and remains in existence until the function terminates.

```python
def f():
    print('Start f()')
    def g():
        print('Start g()')
        print('End g()')
        return

    g()
    print('End f()')
    return

f()
```

In this example, function g() is defined within the body of f(). Here’s what’s happening in this code:

- Lines 1 to 12 define f(), the enclosing function.
- Lines 4 to 7 define g(), the enclosed function.
- On line 15, the main program calls f().
- On line 9, f() calls g().

When the main program calls f(), Python creates a new namespace for f(). Similarly, when f() calls g(), g() gets its own separate namespace. The namespace created for g() is the **local namespace**, and the namespace created for f() is the **enclosing namespace**.

Each of these namespaces remains in existence until its respective function terminates. Python might not immediately reclaim the memory allocated for those namespaces when their functions terminate, but all references to the objects they contain cease to be valid.

## Variable scope

The existence of multiple, distinct namespaces means several different instances of a particular name can exist simultaneously while a Python program runs. As long as each instance is in a different namespace, they’re all maintained separately and won’t interfere with one another.

But that raises a question: Suppose you refer to the name x in your code, and x exists in several namespaces. How does Python know which one you mean?

The answer lies in the concept of **scope**. The scope of a name is the region of a program in which that name has meaning. The interpreter determines this at runtime based on where the name definition occurs and where in the code the name is referenced.

## Order

If your code refers to the name x, then Python searches for x in the following namespaces in the order shown:

- Local: If you refer to x inside a function, then the interpreter first searches for it in the innermost scope that’s local to that function.
- Enclosing: If x isn’t in the local scope but appears in a function that resides inside another function, then the interpreter searches in the enclosing function’s scope.
- Global: If neither of the above searches is fruitful, then the interpreter looks in the global scope next.
- Built-in: If it can’t find x anywhere else, then the interpreter tries the built-in scope.

This is the LEGB rule as it’s commonly called in Python literature (although the term doesn’t actually appear in the Python documentation). The interpreter searches for a name from the inside out, looking in the local, enclosing, global, and finally the built-in scope. If the interpreter doesn’t find the name in any of these locations, then Python raises a NameError exception.

### Example 1: Single definition

In the first example, x is defined in only one location. It’s outside both f() and g(), so it resides in the global scope

```python
x = 'global'

def f():
    def g():
        print(x)
    g()

f()
```

### Example 2: Double definition

In the next example, the definition of x appears in two places, one outside f() and one inside f() but outside g()

```python
x = 'global'

def f():
    x = 'enclosing'

    def g():
        print(x)

    g()


f()
```

As in the previous example, g() refers to x. But this time, it has two definitions to choose from:

- Line 1 defines x in the global scope.
- Line 4 defines x again in the enclosing scope.

According to the LEGB rule, the interpreter finds the value from the enclosing scope before looking in the global scope. So the print() statement on line 7 displays 'enclosing' instead of 'global'.

### Example 3: Triple definition

Next is a situation in which x is defined here, there, and everywhere. One definition is outside f(), another one is inside f() but outside g(), and a third is inside g().

```python
x = 'global'

def f():
    x = 'enclosing'

    def g():
        x = 'local'
        print(x)

    g()

f()
```

Now the print() statement on line 8 has to distinguish between three different possibilities:

- Line 1 defines x in the global scope.
- Line 4 defines x again in the enclosing scope.
- Line 7 defines x a third time in the scope that’s local to g().

Here, the LEGB rule dictates that g() sees its own locally defined value of x first. So the print() statement displays 'local'.

## The globals() function

The built-in function `globals()` returns a reference to the current global namespace dictionary. You can use it to access the objects in the global namespace.

When you define a variable in the global scope

```python
x = 'foo'

globals()
```

After the assignment statement x = 'foo', a new item appears in the global namespace dictionary. The dictionary key is the object’s name, x, and the dictionary value is the object’s value, 'foo'.

You would typically access this object in the usual way, by referring to its symbolic name, x. But you can also access it indirectly through the global namespace dictionary.

```python
x

globals()['x']

x is globals()['x']
```

You can create and modify entries in the global namespace using the globals() function as well.

```python
globals()['y'] = 100

globals()

y

globals()['y'] = 3.14159

y
```

## The locals() function

Python also provides a corresponding built-in function called locals(). It’s similar to globals() but accesses objects in the local namespace instead.

```python
def f(x, y):
    s = 'foo'
    print(locals())


f(10, 0.5)
```

When called within f(), locals() returns a dictionary representing the function’s local namespace. Notice that, in addition to the locally defined variable s, the local namespace includes the function parameters x and y since these are local to f() as well.

If you call locals() outside a function in the main program, then it behaves the same as globals().

## Deep dive: A subtle difference between globals() and locals()

**globals()** returns an actual reference to the dictionary that contains the global namespace. That means if you call globals(), save the return value, and subsequently define additional variables, then those new variables will show up in the dictionary that the saved return value points to.

```python
g = globals()
g

x = 'foo'
y = 29
g
```

**locals()**, on the other hand, returns a dictionary that is a current copy of the local namespace, not a reference to it. Further additions to the local namespace won’t affect a previous return value from locals() until you call it again. Also, you can’t modify objects in the actual local namespace using the return value from locals().

```python
def f():
    s = 'foo'
    loc = locals()
    print(loc)

    x = 20
    print(loc)

    loc['s'] = 'bar'
    print(s)


f()
```

## The nonlocal declaration

The nonlocal declaration allows a function to access and modify object in the enclosing scope.

```python
def f():
    x = 20

    def g():
        nonlocal x
        x = 40

    g()
    print(x)


f()
```

To modify x in the enclosing scope from inside g(), you need the analogous keyword nonlocal. Names specified after the nonlocal keyword refer to variables in the nearest enclosing scope

After the nonlocal x statement on line 242, when g() refers to x, it refers to the x in the nearest enclosing scope, whose definition is in f() on line 239.

The print() statement at the end of f() on line 246 confirms that the call to g() has changed the value of x in the enclosing scope to 40.
