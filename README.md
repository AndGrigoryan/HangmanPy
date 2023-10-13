# HangmanPy


# Hangman Game in Python

Welcome! This project is a console-based implementation of the classic "Hangman" game written in Python. Play the game by guessing words or letters and avoid getting "hanged." The project includes key functionalities such as:

- **Random Word Selection:** The `get_rand_word` function randomly selects a word from the provided list.

- **Validation of Guessed Words or Letters:** The `validate_guessed_word_or_letter` function ensures user input correctness for guessed words and letters.

- **Result Display:** The `display_result` function shows the game result based on whether you win or lose.

- **Reading Words List from a File:** The `get_words_list` function reads a list of words from a file, providing a variety of options for guessing.

- **Check if Entered Early:** The `check_was_entered_early` function prevents re-entering previously guessed words or letters.

- **Check Guessed Letter:** The `check_letter` function verifies if the guessed letter is in the hidden word and updates the game state.

- **Incorrect Guess Handling:** The `not_guess` function manages the case when a guessed letter is incorrect.

- **Gameplay Loop:** The `play` function orchestrates the main gameplay loop, interacting with other functions.

Simply clone the repository, specify the path to your words file, and enjoy the game! We welcome your contributions and suggestions for improvement.
