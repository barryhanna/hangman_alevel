import random


def main():
    dictionary = ["python", "monty", "parrot", "grail", "flying", "circus"]
    hidden_word = dictionary[random.randint(0, len(dictionary)-1)]
    display_word = list('*' * len(hidden_word))
    lives = 5
    guessed_letters = set()

    while lives > 0:
        print("Lives: {0} Guessed Letters: {1}".format(lives,guessed_letters))
        guess_letter = str.lower(raw_input("Please enter a letter:"))
        
        if guess_letter in guessed_letters:
            print("Already tried '{0}'".format(set(guess_letter)))
            continue
        
        guessed_letters.add(guess_letter)
        print(guess_letter)
        display_index = 0
        letter_found = False
        for letter in hidden_word:
            if letter == guess_letter:
                letter_found = True
                display_word[display_index] = guess_letter
            display_index += 1
        lives = lives if letter_found is True else lives-1
        print(display_word)
        if '*' not in display_word:
            break

    if lives > 0:
        print("Congratulations, you win!")
    else:
        print("Tough luck. Maybe next time.")

if __name__ == "__main__":
    main()

""" Concepts:
previous knowledge:
data-types
selection
arithmetic operations
relational operations
boolean operations

not covered:
global variables
random number generation
procedural programming

lessons:
1) variable declaration and assignment / input&output
2) arrays
3) iteration
4) functions
5) string manipulation
6) designing a game (leading to hangman)

"""