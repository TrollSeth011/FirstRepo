from random import randint

print('Please select one of the choices below.')
player1 = input('Rock(r), Paper(p), Scissors(s)')

random = randint(1,3)
if random == 1:
    player2 = 'r'
elif random == 2:
    player2 = 'p'
else:
    player2 = 's'

def whowins(player1, player2):
    print("Player1 has picked " + player1)
    print("Player2 has picked " + player2)
    if player1 == player2:
        print("It's a draw!")
    else:
        if player1 == 'r' and player2 == 'p':
            print('player2 wins!')
        elif player1 == 'r' and player2 == 's':
            print('player1 wins!')
        elif player1 == 'p' and player2 == 's':
            print('player2 wins!')
        elif player1 == 'p' and player2 == 'r':
            print('player1 wins!')
        elif player1 == 's' and player2 == 'p':
            print('player1 wins!')
        elif player1 == 's' and player2 == 'r':
            print('player2 wins!')
whowins(player1, player2)
