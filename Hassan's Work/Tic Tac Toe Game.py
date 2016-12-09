import random
instructions = '''
The players take 1 turn each to place select place 'X' or 'O' on the following table:

     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9

By putting in a value when asked. The player who has 3 mathing pieces in a row wins'''

form = '''
\t| %s | %s | %s |
\t-------------
\t| %s | %s | %s |
\t-------------
\t| %s | %s | %s |
'''

cell = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def win(cell, char):
    return cell[0] == cell[1] == cell[2] == char or\
       cell[3] == cell[4] == cell[5] == char or\
       cell[6] == cell[7] == cell[8] == char or\
       cell[0] == cell[3] == cell[6] == char or\
       cell[1] == cell[4] == cell[7] == char or\
       cell[2] == cell[5] == cell[8] == char

def tie(cell):
    return all(c in ('O','X') for c in cell)

def get_input(player):
    while True:
        m = input('\n%s, select a number (1 - 9) to place your peice: ' % player)
        try:
            return int(m)
        except BaseException:
            print ('Invalid Input')
            continue

board = form % tuple(cell)

instr = input('Would you like to read the instructions? (y/n) ')
if instr.startswith('y'):
    print(instructions)

player1 = input('Enter the name of player 1: ').strip()
player2 = input('Enter the name of player 2: ').strip()

print(player1 + ', you are O and ' + player2 + ', you are X.')
nextPlayer = player1

while not tie(cell) and not (win(cell, 'O') or win(cell,"X")):
    print('This is the board:\n' + board)
    if nextPlayer == player1:
        move = get_input(player1)
        cell[move - 1] = 'O'
        board = form % tuple(cell)
        nextPlayer = player2
    else:
        move = get_input(player2)
        cell[move - 1] = 'X'
        board = form % tuple(cell)
        nextPlayer = player1

if win(cell,"O"):
    print('Congratulations, ' + player1 + ', you have won!')
elif win(cell,"X"):
    print('Congratulations, ' + player2 + ', you have won!')
else:
    print('Unfortunately, neither of you have won... TRY AGAIN!!!')
