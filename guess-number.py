print("Hello! Welcome to my first number guessing game project.")
print("This is my first attempt at creating a game in Python. It's simple, but I'm excited to share it!")
print("I'm just starting out, and any feedback or suggestions you have are greatly appreciated!")

import random
print("Guess any number between 1 to 100")
num = random.randint(1,100)
guess = int(input("Enter your guess: "))
attempt = 1
while (num!=guess):
    if(guess>num):
        print("try lower number, ")
        guess = int(input("Enter your guess once again: "))
        attempt = attempt + 1
    else:
        print("try higher number, ")
        guess = int(input("Enter your guess: "))
        attempt = attempt + 1
print(f"\nCongratulations! You've guessed the right number in {attempt} attempts.")
print("Thank you for playing! Since I’m still learning, I would love to hear any thoughts or suggestions you have.")
print("Feel free to leave a suggestion or feedback (or just say hi!) :)")