# Rock Paper Scissors
import random as ran

def play():
    user = input("Chose 'R' rock, 'P' paper, 'S' scissors: ").upper()
    computer = ran.choice(['R', 'P', 'S'])

    if user == computer:
        return 'It\'s a tie'
    
    # R > S, S > P, P > R
    print(f"User chose: {user}, Computer chose: {computer}")
    if is_win(user, computer):
        return 'User Wins!'
    
    return 'Computer Wins!'

def is_win(player, opponent):
    #return true if player win
    if(player == 'R' and opponent == 'S') or \
       (player == 'S' and opponent == 'P') or \
       (player == 'P' and opponent == 'R'):
        return True
    

print(play())