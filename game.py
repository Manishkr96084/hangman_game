import csv
import random

# Read words from CSV file
with open("name.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    words = [row[0] for row in reader]

# Select a random word from CSV
word = random.choice(words)

guessed_letters = []
attempts_left = 6
display_word = ["_"] * len(word)

print("🎯 Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

while attempts_left > 0 and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Attempts left:", attempts_left)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ Letter already guessed.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong!")
        attempts_left -= 1

if "_" not in display_word:
    print("\n🎉 You won! The word was:", word)
else:
    print("\n💀 You lost! The word was:", word)
