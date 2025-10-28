import random

def play_game():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You guessed the number in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    main()
