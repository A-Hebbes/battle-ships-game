# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint

#Global Variable for the opponent's hidden board
RED_BOARD = [[' '] * 10 for x in range(10)]
#Global variable for the user's visible board to track their guesses
BLUE_BOARD = [[' '] * 10 for x in range(10)]


letters_to_numbers = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9}

def show_board(board):
    print ('   A B C D E F G H I J')
    print ('   -------------------')
    row_number = 1
    for row in board: 
        print("%2d|%s|" % (row_number, "|".join(row)))
        row_number += 1

"""
Function to show board. Letter headings displayed for colmuns and number rows. The rows and columns are separated by pipe symbols
"""

def create_ships(board):
    for ship in range(6):
        ship_row, ship_column = randint(0,9), randint(0,9)
        while board[ship_row][ship_column]=='X':
            ship_row, ship_column = randint(0,9), randint(0,9)
        board[ship_row][ship_column] = 'X'

"""
Set loaction of ships. NB There is a bug in this section, wrap in try except otherwise it wont work with no input
"""

def get_target_location():
    row = input ('Enter a row number to target 1-11')
    while row not in '1234567891011':
        print ('Enter a Valid Row')
        row = input ('Enter a row number to target 1-11')
    column = input ('Enter a column letter to target A-J').upper()
    while column not in 'ABCDEFGHIJ':
        print ('Enter a Valid Column')
        column = input ('Enter a column letter to target A-J').upper()
    return int(row) - 1, letters_to_numbers[column]

"""
function to ask player for the target
"""

def strike_success():
    pass

"""
display if strike was successful
"""

def sunk_ships(board):
    count = 0 
    for row in board:
        for column in row:
           if column == 'X':
            count += 1
    return count 

"""
Shows how many ships have been sunk
"""

create_ships(RED_BOARD)
turns = 15 
while turns > 0:
    print('Prepare for Battleships')
    show_board(BLUE_BOARD)
    row, column = get_target_location()
    if BLUE_BOARD[row][column] == '-':
        print('Select another target location. You already aimed there')
    elif RED_BOARD[row][column] == 'X':
        print ('Congratulations You Sunk a Battleship')
        BLUE_BOARD[row][column] = 'X'
        turns -= 1
    else: 
        print('You missed! :(')
        BLUE_BOARD[row][column] = '-'
        turns -= 1
    if sunk_ships(BLUE_BOARD) == 6:
        print("Congratulations You Sunk All Of Your Opponent's Battleships")
        break
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('You Have No More Turns - Game Over')
        break

