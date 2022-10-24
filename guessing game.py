# Guessing Game

secret_word = "butterfly"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# Using WHILE loop to continue asking for secret word

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Hehe try again: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Oops, YOU LOSE!")
else:
    print("Fairs, you win!")