num1 = int(input("Please input the first number here: "))
num2 = int(input("Please input the second number here: "))

# print(f"Sum: {num1 + num2}")
# print(f"Subtraction: {num1 - num2}")
# print(f"Multiplication: {num1 * num2}")
# print(f"Division: {num1 / num2}")
# print(f"Remainder: {num1 % num2}")
# print(f"Power: {num1 ** num2}")
# print(f"Floor Division: {num1 // num2}")

# print(-7 // 2)   # what do you expect?

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multi(a, b):
    return a * b

def division(a, b):
    return a / b

def mod(a, b):
    return a % b

def div(a, b):
    return a // b

def power(a, b):
    return a ** b

print(f"Sum: {add(num1, num2)}")
print(f"Subtraction: {subtract(num1, num2)}")
print(f"Multiplication: {multi(num1, num2)}")
print(f"Division: {division(num1, num2)}")
print(f"Remainder: {mod(num1, num2)}")
print(f"Power: {power(num1, num2)}")
print(f"Floor Division: {div(num1, num2)}")