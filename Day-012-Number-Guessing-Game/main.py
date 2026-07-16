import random

def select_number():
    return random.randint(1, 100)

def check_guess(submitted_guess, number):
    if submitted_guess == number:
        return "You guessed it! Congratulations!", True
    elif submitted_guess < number:
        return "Too low!", False
    else:
        return "Too high!", False

DIFFICULTY_OPTIONS = {
    "easy": 10,
    "hard": 5,
}

number_to_guess = select_number()

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
guesses = DIFFICULTY_OPTIONS[difficulty]
guessed = False

while guesses > 0 and not guessed:
    guess = int(input("Make a guess: "))
    message, guessed = check_guess(guess, number_to_guess)
    print(message)
    if not guessed:
        guesses -= 1
        if guesses == 1:
            print("Guess again.\nYou have 1 guess left.")
        else:
            print(f"Guess again.\nYou have {guesses} guesses left.")
if not guessed:
    print(f"You ran out of guesses. The number was {number_to_guess}.")

