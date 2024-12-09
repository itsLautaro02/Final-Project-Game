#Chapter 4: Nova faces the villains' ultimate weapon.
#This is where things get intense, I think, with a big choice at the end.

def chapter_4():
    print("Nova learns the villains are about to use a powerful weapon to take over the city.")
    actions = [
        "Stop the weapon before it’s too late",
        "Fight a supervillain with stronger powers",
        "Use Nova’s energy powers creatively to win",
        "Choose between saving a friend or stopping the villain"
    ]
    
    # Players have to make tough decisions here.
    while True:
        print("\nWhat would you like to do?")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action}")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            print("You race against time and successfully disable the weapon.")  # Heroic move.
        elif choice == "2":
            print("You engage in an epic battle against a powerful foe.")  # Fighting focus.
        elif choice == "3":
            print("You harness your energy powers in a creative way to achieve victory.")  # Strategy focus.
        elif choice == "4":
            print("You face a heart-wrenching choice with lasting consequences.")  # Emotional choice.
            break
        else:
            print("Invalid choice. Please try again.")
    return "Chapter 5"


