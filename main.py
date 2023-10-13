#!/usr/bin/env python3

from random import choice
import argparse


def display_hangman(tries):
    stages = [  
        # final state: head, torso, both arms, both legs
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
        # head, torso, both arms, one leg
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
        # head, torso, both arms
        '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
        # head, torso and one arm
        '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
        # head and torso
        '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
        # head
        '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
        # initial state
        '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]

    return stages[tries]


def get_rand_word(word_list):               	 # Function to randomly select a word from the given list
    return choice(word_list).upper()


def validate_guessed_word_or_letter():		# Function to validate user input for a guessed word or letter
    alphabet = ''.join([chr(letters) for letters in range(ord('A'), ord('Z') + 1)]) + '-'
    while True:
        is_word = True
        word = input("Enter a letter or a whole word:\n").upper()
        if len(word) > 1: 		# If the input is more than one character, check if each character is in the alphabet
            for letter in word:                  
                if letter not in alphabet:
                    is_word = False
            break
        elif word in alphabet and word != "":
            is_word = False
            break
        else:
            print("Invalid input.  Please repeat:")
        
    return word, is_word


def display_result(victory):		 	# Function to display the result based on the game outcome
    if victory:
        print("\nCongratulations, you have won!!")
    else:
        print("\nUnfortunately you lost.")


def get_words_list(path):			 # Function to get a list of words from the provided file path
    try: 
        with open(path) as f:
            words_ls = f.read().split(', ')
    except Exception as error:
        print(error)
        exit()

    return words_ls


def get_word_completion(word):			# Function to get the initial word completion with underscores
    return ('_ ' * len(word)).split()


def check_was_entered_early(guess, guessed_words, guessed_letters):		 
    # Function to check if a guessed word or letter has been entered early
    if guess in guessed_words or guess in guessed_letters:
        print("You have already entered this word or letter before, enter another letter or whole word:")
        print(f"Already entered letters: {', '.join(guessed_letters)}\nAlready entered words: {', '.join(guessed_words)}\n")
        return False
    else:
        return True


def check_letter(letter, word, word_completion, guessed_letters):	# Function to check if a guessed letter is in the word
    guessed_letters.append(letter)
    is_guessed = True
    if letter in word:
        while word.find(letter) != -1:
            word_completion[word.find(letter)] = letter
            word = word.replace(letter, ' ', 1)
    else:
        is_guessed = False

    return word_completion, is_guessed


def not_guess(tries):				# Function to handle the case when a guessed letter is incorrect
    print(display_hangman(tries - 1))
    return tries - 1


def play(word):					# Function to play the word guessing game
    print("Let's play a word guessing game!")

    word_completion = get_word_completion(word)
    victory = False

    guessed_letters = []
    guessed_words = []
    word_copy = word
    tries = 6

    print(display_hangman(tries))

    while tries != 0:
        print("".join(word_completion))
        guess, is_word = validate_guessed_word_or_letter()
        if check_was_entered_early(guess, guessed_words, guessed_letters): #Checks whether a given letter or word was entered early
            if not is_word:                                               #Checks whether a letter or word has been entered
                word_completion, is_guessed = check_letter(guess, word, word_completion, guessed_letters)
                if not is_guessed:
                    tries = not_guess(tries)
            else:
                guessed_words.append(guess)
                if guess == word:
                    return True 
                else:
                    tries = not_guess(tries)


        if "_" not in word_completion:
            victory = True
            break

    
    return victory


def main():			# Main function to run the word guessing game
    parser = argparse.ArgumentParser(description="Get file for words.")
    parser.add_argument("words_path", type=str, help="The path to the words path.")

    args = parser.parse_args()

    path = args.words_path

    word_list = get_words_list(path)
        
    while True:
        word = get_rand_word(word_list)
        victory = play(word)
        display_result(victory)
        print(f"The hidden word was: {word.capitalize()}")
        
        want = input("Do you want to play more? (Yes\\no): ").lower()
        if want != 'yes':
            exit()


if __name__ == "__main__":
    main()

