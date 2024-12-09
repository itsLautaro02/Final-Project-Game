# Chapter 1: Setting up the first part of the game
# This is where Nova starts to use their powers and stop a robbery. It's kind of like an intro to the game mechanics.

import random

def chapter_1():
    print("The city lights flickered as Nova tried to control their new powers during a fight.")
    print("Nova stops a robbery at a high-tech lab.")
    
    # This part gives the player options to do stuff.
    actions = ["Fight criminals", "Talk to people", "Look for clues", "Decide what to do next"]
    while True:
        print("\nWhat would you like to do?")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action}")
        
        # This is where the player chooses what to do, I think.
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            print("You engage in combat and practice your fighting skills.")  # Fighting option.
        elif choice == "2":
            print("You gather valuable information about the lab.")  # Talking to people option.
        elif choice == "3":
            print("You find clues pointing to a secret hideout.")  # Investigating option.
        elif choice == "4":
            print("You decide whether to follow the clues or stop more crimes.")  # This might move to the next chapter.
            break
        else:
            print("Invalid choice. Please choose again.")  # Error handling if the player messes up.
    return "Chapter 2"

