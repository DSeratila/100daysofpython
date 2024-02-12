import random
import hangman_stages
import hangman_words

print(hangman_stages.logo)
lives_left = len(hangman_stages.stages)

chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)

display = list(('_' * len(chosen_word)))

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:\n ").lower()

    if guess in display:
        print("You've already got this one. Choose smth else")
        continue

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        if lives_left > 1:
            print("The letter is not in the world, you've guessed it wrong. You've lost 1 life")
        lives_left -= 1
        print(hangman_stages.stages[lives_left])
        if lives_left == 0:
            end_of_game = True
            print("You Lose")

    print(''.join(display))

    if "_" not in display:
        end_of_game = True
        print("You won!")
