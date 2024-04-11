import random

def guessing_game():
    print("guess a number")
    secret_number = random.randint(1, 1000)
    attempts = 0

    while True:
        guess = int(input("enter guess between 1 and 1000"))
        attempts += 1

        if guess < secret_number:
            print("too low:( try again")
        elif guess > secret_number:
            print("too high:( try again")
        else:
            print(f"congratulations!!! you guessed the number in {attempts} attempts!")
            break

guessing_game()
