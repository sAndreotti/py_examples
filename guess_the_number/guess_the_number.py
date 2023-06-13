# Guess the number
import random as ran

def guess(x):
    random_number = ran.randint(1, x)
    guess=0
    while guess!=random_number:
        guess = int(input(f"Indovina un numero tra 1 e {x}: "))
        if guess < random_number: print("Riprova, troppo basso")
        if guess > random_number: print("Troppo alto")

    print(f"Indovinato! {guess} era il numero")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback!='C':
        if low != high:
            guess = ran.randint(low, high)
        else:
            guess = low
            
        feedback = input(f'Is {guess} Troppo alto (H), troppo basso (L), o corretto (C)? ').upper()

        if feedback == 'H': high = guess-1
        if feedback == 'L': low = guess+1

    print(f"Yeeee, trovato, {guess} era il tuo numero")


computer_guess(10)