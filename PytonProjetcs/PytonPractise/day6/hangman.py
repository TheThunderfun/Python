import random
from hangman_art import logo,stages
import hangmanWords 

chosenWord = random.choice(hangmanWords.wordList)

correctLetters = []
gameOver = False
errors = 0
life=6;

print(logo)
# Placeholder inicial con guiones bajos
display = ["_"] * len(chosenWord)
print(chosenWord)
while not gameOver:
    guess = input("Guess a letter: ").lower()
    
    print(f"guess: {guess} correct letters: {correctLetters}")
    if guess in correctLetters:
        print(f"You've already guessed {guess}. Try another letter.")
        guess = input("Guess a letter: ").lower()
        
    
    if guess in chosenWord:
        for index, letter in enumerate(chosenWord):
            if letter == guess:
                display[index] = letter
                correctLetters.append(guess)
    elif guess not in chosenWord:
        errors += 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.Life remaining: {life-errors}")
    
    print(stages[errors])  # Mostrar la horca
    print(" ".join(display))  # Mostrar el progreso de la palabra

    # Verificar si el jugador ha ganado
    if "_" not in display:
        gameOver = True
        print("*************************You win!*************************")

    # Verificar si el jugador ha perdido
    if errors == 6:
        gameOver = True
        print("*************************You lose!*************************\n")
        print(f"You lose! The word was: {chosenWord}")
        
        
        
#import random

# wordList = ["python", "developer", "hangman", "programming", "algorithm", "function", "variable", "debugging", "syntax", "iteration"]

# chosenWord=random.choice(wordList)

# print(chosenWord)

# correctLetters=[]

# gameOver=False

# stages= ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']

# errors=0;
# while not gameOver:
#     guess=input("Guess a letter:").lower()  
#     displpay=""

#     for letter in chosenWord:
#         if letter==guess:
#          displpay+=letter
#          correctLetters.append(guess)
         
#         elif letter in correctLetters:
#             displpay+=letter
#         else:
#             displpay+="_"
  
#     if guess not in chosenWord:
#       errors+=1;
#     elif errors==6:
#       gameOver=True
#       print("You lose!")
#     if errors<6:
#       print(stages[errors])
#     else:
#           print(stages[6])
        
#     print(errors)
#     print(displpay)



  
# placeHolder=""

# wordLength=len(chosenWord)

# for position in range(wordLength):
#         placeHolder+="_" 
    
# if "_" not in displpay:
#     gameOver=True
#     print("You win")
        
    


