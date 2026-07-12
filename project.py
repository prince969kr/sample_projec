# number guessing game


print("====NUMBER GUESSING GAME====")

import random

number = random.randint(1,100)

while True:
  Guess = int(input("Enter your guessing nummber:"))

  if Guess < number:
    print("Your guessing number is too small.")
  elif Guess > number:
    print("Your guessing nummber is too high.")
  else :
    print("🎉 YAY! Your geuss is right.\n You won the game.")
