import random
guesses_allowed = 4

def play_or_not():
    play_or_not = input("Would you like to play? (yes/no) ").lower().strip()
    if play_or_not == "yes":
        print("Let's play!")
        guess_reseter()
    elif play_or_not == "no":
        print("")
        print("Um, okay?...")
        quit()
    else:
        print("Learn to type, lil' bro!")

def guess_reseter():
    guess_loop()
    
def guess_loop():
    random_no = random.randint(1, 10)
    guess_no = 0
    print("I am thinking of a number between 1 and 10...")
    print(f"You have {guesses_allowed} guesses to guess the number...")
    while True:
        guess_no += 1
        try:
            guess = int(input("Enter your guess: "))
            if guess_no - 1 < guesses_allowed:
                if guess == random_no:
                    print("Well done!")
                    print(f"You got the number in {guess_no} guesses, maximum is {guesses_allowed}!")
                    play_or_not()
                elif guess > random_no:
                    print("The number is less than your guess!")
                elif guess < random_no:
                    print("The number is larger than your guess!")
                else:
                    print("Enter a real number!")
            else:
                print("You lost! Try again:")
                print(f"The number was {random_no}")
                quit()
        except KeyError as e:
            print("Get it right, lil' bro!")
            guess_loop()
        
play_or_not()
