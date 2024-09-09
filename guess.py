import art
import  random

# Global Constants for the attempts per turn
PLAYER_ATTEMPTS_EASY = 10
PLAYER_ATTEMPTS_HARD = 5

def check_answer(user_guess, actual_answer):
    if user_guess > actual_answer:
        print("Too high.")
    elif user_guess < actual_answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {actual_answer}")

def set_game_difficulty():
    mode = input("Choose a difficulty. Type 'easy' or 'hard' : ").lower()
    if mode == "easy":
        return PLAYER_ATTEMPTS_EASY
    else:
        return PLAYER_ATTEMPTS_HARD

def guess_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    continue_guessing = True
    print("I'm thinking of a number between 1 and 100.")
    # Chosing a random number between 1 and 100
    answer = random.randint(1, 100)
    turns = set_game_difficulty()
    while continue_guessing:

        print(f"You have {turns} attempts remaining to guess the number")
        guess_number = int(input("Make a guess: "))
        check_answer(guess_number, answer)
        turns -= 1
        if turns < 0:
            continue_guessing = False
            print(f"The answer was {answer}")
        elif guess_number == answer:
            continue_guessing  = False

while input("Do you want to play a game of Guess The Number? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    guess_game()