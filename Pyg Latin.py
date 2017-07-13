print 'Welcome to the Pig Latin Translator! It will automatically make the entire word lower case so heads up!'
pyg = 'ay'  #The suffix

original = raw_input('Enter a word:')  #The actual word that the user enters

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:] + first + pyg
    print new_word
else:
    raw_input('Please enter a word.')
print new_word
