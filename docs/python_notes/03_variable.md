## Introduction to Variables

**Variables** are a fundamental concept in programming, serving as containers
to store data that can be used and manipulated throughout a program. They are
used in every programming language and are essential for handling data in
applications.

### Key Characteristics of Variables:

- **Storage**: Variables store data temporarily in memory, allowing the program
  to access and manipulate it as needed.
- **Dynamic Typing in Python**: Python variables are *dynamically typed*,
  meaning that you don't need to declare the type of a variable when you create
  it. The type is inferred based on the value assigned to it.

### Example of Variables in Python:

```python
name = "John"
# Output: 'John'

number = 10
# Output: 10

# Checking the memory address of variables
id(name)
# Output: 1759753155568

id(number)
# Output: 140720682367704
```

In this example:

- `name` stores a string value `"John"`.
- `number` stores an integer value `10`.
- `id()` function returns the memory address where the variable is stored.

### Updating Variables:

Variables in Python can be reassigned new values, and each time this happens,
the variable points to a new memory address:

```python
name = "Ali"
id(name)
# Output: 1759753175616
```

Here, the variable `name` is updated from `"John"` to `"Ali"`, resulting in a
change in its memory address, as Python creates a new object for the updated
value.

Variables are crucial for storing and manipulating data in programs. Python’s
dynamic typing and ease of use make handling variables straightforward,
allowing for quick development and flexibility.