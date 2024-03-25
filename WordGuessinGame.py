import random
import nltk

nltk.download('words', quiet=True)
word_list = nltk.corpus.words.words()
word_list = [word.lower() for word in word_list if word.isalpha()]
filtered_word_list = [word for word in word_list if 3 <= len(word) <= 10]


def guessinggame(counter=0):
    word_required = random.choice(filtered_word_list)
    print("Welcome to the Word Guessing Game !")
    visible_list_word = []
    for index in range(0, len(word_required)):
        visible_list_word.append("_")
    print(word_required)

    while "_" in visible_list_word:
        print("Counter is {}".format(counter))
        print("The word is : ", visible_list_word)
        guess = None
        while isinstance(guess, str) is False:
            guess = input("Please guess a letter or the word...\n")
            counter += 1
        if len(guess) == 1:
            for index in range(0, len(visible_list_word)):
                if word_required[index] == guess:
                    visible_list_word[index] = guess

        elif len(guess) > 1 and guess == word_required:
            print("The word is : ", [word_required])
            if counter == 1:
                print("Congratulations!!!\nYou guessed the word '{}' correctly in the first try!"
                      .format(word_required))
                break
            else:
                print("Congratulations!!!\nYou guessed the word '{0}' correctly in {1} tries!"
                      .format(word_required, counter))
                break
        else:
            print("Pleas type a valid input...")
            continue
    else:
        print("The word is : ", visible_list_word)
        if counter == 1:
            print("Congratulations!!!\nYou guessed the word '{}' correctly in the first try!"
                  .format(word_required))
        else:
            print("Congratulations!!!\nYou guessed the word '{0}' correctly in {1} tries!"
                  .format(word_required, counter))

    if counter <= 1:
        print("Legendary Score")
    elif 5 > counter > 1:
        print("Gold Score")
    elif 9 > counter >= 5:
        print("Silver Score")
    else:
        print("Bronze Score")
    print("Do you wanna start again?")
    game_cond = input("Type 'restart' to start the game again...\n")
    lowercase_input = game_cond.lower()
    if lowercase_input == "restart":
        guessinggame(counter=0)


guessinggame(counter=0)
