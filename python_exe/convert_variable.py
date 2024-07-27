"""The different conversion functions for the basic data types are outlined here:
• str() to convert to strings
• int() to convert to integers
• bool() to convert to a Boolean—for example, bool(0) will convert to False while bool(1) converts to True
• float() to convert to a floating-point number """

# user input 
my_age = input("What's your age?: ")
# convert the input from a string to an integer
age_as_num = int(my_age)
# now add 10 to it
age_as_num = age_as_num + 10
# lastly, convert variable into string and print
age_as_text = str(age_as_num)
print("Your age + 10 is " + age_as_text)
# print using f-string syntax
print(f"Your age + 10 is {age_as_text}")
