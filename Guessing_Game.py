secret_word = "green"
guess = ""
guess_count = 0
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < 3:
        guess = input("Guess the word: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Sorry! Out of guesses!")
else:
    print("Well done!")