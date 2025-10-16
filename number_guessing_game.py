import random
import time

def intro():
    print("===================================")
    print("     🎯 NUMBER GUESSING GAME 🎯")
    print("===================================")
    print("Welcome! Try to guess the number I'm thinking of.")
    print("You can choose a difficulty level.")
    print()

def choose_level():
    print("Select difficulty level:")
    print("1. Easy (1–10)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")
    print()

    while True:
        level = input("Enter your choice (1/2/3): ")
        if level in ["1", "2", "3"]:
            return int(level)
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")

def set_range(level):
    if level == 1:
        return 1, 10
    elif level == 2:
        return 1, 50
    else:
        return 1, 100

def play_game(start, end):
    number = random.randint(start, end)
    attempts = 0
    print(f"\nI'm thinking of a number between {start} and {end}...")
    time.sleep(1)

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

def play_again():
    while True:
        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        else:
            print("Please type 'y' or 'n'.")

def main():
    intro()
    while True:
        level = choose_level()
        start, end = set_range(level)
        play_game(start, end)
        if not play_again():
            print("\nThanks for playing! Goodbye 👋")
            break
        print("\nRestarting the game...\n")
        time.sleep(1)

if __name__ == "__main__":
    main()
