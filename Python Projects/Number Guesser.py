import random

def play_or_not():    
    while True:
        play = input("Would you like to play? (yes/no) ").lower()
        if play == "yes":
            print("Okay! Let's play.")
            main_play()
        elif play == "no":
            print("Goodbye!")
            quit()
        else:
            print("Please enter a valid input!")
            continue

def main_play():
    while True:    
        guess_no = 0
        top_of_range = int(input("Please enter a number: "))
        if top_of_range <= 1:
            print("Please enter a number greater than 1!")
            continue
        elif top_of_range > 1:
            try:
                top_of_range = int(top_of_range)
                random_no = random.randint(1, top_of_range)
                while True:
                    guess_no += 1
                    guess = int(input("Please enter your guess: "))
                    if guess == random_no:
                        print("Well done! Let's play!")
                        print(f"You got {random_no} in {guess_no} guesses!")
                        play_or_not()
                    elif guess > random_no:
                        print("The number is less than your guess!")
                    elif guess < random_no:
                        print("The number is greater than your guess!")
                    else:
                        print("How the heck?")
                        continue
                
            except ValueError as e:
                print("Please enter a valid input")
        else:
            print("Please enter a valid input!")
            continue
        
play_or_not()