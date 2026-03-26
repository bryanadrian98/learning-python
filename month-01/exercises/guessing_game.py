secret = 42
attempts = 0

while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess < 42:
        print(f"Please guess higher, number of attempts: {attempts}")
    elif guess > 42:
        print(f"Please guess lower, number of attempts: {attempts}")
    else:
        print(f"You guessed the right number! with {attempts} attempts.")
        break