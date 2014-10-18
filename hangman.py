import random


def main():
    dictionary = get_guess_words()
    hidden_word = dictionary[random.randint(0, len(dictionary)-1)]
    display_word = list('*' * len(hidden_word))
    lives = 5
    guessed_letters = set()

    while lives > 0:
        print("Lives: {0} Guessed Letters: {1}".format(lives,guessed_letters))
        guess_letter = str.lower(input("Please enter a letter:"))
        
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


def get_guess_words(filename="words.txt"):
    words_file = open(filename,'r').readlines()
    words = []
    for word in words_file:
        words.append(word.rstrip('\n'))
    return words


if __name__ == "__main__":
    main()

