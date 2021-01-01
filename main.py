from art import logo

print(logo)

# Generate a random number.
import random

selected_number = random.randint(1, 101)

end_of_game = False
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Select the difficulty level.
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Allot the number of guesses in accordance to the difficulty level.
if difficulty == "easy":
    guesses = 10
else:
    guesses = 5

# Continue the game until end_of_game == True.
while not end_of_game:
    # Update the user (after each guess) how many number of guesses they have.
    print(f"You have {guesses} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))

    # If user guessed right, end the game.
    if guessed_number == selected_number:
        end_of_game = True
        print(f"You got it! The answer was {selected_number}.")

    # If user guessed a number higher than the selected number.
    elif guessed_number > selected_number:
        guesses -= 1
        print("Too high.")

    # If user guessed a number lower than the selected number.
    else:
        guesses -= 1
        print("Too low.")

    # If the game hasn't ended yet.
    if not end_of_game:
        # If user can still guess, ask them to guess again.
        if guesses != 0:
            print("Guess again.")
        # If user ran out of guesses, end the game.
        else:
            end_of_game = True
            print(f"Oops! You ran out of guesses 😬\nThe answer was: {selected_number}")
