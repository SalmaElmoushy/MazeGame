import time
import random

total_score = 0
hint = "Do you want a hint? (yes or no)"

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
    print_with_delay("Welcome to Mysterious Island Escape!\n", 0.03)
    print_with_delay("If your Score >= 20, you win!\n", 0.03)
    print_with_delay("If your Score < 20, you lose.\n", 0.03)
    print_with_delay("You wake up on a mysterious island with no recollection of how you got there.\n", 0.03)
    print_with_delay("As you explore, you come across three paths.\n", 0.03)
    
    # The path chosen randomly
    paths = ["left", "middle", "right"]
    path_choice = random.choice(paths)
    
    sentence = "You take the path and find"
    if path_choice == "left":
        print_with_delay(sentence + " a hidden treasure chest!\n", 0.03)
        total_score += 10
    elif path_choice == "middle":
        print_with_delay(sentence + " a dangerous trap!\n", 0.03)
        total_score -= 5
    else:
        print_with_delay(sentence + " an abandoned campsite.\n", 0.03)

    print_with_delay(f"\nYour current score is {total_score}.\n", 0.03)

# Function for the second part of the game
def part_two():
    global total_score
    print_with_delay("You continue your journey through the island and reach a dense forest.\n", 0.03)
    print_with_delay("Ahead of you, you spot two paths.\n", 0.03)
    print_with_delay("Which path do you take? (left or right):", 0.03)
    
    # Ask the user if they want a hint
    print_with_delay(hint, 0.03)
    answer = get_valid_input(["yes", "no"])
    if answer == "yes":
        print_with_delay("The left path is shorter, but it's guarded by dangerous creatures.", 0.03)
        total_score -= 5
    else:
        print_with_delay("Alright, let's move on.", 0.03)
    
    print_with_delay("Which path do you take?\n", 0.03)
    path_choice = get_valid_input(["left", "right"])
    
    if path_choice == "left":
        print_with_delay("You take the left path and stumble upon a mystical lake.\n", 0.03)
        print_with_delay("You notice a boat on the shoreand decide to take it across the lake.\n", 0.03)
        print_with_delay("As you row across the tranquil waters, you spot a hidden treasure island.\n", 0.03)
        print_with_delay("Do you want to search for treasure? (yes or no):", 0.03)
        
        # Ask the user if they want a hint
        print_with_delay(hint, 0.03)
        answer = get_valid_input(["yes", "no"])
        if answer == "yes":
            print_with_delay("The treasure is buried beneath a large palm tree on the southern side of the island.", 0.03)
            total_score += 10
        else:
            print_with_delay("Alright, let's move on.", 0.03)
        
        print_with_delay("Do you want to search for treasure? (yes or no):", 0.03)
        treasure_choice = get_valid_input(["yes", "no"])
        if treasure_choice == "yes":
            print_with_delay("You dig beneath the palm tree and uncover a chest filled with precious jewels!\n", 0.03)
            total_score += 10
        else:
            print_with_delay("You decide to leave the treasure for another time and continue your adventure.\n", 0.03)
        
    else:
        print_with_delay("You take the right path and encounter a group of hostile natives.\n", 0.03)
        print_with_delay("They demand you to leave their territory immediately.\n", 0.03)
        print_with_delay("What do you do? (fight or flee):", 0.03)
        
        # Ask the user if they want a hint
        print_with_delay(hint, 0.03)
        answer = get_valid_input(["yes", "no"])
        if answer == "yes":
            print_with_delay("Fleeing might be your best option as the natives seem highly skilled in combat.", 0.03)
            total_score -= 5
        else:
            print_with_delay("Alright, let's move on.", 0.03)
        
        print_with_delay("What do you do? (fight or flee):", 0.03)
        action_choice = get_valid_input(["fight", "flee"])
        if action_choice == "fight":
            print_with_delay("You engage in a fierce battle but manage to defeat the natives and continue your journey.\n", 0.03)
            total_score += 5
        else:
            print_with_delay("Realizing the odds are against you, you swiftly retreat and find another route.\n", 0.03)
            total_score -= 10
    
    print_with_delay(f"\nYour final score is {total_score}.\n", 0.03)
    
    # Check if the game is over
    if total_score >= 20:
        print_with_delay("Congratulations! You have successfully escaped from the mysterious island!", 0.03)
    else:
        print_with_delay("Sorry, you did not manage to escape from the mysterious island.", 0.03)
    
    # Ask the user if they want to play again
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
