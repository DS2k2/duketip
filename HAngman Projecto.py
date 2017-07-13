import numpy
guess_letter = ""
while guess_letter == "":
    guess_letter = raw_input("Enter a letter please:")
word_list = ['genius', 'orphanage', 'torched', 'ga tech', 'tree']
word = numpy.random.choice(word_list)
if guess_letter[0] == word[0]:
    print word[0]