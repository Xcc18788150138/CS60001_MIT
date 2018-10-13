# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

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

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words
                
    def build_transpose_dict(self, vowels_permutation):
        dic = {}
        for letter in string.ascii_lowercase:
            dic[letter] = letter
        for letter in string.ascii_uppercase:
            dic[letter] = letter
        dic[vowels_permutation[0]] = vowels_permutation[1]
        dic[vowels_permutation[1]] = vowels_permutation[0]
        dic[vowels_permutation[3]] = vowels_permutation[4]
        dic[vowels_permutation[4]] = vowels_permutation[3]
        
        dic[vowels_permutation[0].upper()] = vowels_permutation[1].upper()
        dic[vowels_permutation[1].upper()] = vowels_permutation[0].upper()
        dic[vowels_permutation[3].upper()] = vowels_permutation[4].upper()
        dic[vowels_permutation[4].upper()] = vowels_permutation[3].upper()
        
        return dic
            
    
    def apply_transpose(self, transpose_dict):
        dic = transpose_dict
        shifted_text = ''
        for letter in self.message_text:
            if letter in string.ascii_lowercase or letter in string.ascii_uppercase:
                new_letter = dic[letter]
            else:
                new_letter = letter
            shifted_text += new_letter
        return shifted_text
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        #punc = string.punctuation
        #s = list(self.message_text)
        #words = ''.join([o for o in s if not o in punc]).split()
        vowel_lower = 'aeoiu'
        vowel_upper = 'AEOIU'
        permutation = get_permutations('aeoiu')
        (subs_text, max_num) = ('' , 0)
        
        for seq in permutation:
            valid_num = 0
            dic = self.build_transpose_dict(seq)
            de_text = ''
            
            for letter in self.message_text:
                if letter in vowel_lower or letter in vowel_upper:
                    new_letter = dic[letter]
                else:
                    new_letter = letter
                de_text += new_letter
                
            s = list(de_text)
            punc = string.punctuation
            words = ''.join([o for o in s if not o in punc]).split()
            
            for word in words:
                if is_word(self.valid_words, word):
                    valid_num += 1
            if valid_num > max_num:
                max_num = valid_num
                subs_text = de_text
        if max_num == 0:
            return self.message_text
        else:
            return subs_text
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
