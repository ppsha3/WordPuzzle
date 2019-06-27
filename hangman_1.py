import random
import time


def generate_word(len_word):

    filepath = "words/word" + str(len_word) + ".txt"

    with open("{}".format(filepath),"r") as wordfile:

        words = wordfile.readlines()
        random_word = random.choice(words)

    return random_word


def reveal_word(current_guess, len_word):

    for i in range(len_word):
        if current_guess == word[i]:
            current_word.pop(i)
            current_word.insert(i, current_guess)


##def parse_guess(current_guess):
##
##    if current_guess.lower().isalpha():
##        print("Pass!")
##
##    return True


def game_over():

    global current_word

    if '*' in current_word:
        print('\nYou couldn\'t guess the word.\n\n   The correct word was {}'.format(word))        
    
    print("Game Over!!\n\n\n")

def reveal_hint(word, current_word):

    return True


def play():

    global attempts

    print("\n\nOk! Start the guesses.\n\n")

    while attempts > 0:

        time.sleep(0.5)
        print("\nYou have {} number of attempt/s left.\nYour current word: {}".format(attempts, current_word))
        print("Your previous guess: ", *previous_guess)
        print("\n\n")
        
        current_guess = input("Guess the letter: ")

        if current_guess.lower().isalpha():
            if current_guess.lower() in word:
                print("\n  Great! ")
                reveal_word(current_guess.lower(), len_word)
            else:
                print("\n  Wrong Attempt! ")
            previous_guess.append(current_guess.lower())
            attempts = attempts - 1
        else:
            print("\n  Error! Not a valid input\n\n")


def start():

    global attempts
    
    attempts = int(input("\nChoose the number of attempts[3 to 10]: "))

    if attempts in range(3, 10):
        len_word = int(input("\nChoose the length of the secret word[3 to 7]: "))
        if len_word in range(3, 7):
            word = generate_word(len_word)
            current_word = list("*") * len_word
            previous_guess = []
            return True
        else:
            print("\nPlease choose between 3 and 7")
            return False
    else:
        print("\nPlease choose between 3 and 10")
        return False


def main():

##    print("\n\nWelcome to Hangman!!\n\n")
##    name = input("Enter your name: ")
##    print("\nGet ready to play, {}!\n".format(name))

    while start() is False: pass
    play()
    game_over()

if __name__ == '__main__':
    main()
        

    
        
    
