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

def floor_division(a, b):
    return a // b

def power(a, b):
    return a ** b

num1 = int(input("Please input the first number here: "))
num2 = int(input("Please input the second number here: "))

print(f"Sum: {add(num1, num2)}")
print(f"Subtraction: {subtract(num1, num2)}")
print(f"Multiplication: {multi(num1, num2)}")
print(f"Division: {division(num1, num2)}")
print(f"Remainder: {mod(num1, num2)}")
print(f"Power: {power(num1, num2)}")
print(f"Floor Division: {floor_division(num1, num2)}")