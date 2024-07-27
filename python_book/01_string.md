# Strings

Strings — a sequence of characters enclosed by quotes — are arguably the most well-known data type in all programming
languages.

> In Python 2 strings are ASCII characters and in Python 3 strings are Unicode characters (by default UTF-8), so if you
> receive bytes you will need to encode them to use string methods, using one of the available encode types, such as
> UTF-8, UTF-16, ASCII, or others.

Let’s examine what else you need to know when starting to use strings. First, you’ll define two new variables that are
both strings, `final` and `ipaddr`:

````py
final = 'The IP address of router1 is: '
ipaddr = '192.0.2.1'
````

You can use the built-in function called type to verify the data type of any given object in Python:

````pycon
>>> type(final)
<class 'str'>
````

This is how you can easily check the type of one object, which is often helpful in troubleshooting code, especially if
the code you didn’t write. Next, let’s look at how to combine, add, or concatenate strings:

````pycon
>>> final + ipaddr
'The IP address of router1 is: 192.0.2.1'
````

So far, you’ve created two new variables: ``final`` and ``ipaddr``. Each is a string, after both are created, you
concatenate them using the ``+`` operator, and finally print them out. The same could be done even if ``final`` is not a
predefined object:

````pycon
>>> print('The IP address of router1 is: ' + ipaddr)
>>> The IP address of router1 is: 192.0.2.1
````

## Using built-in methods of strings

To view the available built-in methods for strings, you use the built-in ``dir()`` function while in the Python shell.
You
first create any variable that is a string or use the formal data type name of str and pass it as an argument
to ``dir()``
to view the available methods.

````pycon
>>> dir(str)
# output has been omitted
['__add__', '__class__', '__contains__', '__delattr__', '__doc__',
'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha',
'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'lower',
'lstrip', 'replace', 'rstrip', 'split', 'splitlines', 'startswith',
'strip', 'upper']
````

It’s possible to also pass any string to the ``dir()`` function to produce the same output as previously. For example,
if you define a variable such as ``hostname = 'ROUTER'``, ``hostname`` can be passed to ``dir()`` — that
is, ``dir(hostname)`` — producing the same output as ``dir(str)`` to determine what methods are available for strings.

### Navigate the Code with type(), dir(), and help()

To learn how to use a given method that you see in the output of ``dir()``, you can use the built-in
function ``help()``. To use
this built-in help feature, you pass in the object (or variable) and the given method. The following example shows how
you can use ``help()`` to learn how to use the upper method:

````pycon
>>> help(hostname.upper)
Help on built-in function upper:

upper() method of builtins.str instance
    Return a copy of the string converted to uppercase.
(END)
````

When you’re finished, press ``Q`` to quit viewing the built-in help. At this point, we have already introduced the three
functions that will help you gain more understanding of your code. Here is our recommended flow:

1. Check your data type by using ``type()``.
2. Check the available methods for your object by using ``dir()``.
3. After knowing which method you want to use, learn how to use it by using ``help()``.
