def goinornot():
    go_in_or_not()

def go_in_or_not():  
        go_in_or_not = input("Would you like to go in the temple? ").lower()
        if go_in_or_not == "yes":
            print("You enter the temple, the darkness grows around you until you reach a t-junction")
            print("")
            right_or_left()
        elif go_in_or_not == "no":
            print("Um, okay coward...")
            quit()
        if go_in_or_not not in ["yes", "no"]:
            print("Learn to type bozo!")
            goinornot()
            

def right_or_left(): 
        right_or_left = input("Would you like to go right or left? ").lower().strip()
        if right_or_left == "right":
            print("You turn right...")
            right_turn()
        elif right_or_left == "left":
            print("You turn left...")
            left_turn()
        elif right_or_left == "straight":
            print("Revisit this in a bit, I'll add a side quest to this later!")
        else:
            print("Learn to type bozo!")
            right_or_left()

def dungeon():
    print("")
    print("You made it to the dungeon, well done.")
    print("\n\n\n\nYou see a monster charging towards you...\n\n\n\n")
    fight_or_run = input("Do you stand your ground or do you run away? (stand my ground/run away) ").strip().lower()
    while True:
        if fight_or_run == "stand my ground":
            print("The monster seems taken aback at your boldness, and skids to a stop.")
            print("")
            print("It huffs, and points to a door behind it.")
            riddle()
        elif fight_or_run == "run away":
            print("The monster chases you down and you die...")
            quit()
        else:
            print("Who taught you, an American?")
            quit()

def right_turn():
    print("You see 3 levers and a sign: \n Two levers secure your safety, but one sends you to your doom...")
    lever = int(input("Choose levers 1,2, or 3: "))
    if lever in [1, 2, 3]:
        if lever == 1:
            print("You are safe, you may continue...")
            dungeon()
        elif lever == 2:
            print("You are safe, you may continue...")
            dungeon()
        elif lever == 3:
            print("Stay strapped or get clapped, L Bozo!")
            exit()
    else:
        print("Learn to type! Tsk.. tsk.. tsk..")
        right_turn()

def left_turn():
    print("")
    print("You walk awhile, until light is up ahead...")
    riddle()

def riddle():
    print("You see a man floating in a void, an infinite shining on his white robe..")
    print("He speaks, his voice a rumble:")
    print("If you answer this riddle correctly, you shall ascend to immortality:")
    riddle_answer = input("WWhat is greater than God,\nMore evil than the devil,\nThe poor have it,\nThe rich don't need it,\nAnd if you eat it, you'll die?").lower().strip()
    if riddle_answer == "nothing":
        print("Oh, that actually makes sense... Thanks, I got to go talk to the real God now, get scammed!")
        print("The man snaps his fingers, and disappears, a few seconds later, you get teleported to the entrance of the temple.")
        goinornot()
        
go_in_or_not()