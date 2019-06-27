def generate_word(len_word):

    word = "secret"

    return word

def reveal_word(current_guess, len_word):

    for i in range(len_word):
        if current_guess == word[i]:
            current_word.pop(i)
            current_word.insert(i, current_guess)

def parse_guess(current_guess):
    return True

def main():

    global name, attempts, len_word, word, current_word, previous_guess

    print("\n\nWelcome to Hangman!!\n\n")
    name = input("Enter your name: ")
    print("\nGet ready to play, {}!!\n".format(name))

    attempts = int(input("Choose the number of attempts[1 to 10]: "))
    len_word = int(input("\nChoose the length of the secret word: "))

    word = generate_word(len_word)
    current_word = list("*") * len_word
    previous_guess = []

    print("\n\nOk! Start the guesses.\n\n")

    while attempts > 0:

        print("You have {} number of attempts left.\nYour current word: {}".format(attempts, current_word))
        print("Your previous guess: ", *previous_guess)
        print("\n\n")
        
        current_guess = input("Guess the letter: ")

        if parse_guess(current_guess):
            if current_guess in word:
                print("Great! ")
                reveal_word(current_guess, len_word)
                attempts = attempts - 1
                previous_guess.append(current_guess)
        else:
            print("Error! Not a valid input\n\n")

    print("\n\nGame Over!!")

if __name__ == '__main__':
    main()
        

    
        
    
