# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
def valid(word):
    if word not in wordlist: return 0
    return 1

def validstart(word):
    length=len(word)
    for words in wordlist:
        if words[:length]==word:
            print words
            return 1
    return 0
        

# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.   in string.ascii_letters
wordlist = load_words()


def ghost():
    print
    print'Hi'
    print'This is the ghost, do not be scared, it is just a game.'
    print'This game is for two players, not suitable for Dan Sheng Gou'
    playerone=raw_input('PLAYER 1, please input your name  ' )
    print 'Thanks '+str(playerone)+', you are player one now'
    playertwo=raw_input('PLAYER 2, please input your name  ' )
    print 'Thanks '+str(playertwo)+', you are player two now'
    print'3'
    print'2'
    print'1'
    print
    word=''
    for ctr in range(100):
        if ctr%2==0:
            print playerone
        if ctr%2==1:
            print playertwo
        char=raw_input('please input a character  ')
        while char not in string.ascii_letters:
            print'are you retarded? just a character'
            char=raw_input('input a character  ')
        word+=string.lower(char)
        print'Current word fragment is '+word
        if valid(word):
            if ctr%2==0: print playerone +'loses, this is valid word'
            else: print playertwo +'loses, this is valid word'
            break
        if not validstart(word):
            if ctr%2==0: print playerone +"loses, not valid start"
            else: print playertwo +"loses, not valid start"
            break
        ctr+=1

        
            















