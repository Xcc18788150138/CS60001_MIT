# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'
word_list = load_words(WORDLIST_FILENAME)

class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = self.valid_words = load_words(WORDLIST_FILENAME)
        
    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words
        
    def build_shift_dict(self, shift):
        dic = {}
        for letter in string.ascii_lowercase:
            dic[letter] = letter
        for letter in string.ascii_uppercase:
            dic[letter] = letter
        for key, value in dic.items():
            if key in string.ascii_uppercase:
                if ord(key) + shift <= 90:
                    dic[key] = chr(ord(key) + shift)
                else:
                    dic[key] = chr(ord(key) + shift - 26)
                    
            if key in string.ascii_lowercase:
                if ord(key) + shift <= 122:
                    dic[key] = chr(ord(key) + shift)
                else:
                    dic[key] = chr(ord(key) + shift - 26)
        return dic
                
    def apply_shift(self, shift):
        dic = self.build_shift_dict(shift)
        shifted_text = ''
        for letter in self.message_text:
            if letter in string.ascii_lowercase or letter in string.ascii_uppercase:
                new_letter = dic[letter]
            else:
                new_letter = letter
            shifted_text += new_letter
        return shifted_text

        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''


class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self, text)
        self.shift = shift

    def get_shift(self):
        return self.shift

    def get_encryption_dict(self):
        return self.build_shift_dict(self.shift)

    def get_message_text_encrypted(self):
        return self.apply_shift(self.shift)

    def change_shift(self, shift):
        self.shift = shift

class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, text)

    def decrypt_message(self):
        punc = string.punctuation
        (shift_max, max_num) = (0 , 0)
        for shift in range(26):
            valid_num = 0
            decrepted = self.apply_shift(shift)
            s = list(decrepted)
            words = ''.join([o for o in s if not o in punc]).split()
            for word in words:
                if is_word(self.valid_words, word):
                    valid_num += 1
            if valid_num > max_num:
                shift_max = shift
                max_num = valid_num
        de_text = self.apply_shift(shift_max)
        return((shift_max, de_text))

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
    pass #delete this line and replace with your code here
