
if __name__ == "__main__":

    #First thing printed when we start the game
    print('Player 2 look away')

    #gets user to input a word and its saves as guessing word.
    guessing_word = input('Type a word,then press enter,then ctrl+l ')

    # creating an empty list
    player_2_word = []

    # adding an underscore to the empty list for letter there is
    for letter in guessing_word:
        player_2_word.append ('_')

    print(' '.join(player_2_word))


    # setting a counter of incorrect guesses
    incorrect_guesses = 0

    game_won = False

    while incorrect_guesses <= 10 and game_won == False:


       # asking the user to guess a letter
        guess_letter = input('guess a letter ')

        if guess_letter in guessing_word:
            print('correct' )

            #finds the position of the guess letter in the word
            letter_position = guessing_word.index(guess_letter)

            # change the underscore to the guess letter in the right poition.
            player_2_word[letter_position] = guess_letter
            print(' '.join(player_2_word))

            # check to see if player 2 has won, and can exit while loop
            if guessing_word == ''.join(player_2_word):


              game_won = True
        else:
            print ('incorrect')
            incorrect_guesses += 1

    if incorrect_guesses == 11:
      print('player 1 has won')

    if game_won == True:
      print('player 2 has won')
