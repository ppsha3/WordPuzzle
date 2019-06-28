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


def parse_guess(current_guess):

    if current_guess.lower().isalpha():
        return True
    if current_guess == '*':
        reveal_hint()
        return True


def game_over():

    global current_word

    if '*' in current_word:
        print('\nYou couldn\'t guess the word.\n\n   The correct word was {}'.format(word))
    else:
        print('You guessed the word correctly: {}'.format(word))
    
    print("Game Over!!\n\n\n")


def reveal_hint():

    global word, current_word, len_word, hint_taken

    for i in range(len_word):

        if current_word[i] == '*':
            hint = word[i]
            break

    print("\n  At {} position, the letter is {}".format(i+1, hint))

    hint_taken = True
    
    return True


def play():

    global attempts, current_word, current_guess, previous_guess, word, len_word, hint_taken

    hint_taken = False

    print("\n\nOk! Start the guesses.\n\n")

    while attempts > 0:

        time.sleep(0.5)
        print("\nYou have {} number of attempt/s left.\nYour current word: {}".format(attempts, current_word))
        print("Your previous guess: ", *previous_guess)
        print("\n\n")
        
        current_guess = input("Guess the letter: ")

        if parse_guess(current_guess):
            if current_guess.lower() in previous_guess:
                print("\n  You already guessed that! ")
            elif current_guess.lower() in word:
                print("\n  Great! ")
                reveal_word(current_guess.lower(), len_word)
                attempts = attempts - 1
                previous_guess.append(current_guess.lower())
            elif hint_taken:
                hint_taken = False
            else:
                 print("\n  Wrong Attempt! ")
                 attempts = attempts - 1
                 previous_guess.append(current_guess.lower())

        else:
            print("\n  Error! Not a valid input\n\n")

##    if attempts == 0:
##        while last_chance() is False:   pass
##
##def last_chance():
##
##    last_chance = input("You have exhausted your number of attempts. Do you want to increase you attempts? [Y/N]: ")
##    if last_chance.lower == 'y':
##        new_attempts = int(input("\nChoose the number of attempts[3 to 10]: "))


def start():

    global attempts, current_word, current_guess, previous_guess, word, len_word
    
    attempts = int(input("\nChoose the number of attempts[3 to 10]: "))

    if attempts in range(3, 11):
        len_word = int(input("\nChoose the length of the secret word[3 to 7]: "))
        if len_word in range(3, 8):
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

    print("\n\nWelcome to Hangman!!\n\n")
    name = input("Enter your name: ")
    print("\nGet ready to play, {}!\n".format(name))

    while start() is False: pass
    play()
    game_over()

if __name__ == '__main__':
    main()
        

    
        
    
