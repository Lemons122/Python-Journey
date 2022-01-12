import random

def play():
    user = input("Choose an option to play! 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return f'\nIt\'s a tie! Computer chose {computer}'
    if is_win(user, computer):
        return f'\nYou won! Computer chose {computer}'

    return f'\nYou lost! Computer chose {computer}'
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())