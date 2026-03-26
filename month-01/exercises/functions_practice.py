# Function 1: Temperature Checker
def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

# Function 2: Palindrome checker
def palindrome_checker(word):
    result = word == word[::-1]
    return result

# Function 3: Vower counter
def count_vowels(sentence):
    vowels = 0
    for x in sentence.lower():
        if x in ["a", "i", "u", "e", "o"]:
            vowels +=1
    return vowels

print("Please choose which fucntion you want to use.")
print("1. Celcius to Fahrenheit")
print("2. Check Palindrome")
print("3. Count Vowels")

choice = str(input("Enter 1, 2, or 3: "))

if choice == "1":
    celcius = float(input("Please input Celcius: "))
    print(f"So {celcius} degrees Celcius equal to {celcius_to_fahrenheit(celcius)} degrees Fahrenheit.")

elif choice == "2":
    word = str(input("Input your word here: "))
    print(f"Palindrome checker result: {palindrome_checker(word)}")

elif choice == "3":
    sentence = str(input("Input your sentence here: "))
    print(f"The number of vowels in this setence is: {count_vowels(sentence)}.")

else:
    print("Invalid choise")