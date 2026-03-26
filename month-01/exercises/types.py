 
# Integer - whole numbers
age = 27
print(type(age))

# Float - number with decimals
height = 1.75
print(type(height))

# String - text, always in quotes
name = "Bryan"
print(type(name))

# Boolean - only True or False (capital T and F)
is_employed = True
print(type(is_employed))

# Convert string to integer
user_input = "25"
converted = int(user_input)
print(type(user_input)) # still a string
print(f"This is a string {type(user_input)}.")
print(type(converted)) # now an integer
print (f"This is an integer {type(converted)}.")

# What happens when conversion failes?
broken = int("hello")

# The broken variable fails because it cannot convert a string to an integer since it is not a number