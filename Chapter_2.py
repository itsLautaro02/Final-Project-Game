
# Chapter 2: Nova finds the hideout of the villains.
# This chapter kind of focuses on sneaking or fighting, I think. Players get to explore more.

def chapter_2():
    print("Nova finds the secret hideout of the bad guys.")
    actions = ["Sneak into the base", "Use force or stealth to get through", "Find the plan to destroy the city"]
    
    # Letting players choose their strategy.
    while True:
        print("\nWhat would you like to do?")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action}")
        
        # Each choice has a different outcome, I think.
        choice = input("Enter the number of your choice: ")
        
        if choice == "1":
            print("You successfully sneak past the guards.")  # Stealth option.
        elif choice == "2":
            print("You fight or evade guards and make it through the base.")  # Fighting or sneaky mix option.
        elif choice == "3":
            print("You uncover a plan to destroy the city.")  # This probably sets up the next part.
            break
        else:
            print("Invalid choice. Please try again.")  # Error if input isn't valid.
    return "Chapter 3"


