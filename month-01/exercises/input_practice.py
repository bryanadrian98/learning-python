 # input() always returns a STRING
name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

# This will crash - run it and read the error
age = 2026 - birth_year
print(f"You are {age} years old.")

print(f"In 2031, you will be {2031 - int(birth_year)} years old.")

# Before it was error because the birth_year is not an integer (a string) and you cannot do mathematical operations with string