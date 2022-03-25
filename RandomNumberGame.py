import random

print("Number Guessing Game")

Diffculty = input("Please select the diffculty( easy, meduim, hard):")

if Diffculty = "easy":
    lives = 8

elif Diffculty = "meduim":
    lives = 5

elif Diffculty = "hard":
    lives = 3

else:
    print("invalid input please select a givin diffculty")

number = random.randint(1, 9)

chances = 0

print("Guess a number, between 1 and 9:")

while chances < lives:
    
    guess = int(input("Enter your guess: "))

    if guess == number: 
        print("Congratulation You Win")
        break

    elif guess < number: 
        print("your guess was to low, select a number greater than",guess)

    else:
        print("your guess was to high, select a number lower than",guess)
    
    chances += 1
    
if not chances > lives:
    print("You lose, you will get it next time. The number was",number)

int(input("Game Over"))
