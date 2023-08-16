import random
if __name__ == "__main__":
    while True:
        mode_type = input('do you want 1 player yes/no ')
        if mode_type == "yes":
            word_list = ['sunday', 'train', 'armidilo', 'tree', 'pencil']

    # pick a random element from a list of strings.
            guessing_word = random.choice(word_list)
            break
        elif mode_type == "no":
            # First thing printed when we start the game
            print('Player 2 look away')

            # gets user to input a word and its saves as guess ing word.
            guessing_word = input('Type a word,then press enter,then ctrl+l ')
            guessing_word = guessing_word.lower()
            break
        else:
            print("wrong word please input yes or no")


    # creating an empty list
    player_2_word = []

    # adding an underscore to the empty list for letter there is
    for letter in guessing_word:
        player_2_word.append('_')

    print(' '.join(player_2_word))

    # setting a counter of incorrect guesses
    incorrect_guesses = 0

    game_won = False

    while incorrect_guesses <= 10 and game_won == False:

        # asking the user to guess a letter
        guess_letter = input('guess a letter ')

        if guess_letter in guessing_word:
            print('correct')

            letter_position = 0

            for letter in guessing_word:

                if letter == guess_letter:
                    # change the underscore to the guess letter in the right poition.
                    player_2_word[letter_position] = guess_letter

                letter_position += 1

            print(' '.join(player_2_word))

            # check to see if player 2 has won, and can exit while loop
            if guessing_word == ''.join(player_2_word):
                game_won = True
        else:
            print('incorrect')
            incorrect_guesses += 1

    if incorrect_guesses == 11 and mode_type == "no":
        print('player 1 has won')

    if incorrect_guesses == 11 and mode_type == "yes":
        print('you have lost try again')

    if game_won == True and mode_type == "no":
        print('player 2 has won')

    if game_won == True and mode_type == "yes":
        print('You won')
