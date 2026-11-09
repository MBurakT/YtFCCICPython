import random

print("Welcome to Jargon Jumble")

words = ["Python", "JavaScript", "Bootstrap", "Dart", "Swift"]
random.shuffle(words)

index = 1
correct_guess = 0
words_length = len(words)
score = ""
total_point = 0
for word in words:
    word = word.lower()
    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters)

    print(f"{index} of {words_length}\nScrambled Word: {scrambled_word}")

    guess = input("Enter your guess or skip or quit: ").strip().lower()

    if guess == word:
        print("✅")
        score += "✅"
        correct_guess += 1
        total_point += 10
    elif guess == "skip":
        print("➖")
        score += "➖"
        index += 1
        continue
    elif guess == "quit":
        score = score.ljust(words_length, "❌")
        left_over = words_length + 1 - index
        i = 0
        while i < left_over:
            total_point -= 10
            i += 1
        break
    else:
        print("❌")
        score += "❌"
        total_point -= 10
    index += 1

print(f"Score: {score} {correct_guess}/{words_length} Points: {total_point}")
