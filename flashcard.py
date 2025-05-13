import os

class FlashcardManager:
    def __init__(self, file_path):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self.flashcards = self.load_flashcards()

    def load_flashcards(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
            return [tuple(line.strip().split('|')) for line in lines]

    def save_flashcards(self):
        with open(self.file_path, 'w') as f:
            for word, meaning in self.flashcards:
                f.write(f"{word}|{meaning}\n")

    def view_flashcards(self):
        if not self.flashcards:
            print("No flashcards available.")
            return
        for i, (word, meaning) in enumerate(self.flashcards, 1):
            print(f"{i}. {word} - {meaning}")

    def clear_flashcards(self):
        confirm = input("⚠️ Are you sure you want to delete all flashcards? (y/n): ").strip().lower()
        if confirm == 'y':
            self.flashcards = []
            self.save_flashcards()
            print("🗑️ All flashcards have been cleared.")
        else:
            print("Operation cancelled.")

    def add_flashcard(self):
        word = input("Enter the word: ")
        meaning = input("Enter the chinese: ")
        self.flashcards.append((word, meaning))
        self.save_flashcards()
        print("Flashcard added.")

    def edit_flashcard(self):
        self.view_flashcards()
        try:
            index = int(input("Enter flashcard number to edit: ")) - 1
            if 0 <= index < len(self.flashcards):
                word = input("New word: ")
                meaning = input("New meaning: ")
                self.flashcards[index] = (word, meaning)
                self.save_flashcards()
                print("Flashcard updated.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Please enter a valid number.")

    def quiz_mode(self):
        import random
        if not self.flashcards:
            print("No flashcards available for quiz.")
            return
        random.shuffle(self.flashcards)
        score = 0
        for word, meaning in self.flashcards:
            answer = input(f"What does '{word}' mean? ")
            if answer.strip().lower() == meaning.strip().lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong. The correct answer is: {meaning}")
        print(f"\nYour score: {score}/{len(self.flashcards)}")
