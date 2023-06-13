# Rock Paper Scissors
import random as ran

def play():
    user = input("Scegli 'R' Sasso, 'P' Carta, 'S' Forbici: ").upper()
    computer = ran.choice(['R', 'P', 'S'])

    if user == computer:
        return 'It\'s a tie'
    
    # R > S, S > P, P > R
    print(f"Hai schelto: {user}, Computer: {computer}")
    if is_win(user, computer):
        return 'Hai Vinto!'
    
    return 'Il Computer ha Vinto!'

def is_win(player, opponent):
    #return true if player win
    if(player == 'R' and opponent == 'S') or \
       (player == 'S' and opponent == 'P') or \
       (player == 'P' and opponent == 'R'):
        return True
    

print(play())