import random

random_integer = random.randint(1, 100)
# print(f"(Debug) Secret number is: {random_integer}") # Uncomment to test path validations easily

incorrect_guesses = 0

while True:
    guess = int(input("Guess a number from 1 to 100: "))
    if guess == random_integer:
        print("Correct!")
        break
    elif guess < random_integer:
        print("too low!")
        incorrect_guesses += 1
    else:
        print("too high!")
        incorrect_guesses += 1

total_attempts = incorrect_guesses + 1
pct_correct = (1 / total_attempts) * 100
pct_incorrect = (incorrect_guesses / total_attempts) * 100

print(f"Percentage of correct answers: {pct_correct:.1f}%")
print(f"Percentage of incorrect answers: {pct_incorrect:.1f}%")
