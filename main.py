import random

word_guess = ["huytonquadeptrai",'apple','banana','template']

chosen_word = random.choice(word_guess)
lives = 6
print(chosen_word)

blank = ""
for x in range(len(chosen_word)):
    blank += '_'
print(f"Your word to guess is: {blank}")

game_over = False
correct_word = []

while not game_over:
    print(f"You have {lives}/6 left")
    guess = input("Guess a word please: ").lower()

    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_word.append(guess)
        elif letter in correct_word:
            display += letter
        else:
            display += "_"

    print(f"Word to guess is: {display}")

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True
            print("Bruh you losed dumb ass")

    if "_" not in display:
        game_over = True
        print(f"God damn! you won and the word actually is {display}")
