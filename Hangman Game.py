import random
# Words by level
words_list = {
    "easy": ["cat", "dog", "sun", "fish", "head"],
    "medium": ["mirror", "train", "planet", "python", "program"],
    "hard": ["harmony", "whistle", "eclipse", "syndrome", "protocol"]
}
# Attempts by level
attempts_by_level = {
    "easy": 6,
    "medium": 5,
    "hard": 3
}

print("\n======== HANGMAN GAME ========")

levels = ["easy", "medium", "hard"]

# Game Loop through levels
for level in levels:
    print(f"\n----- {level.upper()} LEVEL -----")
    
    original_word = random.choice(words_list[level])
    max_attempts = attempts_by_level[level]
    missing_index = random.randint(0, len(original_word) - 1)
    new_word = original_word[:missing_index] + "_" + original_word[missing_index + 1:]

    print(f"Guess the missing letter in the word.")
    print(f"You have {max_attempts} attempts. Good luck!")
    print("Word:", new_word)

    attempts = 0
    success = False

    while attempts < max_attempts:
        guessed = input("Enter your guess: ")

        if guessed.lower() == original_word[missing_index].lower():
            print("\n🎉 Correct!")
            print("The complete word is:", original_word)
            success = True
            break
        else:
            attempts += 1
            print("❌ Wrong guess.")
            print(f"Attempts left: {max_attempts - attempts}")

    if not success:
        print("\n😢 Game Over!")
        print(f"The correct word was: {original_word}")
        break
    else:
        print(f"✅ Level {level.capitalize()} completed!")

# If all levels passed
else:
    print("\n🏆 Congratulations! You completed all levels of Hangman!")
