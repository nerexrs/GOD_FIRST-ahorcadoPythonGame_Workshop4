import random

def choose_word():
    words = ["python", "java", "javascript", "ruby", "rust", "php", "solidity", "go"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6

    print("¡Bienvenido al juego de ahorcado donde adivinas lenmguajes de programación!")
    print(display_word(word_to_guess, guessed_letters))

    while True:
        guess = input("Adivina una letra: ").lower()

        if guess in guessed_letters:
            print("Ya adivinaste esa letra. Intenta de nuevo.")
        else:
            guessed_letters.append(guess)
            if guess in word_to_guess:
                print("¡Correcto! Letra encontrada.")
            else:
                attempts -= 1
                print(f"Incorrecto. Te quedan {attempts} intentos.")

        displayed_word = display_word(word_to_guess, guessed_letters)
        print(displayed_word)

        if displayed_word == word_to_guess:
            print("¡Felicidades! Has ganado. La palabra era: " + word_to_guess)
            break

        if attempts == 0:
            print("¡Perdiste! La palabra era: " + word_to_guess)
            break

if __name__ == "__main__":
    main()
