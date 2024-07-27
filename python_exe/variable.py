# variable called my_hostname and assign it a value(string)
my_hostname = "router01"

# using single quotes to assign a string
my_domain = 'example.com'

# use trippe quotes to define a string with multiple lines
my_motd = """
This is banner that will contain linebreaks and could be
the motd of a router
"""

# to print a variable, we can use print() function
print(my_hostname)
print(my_domain)
print(my_motd)

# similar to strings, we can also use numeric values.
# floats for floating-point and integers for whole numbers.
my_port = 22
my_throughput = 1.75
print(my_port)
print(my_throughput)

# True & False in python are represented truth values(boolean)
knows_python = True
knows_python = False
print(knows_python)

# define a variable's create an empty list 
l = []

# add variables to the end of this list using append() function
l.append(my_hostname)
l.append(my_domain)
l.append(my_port)
l.append(my_throughput)

""""
access elements in our list using the index. Be aware that indexes start at zero, so the first element in the list will be at index 0. Lists preserve the order in which items are added. Let's print out this information:
"""
print("The hostname stored in the list is: ")
print(l[0])
print("The domain stored in the list is: ")
print(l[1])
print("The port stored in the list is: ")
print(l[2])
