# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint

letters_to_numbers = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9}

#Difficulty Level. Needs to be a variable accessible throughtout game so has to come early on in code. Check and see if this works later.
ship_sizes = {
    'easy': [3, 3, 2, 2, 1, 1],  
    'hard': [1, 1, 1, 1, 1, 1] 
}

#Function to allow user to change size of board.
def choose_board_size(): 
    print("Choose Board Size:")
    print("1. Small 5x5")
    print("2. Medium 8x8")
    print("3. Large 10x10")
    choice = input ("Enter choice (1-3): ")
    if choice == '1':
        return 5 
    elif choice == '2':
        return 8
    elif choice == '3':
        return 10
    else: 
        print ("Your Choice Wasn't Valid. Defauting to a small board.")
        return 5 

#Function for difficulty selection 
def choose_difficulty():
    print("Select Difficulty:")
    print("1. Easy (Ships occupy more squares)")
    print("2. Hard (Ships occupy one square each)")
    choice = input("Enter choice (1-2): ")
    if choice == '1':
        return 'easy'
    elif choice == '2':
        return 'hard'
    else:
        print("Invalid choice. Defaulting to Easy.")
        return 'easy'

#Global Variable for the opponent's hidden board
#RED_BOARD = [[' '] * 10 for x in range(10)]
#Global variable for the user's visible board to track their guesses
#BLUE_BOARD = [[' '] * 10 for x in range(10)]

def show_board(board, board_size):
    row_number = 1
    if board_size == 10:
        print ('   A B C D E F G H I J')
        print ('   -------------------')
    elif board_size == 8:
        print ('   A B C D E F G H')
        print ('   ---------------')
    else:
        print ('   A B C D E')
        print ('   ---------')

   
   # row_number = 1 was after code but have put before to see if it works. 

    for row in board: 
        print("%2d|%s|" % (row_number, "|".join(row)))
        row_number += 1

"""
Function to show board. Letter headings displayed for colmuns and number rows. The rows and columns are separated by pipe symbols
"""

def create_ships(board, board_size, ship_sizes):
    for ship in range(6):
        ship_row, ship_column = randint(0, board_size - 1), randint(0, board_size - 1)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, board_size - 1), randint(0, board_size - 1)
        board[ship_row][ship_column] = 'X'

"""
EDITED FUNCTION TO TARGET ON VARIED SIZED BOARDS

"""

def get_target_location(board_size):
    row = input(f'Enter a row number to target (1-{board_size}): ')
    while not row.isdigit() or not 1 <= int(row) <= board_size:
        print('Enter a valid row number')
        row = input(f'Enter a row number to target (1-{board_size}): ')
    column = input(f'Enter a column letter to target (A-{chr(ord("A") + board_size - 1)}): ').upper()
    while len(column) != 1 or column < 'A' or column > chr(ord("A") + board_size - 1):
        print('Enter a valid column letter')
        column = input(f'Enter a column letter to target (A-{chr(ord("A") + board_size - 1)}): ').upper()

    return int(row) - 1, letters_to_numbers[column]




"""
Set loaction of ships. NB There is a bug in this section, wrap in try except otherwise it wont work with no input
"""

"""

INITIAL FUNCTION FOR TARGETTING SHIPS --> LIMITED TO ONE BOARD SIZE. 
def get_target_location():
    row = input ('Enter a row number to target: ')
    while row not in '12345678910':
        print ('Enter a Valid Row')
        row = input ('Enter a row number to target 1-10')
    column = input ('Enter a column letter to target A-J').upper()
    while column not in 'ABCDEFGHIJ':
        print ('Enter a Valid Column')
        column = input ('Enter a column letter to target A-J').upper()
    return int(row) - 1, letters_to_numbers[column]


-----

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

board_size = choose_board_size()

difficulty = choose_difficulty()

#create boards
RED_BOARD = [[' '] * board_size for _ in range(board_size)]
BLUE_BOARD = [[' '] * board_size for _ in range(board_size)]

# Set ships on opponent board 
create_ships(RED_BOARD, board_size)

#Game loop 

turns = 15 
while turns > 0:
    print('Prepare for Battleships')
    show_board(BLUE_BOARD, board_size)
    row, column = get_target_location(board_size)
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


