import random as rnd

while True:
  try:
    num = int(input("Enter a number: "))
    if num.isdigit():
      if top_of_range > 1:
        random_no = rnd.randint(1, top_of_range)
        break
      else:
        print("Please enter a valid number")
    elif num == "exit":
      quit()
    else:
      print("Please enter a valid input!")
      continue
  except KeyError:
    print("Please enter a valid input!")
    
guess_no += 1
guess = input("Please enter your guess: ")
if guess == random_no:
  print("Well done, have a good day!")
  quit()
elif guess > random_no:
  print("The number is larger than your guess!")
elif guess < random_no:
  print("The number is smaller than your guess!")
else:
  print("Please enter a valid number")
            
print(guess_no)
