print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input('You\'re at a cross road! What is your choice "left" or "right?".').lower()

if direction == "left":
    island = input('You\'ve come to the sea and there is an island in the middle of the sea.'
                   ' Type "wait" to wait for a boat and "swim" to swim along!').lower()
    if island == "wait":
        colour = input("You arrive at the island unharmed. There is a house with 3 doors."
                       " One red, one yellow and one blue. "
                       "Which colour do you choose?").lower()
        if colour == "red":
            print("You entered the room with fire, you lose the game!")
        elif colour == "blue":
            print("The room is full with snakes, you lose the game!")
        elif colour == "Yellow":
            print("Wohoo! You find the treasure, you made a victory!!")
        else:
            print("you chose a door that doesn't exist! Game Over!")
    else:
        print("Ooh no! There is a giant crocodile,you won't survive! "
              "May you find the treasure next time")

elif direction == "right":
    print("oops! You've fell into the pothole!")
else:
    print("You don't have that choice! you typed something wrong")
