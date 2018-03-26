from random import *

attempts = 0

score = randint(1, 50)
tries = 1
win = True

name = input("Hello, What is your player name?")
print("Hello", name + ".",)

question = input("Would you like to play a game? [y/n] ")
if question == "n":
    print("Good Bye! {S Good Bye -AOL")

if question == "y":
    print("I'm thinking of a score between 1 & 50")
    isCorrect = False
    guess = int(input("Take a guess: "))

while score != guess and attempts < 6:

        if guess < score:
            print("Higher!! Think Think!")
        elif guess > score:
            print("Lower! Think think!")
        guess = int(input("Take a guess: "))
        attempts += 1

if attempts == 6:
        print("\nSorry you reached the maximum number of tries")
        print("The secret number was ", score)

else:
            print("\nYou guessed it! The number was ", score)
            print("You guessed it in ", attempts, "attempts")
