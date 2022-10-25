
import random
from Hangman_visual import Hangman_stages 
import pandas as pd
import string


def get_a_word(words):
    word = random.choice(words)
    return word.upper()

def hangman():
    words_list = list(pd.read_csv('Comic_Characters.csv'))
    word = get_a_word(words_list)
#     print(word)
    letters = set(word)
#     print(letters)
    two_words = False
    first,last = "",""
    if '-' in letters:
        two_words = True
        first = str(word.split('-')[0])
        last = str(word.split('-')[1])
        letters = set(first + last)
#     print(letters)
#     print(two_words)
#     print(first)
#     print(last)
    alphabets = set(string.ascii_uppercase)
    guess = set()
    chance = 6
    while len(letters)>0 and chance>0:
        print(chance,"CHANCE REMAINING!!!\n", ' '.join(guess))
        
        if two_words==True:
            current = [letter if letter in guess else '_' for letter in first] + ['    '] + [letter if letter in guess else '_' for letter in last]
        else:
            current = [letter if letter in guess else '_' for letter in word]
        print(Hangman_stages[6-chance])
        print("Your Word:",' '.join(current))
        guessed = input("Make a Guess:")
        guessed = guessed.upper()
        if guessed in alphabets - guess:
            guess.add(guessed)
            if guessed in letters:
                letters.remove(guessed)
                print('')
            
            else:
                chance = chance-1
                print("\n\nWRONG GUESS!!!\n")
        elif guessed in guess:
            print("\nMake a different guess\n")
        
        else:
            print("\n Please choose from A B C D E F G H I J K L M N O P Q R S T U V W X Y Z\n")
            
    if chance == 0:
        print(Hangman_stages[6-chance])
        print('YOU WERE HANGED!!!\n The Word was ', word)
    else:
        print("Congrats!!!\n You Guessed ",word)  
    
if __name__ == '__main__':
    hangman()