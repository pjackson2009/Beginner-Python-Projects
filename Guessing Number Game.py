
import random
lower_limit = random.randint(-10, -1)
upper_limit = random.randint(lower_limit + 2, 10)

secret_number = random.randint(lower_limit, upper_limit)

guesses_made = 0
guess_limit = int((upper_limit - lower_limit) / 3)

print(f"I'm thinking of an integer between {lower_limit} and {upper_limit}. You have {guess_limit} guesses.")
while guesses_made < guess_limit:
    guess = input("Guess the number: ")
    if guess.lstrip("-").isdigit():
        guess = int(guess)
        if lower_limit <= guess <= upper_limit:
            guesses_made += 1
            if guess < secret_number and guess_limit - guesses_made > 0:
                print(f"The number is higher than {guess}.")
                print(f"You have {guess_limit - guesses_made} guess(es) left.")
            elif guess > secret_number and guess_limit - guesses_made > 0:
                print(f"The number is lower than {guess}.")
                print(f"You have {guess_limit - guesses_made} guess(es) left.")
            elif guess == secret_number:
                print(f"Correct! The number was {secret_number}. You guessed in {guesses_made} guesses.")
                break
        else:
            print(f"That guess is not in range. Please enter a number between {lower_limit} and {upper_limit}")
            print(f"You have {guess_limit - guesses_made} guess(es) left.")
    else:
        print(f"Please enter a digit between {lower_limit} and {upper_limit}.")
        print(f"You have {guess_limit - guesses_made} guess(es) left.")
else:
    print(f"Unlucky, you failed to guess {secret_number} as the number!")