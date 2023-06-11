# Guess the number
import random as ran

def guess(x):
    random_number = ran.randint(1, x)
    guess=0
    while guess!=random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number: print("Guess again, too low")
        if guess > random_number: print("Too high")

    print(f"Guess! {guess} is the number")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback!='C':
        if low != high:
            guess = ran.randint(low, high)
        else:
            guess = low
            
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').upper()

        if feedback == 'H': high = guess-1
        if feedback == 'L': low = guess+1

    print(f"Yeeee, found {guess} as your number")


computer_guess(10)