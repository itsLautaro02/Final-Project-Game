# Chapter 3: Nova discovers a bigger plot.
# I think this chapter is about finding out more about the villains and their connections.

def chapter_3():
    print("A gust of wind cleared the fog just in time. What remained was an abyss, echoing the pounding.")
    print("Nova uncovers a bigger plot involving powerful people in the city.")
    
    actions = [
        "Question captured bad guys",
        "Confront a corrupt politician",
        "Gather superhero friends or work alone",
        "Reveal the truth or fight the bad guys directly"
    ]
    
    # More choices here to advance the story.
    while True:
        print("\nWhat would you like to do?")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action}")
        
        # I think these choices determine how the story unfolds.
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            print("You interrogate the bad guys and get crucial information.")  # Talking option.
        elif choice == "2":
            print("You confront a politician, uncovering their connection to the villains.")  # Diplomacy option.
        elif choice == "3":
            print("You decide to either rally allies or face the enemies alone.")  # Teamwork vs solo.
        elif choice == "4":
            print("You choose to either expose the villains' plans or engage in a direct fight.")  # Final decision.
            break
        else:
            print("Invalid choice. Please try again.")
    return "Chapter 4"




