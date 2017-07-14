import numpy

def hangman_game():
    word_list = ['genius', 'orphanage', 'torched', 'tree', 'pizza'] # The word list
    word = numpy.random.choice(word_list) # Randomly chooses a word from the word list
    word_len=[]
    n=-1

    for letter in word:
        word_len.append("_" )# Represents the amount of spaces in the word
    stage = 0
    def hangman_stage(stage):
        if stage ==0:
            print "  |------|"
            print "  |       "
            print "  |"
            print "  |"
            print "  |"
            print "  |"
            print "  |--------------|"
            print "  |              |"
            print "Good guess! Try again!"
            print "You have guessed:" + l_list
        elif stage == 1:
            print "  |------|"
            print "  |      O"
            print "  |"
            print "  |"
            print "  |"
            print "  |"
            print "  |--------------|"
            print "  |              |"
            print "Good guess! Try again!"
            print "You have guessed:" + l_list
        elif stage ==2:
            print "  |------|"
            print "  |      O"
            print "  |      |"
            print "  |"
            print "  |"
            print "  |"
            print "  |--------------|"
            print "  |              |"
            print "Good guess! Try again!"
            print "You have guessed:" + l_list
        elif stage == 3:
            print "  |------|"
            print "  |      O"
            print "  |     _|"
            print "  |"
            print "  |"
            print "  |"
            print "  |--------------|"
            print "  |              |"
            print "Good guess! Try again!"
            print "You have guessed:" + l_list
        elif stage == 4:
            print "  |------|"
            print "  |      O"
            print "  |     _|_"
            print "  |"
            print "  |"
            print "  |"
            print "  |--------------|"
            print "  |              |"
            print "Good guess! Try again!"
            print "You have guessed:" + l_list
        elif stage == 5:
            print "  |------|"
            print "  |      O"
            print "  |     _|_"
            print "  |      |"
            print "  |"
            print "  |"
            print "  |--------------|"
            print "  |              |"
            print "Good guess! Try again!"
            print "You have guessed:" + l_list
        elif stage == 6:
            print "  |------|"
            print "  |      O"
            print "  |     _|_"
            print "  |      |"
            print "  |     /"
            print "  |"
            print "  |--------------|"
            print "  |              |"
            print "Good guess! Try again!"
            print "You have guessed:" + l_list
        elif stage == 7:
            print "  |------|"
            print "  |      O"
            print "  |     _|_"
            print "  |      |"
            print "  |     / \\"
            print "  |"
            print "  |--------------|"
            print "  |              |"
            game = ''
            while game == "":
                game = raw_input('Would you like to play hangman? y or n:')
            if game == 'y':
                hangman_game()

    print word_len
    while stage < 7:
        guess_letter = ""
        while guess_letter == "": # Makes it so you have to input a letter
            guess_letter = raw_input("Enter a letter please:")
        l_list = guess_letter[0] # The list that stores the letters guessed
        for l in word: # This for loop checks if the guessed letter is in the word and then replaces the corresponding space
            if guess_letter[0] in word:
                word_len[n]=guess_letter
                print word_len
                print 'Good job! You have guessed:' + l_list
                break
            else:
                print "  |------|"
                print "  |      O"
                print "  |"
                print "  |"
                print "  |"
                print "  |"
                print "  |--------------|"
                print "  |              |"
                print "Good guess! Try again!"
                print "You have guessed:" + l_list
                stage=+1
                break
        l_list = l_list + guess_letter

intro = ""
while intro == "":
    intro = raw_input('Would you like to play hangman? y or n:')
if intro == 'y':
     hangman_game()
