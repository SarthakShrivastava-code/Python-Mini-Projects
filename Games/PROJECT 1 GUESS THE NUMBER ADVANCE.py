import random

def play_game():
    target = random.randint(1, 100)
    attempts = 0
    print("\n🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100... Can you guess it?")
    print("Type 'Quit' anytime to give up.\n")

    while True:
        user_input = input("🔢 Your guess: ")

        if user_input.lower() == "quit":
            print(f"\n😢 You gave up! The number was {target}.")
            break

        if not user_input.isdigit():
            print("⚠️ Please enter a valid number (or type 'Quit' to exit).")
            continue

        user_guess = int(user_input)
        attempts += 1

        if user_guess == target:
            print(f"\n🎉 Success! You guessed it in {attempts} {'try' if attempts == 1 else 'tries'}!")
            if attempts <= 3:
                print("🌟 You're a mind reader!")
            elif attempts <= 7:
                print("👍 Great job!")
            else:
                print("😅 That took a while, but you did it!")
            break
        elif user_guess < target:
            print("📉 Too low! Aim higher ⬆️")
        else:
            print("📈 Too high! Aim lower ⬇️")

    print("\n🎲 _____Game over_____ 🎲")

while True:
    play_game()
    again = input("\n🔁 Wanna play again? (yes/no): ").lower()
    if again != "yes":
        print("👋 Thanks for playing! See you next time!")
        break