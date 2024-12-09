# main.py

# Importing the chapter functions from their respective files
from chapter_1 import chapter_1
from chapter_2 import chapter_2
from chapter_3 import chapter_3
from chapter_4 import chapter_4
from chapter_5 import chapter_5

def main():
    """
    Main function to control the flow of the game.
    This function runs each chapter in sequence, based on the player's progress.
    """
    print("Welcome to Nova's Story!")
    print("Embark on an interactive journey where your choices shape the story.")
    print("\nLet's begin!\n")
    
    # Start with Chapter 1
    next_chapter = chapter_1()  # Calls the first chapter and retrieves the next chapter
    
    # Progress to Chapter 2 if the player completes Chapter 1
    if next_chapter == "Chapter 2":
        next_chapter = chapter_2()
    
    # Progress to Chapter 3 if the player completes Chapter 2
    if next_chapter == "Chapter 3":
        next_chapter = chapter_3()
    
    # Progress to Chapter 4 if the player completes Chapter 3
    if next_chapter == "Chapter 4":
        next_chapter = chapter_4()
    
    # Progress to Chapter 5 if the player completes Chapter 4
    if next_chapter == "Chapter 5":
        chapter_5()  # Final chapter does not need to return anything as it's the last one
    
    # End of the game
    print("\nThank you for playing Nova's Story! We hope you enjoyed it.")

# Ensures the script runs only if it's executed directly (not imported as a module)
if __name__ == "__main__":
    main()
