# def = define a function
# calculate_area = the function name
# radius = parameter (input the function expects)

phi = 3.14159

def calculate_area(radius):
    area = phi * radius ** 2
    return area
    # return area # sens the result back to whoever called it

# Calling the function
result = calculate_area(5)
print(result)

# Or directly
print(calculate_area(10))

print("STEP 3")

def add_numbers(a, b):
    print(a + b) # version 1: prints but returns nothing

def add_numbers_v2(a, b):
    return a + b # version 2: returns the result

# Try to use the result
result1 = add_numbers(3, 4)
result2 = add_numbers_v2(3, 4)

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")


print("STEP 4")
def my_function():
    secret = "I only exist inside this function"
    print(secret)

# my_function()
# print(secret)

name = "Bryan"

def greet():
    print(f"Hello {name}")

greet()