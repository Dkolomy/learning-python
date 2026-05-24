import random

print("Guess the number game")
guess = int(input("Enter a number between 1 and 100: "))
correct_number = random.randint(1, 100)
guess_count = 1

while guess != correct_number:
  guess_count += 1
  if guess < correct_number:
    print("Too low!")
  elif guess > correct_number:
    print("Too high!")
  guess = int(input("Enter a number between 1 and 100: "))

print(f"You guessed the correct number {correct_number} in {guess_count} guesses!")
