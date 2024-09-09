import art
import  random


def guess_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    player_attempts_easy = 10
    player_attempts_hard = 5
    continue_guessing = True
    difficulty_mode = input(
        "I'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard' : ").lower()
    number_picked = random.randint(1, 100)
    if difficulty_mode == "easy":
        while continue_guessing:
            print(f"You have {player_attempts_easy} attempts remaining to guess the number")
            guess_number = int(input("Make a guess: "))
            if guess_number < number_picked:
                print("Too low.")
                print("Guess again.")
                player_attempts_easy -= 1
            elif guess_number > number_picked:
                print("Too high.")
                print("Guess again.")
                player_attempts_easy -= 1
            elif guess_number == number_picked:
                print(f"You got it! The answer was {number_picked}")
                continue_guessing = False
            if player_attempts_easy <= 0:
                print("You've run out of guesses, you lose")
                print(f"The answer was {number_picked}")
                continue_guessing = False
    if difficulty_mode == "hard":
        while continue_guessing:
            print(f"You have {player_attempts_hard} attempts remaining to guess the number")
            guess_number = int(input("Make a guess: "))
            if guess_number < number_picked:
                print("Too low.")
                print("Guess again.")
                player_attempts_hard -= 1
            elif guess_number > number_picked:
                print("Too high.")
                print("Guess again.")
                player_attempts_hard -= 1
            elif guess_number == number_picked:
                print(f"You got it! The answer was {number_picked}")
                continue_guessing = False
            if player_attempts_hard <= 0:
                print("You've run out of guesses, you lose")
                print(f"The answer was {number_picked}")
                continue_guessing = False

while input("Do you want to play a game of Guess The Number? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    guess_game()