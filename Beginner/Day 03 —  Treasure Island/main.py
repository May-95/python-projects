from time import sleep

# welcome message to user.
print("Welcome to Treasure Island.")
sleep(0.5)
print("Your mission is to find the treasure on this island.")
sleep(0.5)

left_right = input(
    "You have come across a crossroad. Do you go 'left' or 'right'? ")
sleep(0.3)

# if statement that takes player to different routes depending on their choices.
if left_right.lower() == "left":
    sleep(0.2)
    swim_wait = input(
        "You have come to a lake. Enter 'wait' to wait for a boat and 'swim' to swim across the lake: ")
    sleep(0.2)
    if swim_wait.lower() == "wait":
        door = input(
            "You have found three caves with coloured doors. There is a 'blue' door, a 'yellow' door and a 'red door'. Which door do you go through? ")
        sleep(0.2)
        if door.lower() == "yellow":
            print("You have found the treasure. YOU WON!")
        elif door.lower() == "red":
            print("You have been burned by fire. GAME OVER!")
        elif door.lower() == "blue":
            print("You have been eaten by beasts. GAME OVER!")
        else:
            print("Game OVER!")
    else:
        print("You have been attacked by a trout. GAME OVER!")
else:
    print("You have fallen into a hole. GAME OVER!")
