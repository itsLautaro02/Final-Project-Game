# Chapter 5: Wrapping up the story.
# This is kind of like the conclusion with different endings.

def chapter_5():
    print("The battle was over, but Nova now understood their true power.")
    print("With the city in danger, Nova prepared for the final battle.")
    
    actions = [
        "Talk to people in the city",
        "Learn more about Nova’s powers and past",
        "Choose to keep being a hero, retire, or start a new mission"
    ]
    
    # Players reflect on their journey here.
    while True:
        print("\nWhat would you like to do?")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action}")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            print("You speak with the city's residents and learn their thoughts on Nova.")  # Epilogue-type thing.
        elif choice == "2":
            print("You explore Nova's past, unlocking potential for a sequel.")  # Foreshadowing.
        elif choice == "3":
            print("You make a significant decision about Nova's future as a hero.")  # Endgame choice.
            break
        else:
            print("Invalid choice. Please try again.")
    print("Thank you for playing!")  # End of the game.
    return "End of Game"
