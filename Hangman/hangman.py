import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 6
    while len(word_letters)>0 and lives>0:
        print(f'You have {lives} lives left and you have used these letters:', ' '.join(used_letters)) # ' 'join(['a','b''c']) --> 'a,b,c'
        
        word_list = [letter if letter in used_letters else '-' for letter in word] #What current word is
        print('Current words:',' '.join(word_list))
        
        # user input
        user_letter = input('Guess a letter').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word')
        elif user_letter in used_letters:
            print('You have already used that character. Please try again')
        else:
            print('Invalid character. Please try again')
    if lives == 0:
        print('You died, sorry. The word was',word)
    else:
        print(f"You guessed the word {word}!")

hangman()    

