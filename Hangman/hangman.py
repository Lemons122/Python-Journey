import random
from words import words
import string
import os
def get_valid_word(words):
    word = random.choice(words)
    min_letters = int(input('Min letters (at maximum 14): '))
    max_letters = int(input('Max letters (at least 3): '))

    while len(word) > max_letters or len(word) < min_letters or '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = int(input('Lives: '))
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left, and have used the following letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('\nGuess a letter: ').upper()
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('That letter is not in the word!')
        
        elif user_letter in used_letters:
            print('\nYou have already guessed that letter.')
        else:
            print('\nInvalid character')
    if lives == 0:
        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou were hung, the word was', word, '\n\nPress Enter to Close')
    else:
        print('The word was:', word, 'and you had', lives, 'lives left.\n\nPress Enter to Close')

hangman()
input()