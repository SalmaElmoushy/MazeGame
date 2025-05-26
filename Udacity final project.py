import time
import random

total_score = 0
hint="Do you want a hint? (yes or no)"
# Function to print text with delay
def print_with_delay(text, delay):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()

# Function to get user input and handle invalid input
def get_valid_input(valid_options):
    while True:
        user_input = input().lower()
        if user_input in valid_options:
            return user_input
        else:
            print_with_delay("Sorry, I didn't understand that. Please enter a valid option.", 0.03)

# Function for the first part of the game
def part_one():
    global total_score
    print_with_delay("Welcome to the game!\n", 0.03)
    print_with_delay("If Score >= 20 this means you won\n", 0.03)
    print_with_delay("If Score =< 20 this means you lose\n", 0.03)
    print_with_delay("You wake up in a dark room with no memory of how you got there.\n", 0.03)
    print_with_delay("You look around and see three doors.\n", 0.03)
    #the door chosen randomly
    doors = ["left", "middle", "right"]
    door_choice = random.choice(doors)
    sentence= "You open the door and see a"
    if door_choice == "left":
        print_with_delay( sentence+ " pile of treasure!\n", 0.03)
        total_score += 10
    elif door_choice == "middle":
        print_with_delay(sentence+" monster!\n", 0.03)
        total_score -= 5
    else:
        print_with_delay(sentence+"n empty room.\n", 0.03)

    print_with_delay(f"\nYour current score is {total_score}.\n", 0.03)

# Function for the second part of the game
def part_two():
    global total_score
    print_with_delay("You leave the room and find yourself in a forest.\n", 0.03)
    print_with_delay("You see two paths ahead of you.\n", 0.03)
    print_with_delay("Which path do you take? (left or right): \n", 0.03)
    # ask user if they want a hint
    print_with_delay(hint, 0.03)
    answer = get_valid_input(["yes", "no"])
    if answer == "yes":
        print_with_delay("The left path is shorter.The right path is safer.", 0.03)
        total_score -= 5
    else:
        print_with_delay("Alright, let's move on.", 0.03)
    print_with_delay("Which path do you take? \n", 0.03)
    path_choice = get_valid_input("Which path do you take? (left or right): ")
    if path_choice == "left":
        print_with_delay("You take the left path and arrive at a river.\n", 0.03)
        print_with_delay("You can either swim across or try to find a bridge.\n", 0.03)
        print_with_delay("What do you do? (swim or look for a bridge): \n", 0.03)
        # ask user if they want a hint
        print_with_delay(hint, 0.03)
        answer = get_valid_input(["yes", "no"])
        if answer == "yes":
            print_with_delay("There is a bridge upstream. There is a strong current in the river.", 0.03)
            total_score -= 5
        else:
            print_with_delay("Alright, let's move on.", 0.03)
        print_with_delay("What do you do? \n", 0.03)
        river_choice = get_valid_input("What do you do? (swim or look for a bridge): ")
        if river_choice == "swim":
            print_with_delay("You try to swim across but get swept away by the current!\n", 0.03)
            total_score -= 10
        else:
            print_with_delay("You find a bridge and safely cross the river.\n", 0.03)
            total_score += 5
    else:
        print_with_delay("You take the right path and find a shortcut through the forest!\n", 0.03)
        total_score += 10
    print_with_delay(f"\nYour current score is {total_score}.\n", 0.03)
    # check if game is over
    if total_score >= 20:
        print_with_delay("Congratulations! You have won the game!", 0.03)
    else:
        print_with_delay("Sorry, You lost", 0.03)
    # ask user if they want to play again
    print_with_delay("Do you want to play again? (yes or no)", 0.03)
    play_again = get_valid_input(["yes", "no"])
    if play_again == "yes":
        total_score = 0
        part_one()
        part_two()
    else:
        print("Thanks for playing!")
part_one()
part_two()