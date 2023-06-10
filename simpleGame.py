import random

WORDS = ["python", "java", "javascript", "ruby", "php", "html", "css"]
MAX_LIVES = 6

def display_word(word, guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()simpleGame.py

def play_game():
    word = random.choice(WORDS)
    guessed_letters = set()
    lives = MAX_LIVES

    while True:
        display_word(word, guessed_letters)

        if set(word) == guessed_letters:
            print("Congratulations! You guessed the word.")
            break

        if lives == 0:
            print("Sorry, you ran out of lives. The word was", word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            lives -= 1
            print("Sorry, that letter is not in the word. You have", lives, "lives left.")

if __name__ == "__main__":
    play_game()
