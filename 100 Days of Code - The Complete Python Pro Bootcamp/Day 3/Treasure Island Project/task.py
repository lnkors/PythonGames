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

direction = input("You are at a cross road, where do you want to go? \n Type left or right.")
if direction == "left" or direction == "Left":
    action = input("You have come to a lake and there is an island in the middle. \n "
                   "Type 'swim' to swim across or 'wait' to wait for a boat")
    if action == "wait":
        door = input("You have come to a selection of doors. \n "
                     "Which door do you select: red, blue, yellow?")
        if door == "red":
            print("Game Over! You got burned by the fire.")
        elif door == "blue":
            print("Game Over! You got eaten by the wizard.")
        elif door == "yellow":
            print("You won! Congrats the treasure is yours!")
        else:
            print("Game Over! You lost.")
    else:
        print("Game Over! You got eaten by a shark on the swim over to the island.")
else:
    print("Game Over! You fell into a hole!")

