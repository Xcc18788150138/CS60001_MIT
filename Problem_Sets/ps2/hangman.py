# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed = []
    for i in range(len(secret_word)):
        guessed.append(secret_word[i])
        if secret_word[i] not in letters_guessed:
            guessed[i] = '_'
    guessed_letter = ''
    for letter in guessed:
        guessed_letter += letter
    return guessed_letter
        

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letter = string.ascii_lowercase
    letter_avail = ''
    for letter in all_letter:
        if letter not in letters_guessed:
            letter_avail += letter
    return letter_avail

    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Loading word list from file...\n55900 words loaded\nWelcome to the game Hangman!\nI am thinking of a world that is '
          + str(len(secret_word)) + ' letters long.')
    print('---------------')
    
    print('You have 3 warnings left.')
    guesses = 6
    warning = 3
    letter_avail = string.ascii_lowercase
    letters_guessed = []
    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        print('----------------------')
        print('You have ' +str(guesses) + ' guesses left')
        print('Available letters: ' + letter_avail)
        letter = input('Please guess a letter: ')
        if letter in string.ascii_lowercase:  
            if letter not in letters_guessed:
                letters_guessed.append(letter)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                letter_avail = get_available_letters(letters_guessed)
                if letter in secret_word:
                    print('Good guess: ' + guessed_word)
                elif letter in ['a', 'e', 'i', 'o', 'u']:
                    print('Opps! The letter is not in my world: '+ guessed_word)
                    guesses -= 2
                else: 
                    print('Opps! The letter is not in my world: '+ guessed_word)
                    guesses -= 1
            elif warning > 0:
                warning -= 1
                print("Opps! You've already guessed that letter.. You have " + str(warning) + ' warnings left: ' + guessed_word)
            else:
                guesses -= 1
        elif warning > 0:
            warning -= 1
            print('Opps! That is not a valid letter. You have ' + str(warning) + ' warnings left: ' + guessed_word)
        else:
            guesses -= 1
    print('--------------------')
    num_letter = []
    for letter in secret_word:
        if letter not in num_letter:
            num_letter.append(letter)
    if is_word_guessed(secret_word, letters_guessed):
        tot_score = len(num_letter)*guesses
        print('Congratulations, you won!\nYour total score for this game is: '+ str(tot_score))
    else:
        print('You have lost! Have another try')
        
        
        


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = my_word.replace(' ', '')
    letter_my = []
    for letter in word:
        if letter not in letter_my:
            letter_my.append(letter)
    if len(word) != len(other_word):
        return False
    for i in range(len(word)):
        if word[i] != '_':
            if word[i] != other_word[i]:
                return False
    for j in range(len(other_word)):
        if word[j] == '_' and other_word[j] in letter_my:
            return False
    return True
    


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #wordlist = load_words()
    matched_word = ''
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_word += (word + ' ')
    if matched_word == '':
        print('No matches found')
    return matched_word.strip()



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Loading word list from file...\n55900 words loaded\nWelcome to the game Hangman!\nI am thinking of a world that is '
          + str(len(secret_word)) + ' letters long.')
    print('---------------')
    
    print('You have 3 warnings left.')
    guesses = 6
    warning = 3
    letter_avail = string.ascii_lowercase
    letters_guessed = []
    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        print('----------------------')
        print('You have ' +str(guesses) + ' guesses left')
        print('Available letters: ' + letter_avail)
        letter = input('Please guess a letter: ')
        if letter == '*':
            print(show_possible_matches(guessed_word))
        elif letter in string.ascii_lowercase:  
            if letter not in letters_guessed:
                letters_guessed.append(letter)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                letter_avail = get_available_letters(letters_guessed)
                if letter in secret_word:
                    print('Good guess: ' + guessed_word)
                elif letter in ['a', 'e', 'i', 'o', 'u']:
                    print('Opps! The letter is not in my world: '+ guessed_word)
                    guesses -= 2
                else: 
                    print('Opps! The letter is not in my world: '+ guessed_word)
                    guesses -= 1
            elif warning > 0:
                warning -= 1
                print("Opps! You've already guessed that letter.. You have " + str(warning) + ' warnings left: ' + guessed_word)
            else:
                guesses -= 1
        elif warning > 0:
            warning -= 1
            print('Opps! That is not a valid letter. You have ' + str(warning) + ' warnings left: ' + guessed_word)
        else:
            guesses -= 1
        
    print('--------------------')
    num_letter = []
    for letter in secret_word:
        if letter not in num_letter:
            num_letter.append(letter)
    if is_word_guessed(secret_word, letters_guessed):
        tot_score = len(num_letter)*guesses
        print('Congratulations, you won!\nYour total score for this game is: '+ str(tot_score))
    else:
        print('You have lost! The world is ' + secret_word)




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
