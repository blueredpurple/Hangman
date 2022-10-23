import random
from python.h import new_func
from words import words
import string

def get_valid_word(words):#in order to function work we need a list, list should be given 
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word

def hangman():
    #global word
    word = get_valid_word(words)
    #global word_letters
    word_letters = set(word)  # letters in the word
    #global alphabet
    alphabet = set(string.ascii_uppercase)
    #global used_letters
    used_letters = set()  # what the user has guessed
    
    #getting user input
    while len(word_letters)>0 :
        word_list = new_func(word, used_letters)
        print("you have used these letters: ", ' '.join(used_letters))
        
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)#forgeted add thats the reason why it was not showing it 
            if user_letter in word_letters:
                word_letters.remove(user_letter)#forgeted remove thats the reason why it was not removing it
                print('\nYour letter,', user_letter, 'is not in the word.')

            elif user_letter in used_letters:
                print('\nYou have already used that letter. Guess another letter.')
            
            else:
                print('\nThat is not a valid letter.')


if __name__ == '__main__':
    hangman()


