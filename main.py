import art 
import random


print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

choosed_number = random.randint(1,101)

easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ")

attempts = 0

if easy_or_hard == "easy":
  attempts = 10
else:
  attempts = 5

print(attempts)

print(f"You have {attempts} attempts remaining to guess the number.")

flag = True

def show(attempts):
  if attempts == 0:
    print("You've run out of guesses.You lose.")
  else:
    print(f"You have {attempts} to guess the number.")

while flag:
  if attempts == 0:
    break
  guessed_number = int(input("Make a guess: "))
  if guessed_number > choosed_number:
    print("Too High.")
    print("Guess again.")
    attempts -= 1
    show(attempts)
  elif guessed_number < choosed_number:
    print("Too low.")
    print("Guess again.")
    attempts -= 1
    show(attempts)
  else:
    print(f"You got it. The answer was {guessed_number}")
    flag = False
  
  
  