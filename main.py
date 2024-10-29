import random
import time

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
attempts = 0
guess_attempts = 0
start_time = 0
end_time = 0
elapsed_time = 0

guess_number = random.randint(1, 100)

dificult =  input("Choose a difficulty. Type 'easy','medium' or 'hard': ").lower()
print(dificult)


if dificult == "easy":
    attempts = 10
elif dificult == "medium":
        attempts = 5
elif dificult == "hard":
        attempts = 3
else:
    print("Invalid input.")
    exit()
print(f"You have {attempts} attempts.")
start_time = time.time()

while attempts > 0:
    choose_number = int(input("Choose a number between 1 and 100: "))
    
    print(start_time)
    if choose_number == guess_number:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"You got it! The answer was {guess_number}, you found it in {guess_attempts} attempts. The elapsed time was {elapsed_time:.2f} seconds.")
        exit()
    elif choose_number > guess_number:
        print("Too high.")
        attempts-=1
        guess_attempts += 1
        print(f"You have {attempts} attempts.")
    else:
        print("Too low.")
        attempts-=1
        guess_attempts += 1
        print(f"You have {attempts} attempts.")
        



