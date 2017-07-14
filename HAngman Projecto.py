import numpy

def hangman_game():
    word_list = ['genius', 'orphanage', 'torched', 'tree', 'pizza'] # The word list
    word = numpy.random.choice(word_list) # Randomly chooses a word from the word list
    guess_letter = "" # The variable that stores the player's input
    space = "_ " * len(word) # Represents the amount of spaces in the word
    print space
    stage = 0
    while stage <= 6:
        while guess_letter == "": # Makes it so you have to input a letter
            guess_letter = raw_input("Enter a letter please:")
        l_list = guess_letter[0] # The list that stores the letters guessed
        for letter in word: # This for for loop checks if the guessed letter is in the word and then replaces the corresponding space
            if guess_letter[0] == word[0]:
                print guess_letter[0] + space[1:]
                print 'Good job! You have guessed:' + guess_letter[0]
            break

        else: # Prints the gallows with the partially created hanging man
            print "  |------|"
            print "  |      0"
            print "  |"
            print "  |"
            print "  |"
            print "  |"
            print "  |--------------|"
            print "  |              |"
            print "Good guess! Try again!"
            print "You have guessed:" + l_list



intro = ""
while intro == "":
    intro = raw_input('Would you like to play hangman? y or n:')
if intro == 'y':
     hangman_game()
