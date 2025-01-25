import art
import random

def compare(attempt, number):
    print(f"You have {attempt} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess < number:
        print("Too Low.\nGuess Again.")
    elif guess > number:
        print("Too High.\nGuess Again.")
    else:
        print(f"You got it the answer was {number}.")
        attempt = 0
    return attempt

def number_guessing():
    print(art.logo2)
    print("Welcome to the number guessing game!\nI am thinking of a number between 1-100.")
    number = random.randint(1,100)
    difficulty = input("Choose a difficulty level. Type easy or hard.")
    attempt = 10
    if difficulty == "easy":
        while attempt != -1:
            output = compare(attempt, number)
            attempt = output - 1
    elif difficulty == "hard":
        attempt -= 5
        while attempt != -1:
            output = compare(attempt, number)
            attempt = output -1
    return

number_guessing()
