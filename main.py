# linguabuddy/main.py
from flashcard import FlashcardManager
from streak_tracker import StreakTracker
from datetime import date
import os

flashcard_file = "data/flashcards.txt"
streak_file = "data/streak.txt"

flashcard_manager = FlashcardManager(flashcard_file)
streak_tracker = StreakTracker(streak_file)

def main_menu():
    print("\n📚 Welcome to LinguaBuddy!")
    print("1. View Flashcards")
    print("2. Add Flashcard")
    print("3. Edit Flashcard")
    print("4. Daily Quiz")
    print("5. View Streak")
    print("6. Clear Flashcards")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        flashcard_manager.view_flashcards()
    elif choice == "2":
        flashcard_manager.add_flashcard()
    elif choice == "3":
        flashcard_manager.edit_flashcard()
    elif choice == "4":
        flashcard_manager.quiz_mode()
        streak_tracker.update_streak()
    elif choice == "5":
        streak_tracker.view_streak()
    elif choice == "6":
        flashcard_manager.clear_flashcards()
    elif choice == "7":
        print("👋 Goodbye and happy learning!")
        exit()
    else:
        print("⚠️ Invalid option.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    main_menu()
    while True:
       
        cont = input("\n🔁 Continue? (y/n): ").strip().lower()
        if cont == "n":
            print("👋 Goodbye and happy learning!")
            break
        elif cont == "y":
            clear_screen()
            main_menu()
            continue
        else:
             print("Invalid option.")



if __name__ == "__main__":
    main()