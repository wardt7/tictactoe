# Tic Tac Toe Game
  2.
  3. import random
  4.
  5. def drawBoard(board):
  6.     # This function prints out the board that it was passed.
  7.
  8.     # We decided to ignore the number 0 as you can see.



  print('   |   |')
 10.     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
 11.     print('   |   |')
 12.     print('-----------')
 13.     print('   |   |')
 14.     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
 15.     print('   |   |')
 16.     print('-----------')
 17.     print('   |   |')
 18.     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
 19.     print('   |   |')
