# Hangman ITA
import random as ran
import string
from words import words

def get_valid_word(words):
    word = ran.choice(words)
    # non necessario per l'italiano
    while '-' in word or ' ' in word:
        word = ran.choice(words)
    
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # vite
    lives = 6

    # user input
    while len(word_letters) > 0 and lives > 0:
        # lettere usate
        if len(used_letters) > 0:
            print('Hai già provato queste lettere: ', ' '.join(used_letters))
        print(f'Vite rimanenti {lives}')

        # parola che si sta indovinando
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Parola attuale: ", ' '.join(word_list))        

        user_letter = input('Inserisci una lettera: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                # lettera indovinata
                word_letters.remove(user_letter)
            else:
                # lettera non indovianta
                lives = lives -1
                print(f'Lettera non presente, vite rimanenti {lives}')
            

        elif user_letter in used_letters:
            print('Hai già usato questa lettera. Prova ancora')

        else:
            print('Lettera non valida. Prova ancora')
        print()

    if len(word_letters) == 0:
        print(f'Congratulazioni! Hai indovinato la parola {word}!')
    else:
        print('Hai finito le vite')

hangman()