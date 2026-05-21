# Hangman game in python
# from word-list import words
import random

words = (
    "toyota", "honda", "ford", "bmw", "audi",
    "nissan", "mazda", "hyundai", "kia", "chevrolet",
    "mercedes", "volkswagen", "tesla", "lexus",
    "porsche", "ferrari", "lamborghini", "mitsubishi",
    "aston-martin",

    "civic", "corolla", "camry", "accord", "mustang",
    "ranger", "prius", "supra", "golf"
)

# dictionary of key:()
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/| ",
                  "   "),
               4:(" o ",
                  "/|\\",
                  "   "),
               5:(" o ",
                  "/|\\"
                  "/  "),
               6:(" o ",
                  "/|\\",
                  "/ \\")}

def display_man(wrong_guesses):
    print("************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses) # begin the game 
        display_hint(hint) # represent the answer we gave to guess

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha: # use for guess only 1 alphabet and not a number
            print("Invalid input")
            continue
        
        if guess in guessed_letters: # for a execute when the letter is already guess no second time 
            print(f"{guess} is already guess")
            continue

        guessed_letters.add(guess)
            
      # we put if in while loop
        if guess in answer:
           for i in range(len(answer)):
               if answer [i] == guess:
                   hint[i] = guess
        else:
            wrong_guesses += 1
        if "_" not in  hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False
        


if __name__ == "__main__":
    main()