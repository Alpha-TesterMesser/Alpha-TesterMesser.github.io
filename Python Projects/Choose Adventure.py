def right_or_left():
    while True:    
        right_or_left = input("Would you like to go right or left? ").lower()
        if right_or_left == "right":
            print("You turn right...")
            right_turn()
        elif right_or_left == "left":
            print("You turn left...")
            left_turn()
        else:
            print("Learn to type bozo!")
            continue

def right_turn():
    print("You see 3 levers and a sign: \n Two levers secure your safety, but one sends you to your doom...")
    lever = input("Choose levers 1-3")
    if lever.isdigit():
        if lever == 1:
            print("You are safe, you may continue...")
            dungeon()
        elif lever == 2:
            print("You are safe, you may continue...")
            dungeon()
        elif lever == 3:
            print("Stay strapped or get clapped, L Bozo!")
            quit()
    else:
        print("Please enter a valid input!")

def left_turn():
    print("")
    print("You turn left...")

def dungeon():
    print("")
    print("You made it to the dungeon, well done.")
    print("\n\n\n\nYou see a monster charging towards you...\n\n\n")
    fight_or_run = input("Do you stand your ground or do you run away? (stand your ground/ run away)").lower()
    if fight_or_run == "stand you ground":
        print("The monster seems taken aback at your boldness, and skids to a stop.")

right_or_left()