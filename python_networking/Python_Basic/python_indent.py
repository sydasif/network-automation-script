""" Indentation in python:
1. Indentation determines which code is inside the block
2. When a block starts and ends """
a = 10
b = 5

if a > b:
    print("A greater than B")  # This code indent under if block
    print("A - B:", a - b)  # This code indent under if block
else:
    print("B is greater than A")  # This code indent under else block

a = 10
b = 15

if a > b:
    print("A greater than B")  # This code indent under if block
    print("A - B:", a - b)  # This code indent under if block
else:
    print("B is greater than A")  # This code indent under else block
    print("A - B:", a - b)  # This code indent under else block

# Commit or blank line improve code readability
print("End")
