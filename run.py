# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#https://www.youtube.com/watch?v=tF1WRCrd_HQ Used this video for guidance

"""
Issues to sort. 
- The differntiation between sunk ships and hits is not working. The message displays that a ship is sunk, even when the 
  ship has been hit and not sunk. Need to fix this. 
- There is still an issue with ship numbers and the small board. Only appears to be two ships each time. Make the opponent board 
  visible to test and see what can be done to fix it.
- Add the response for invalid choice if player doesnt select 1 or 2 in the difficulty selection


"""

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

#Function for difficulty selection !! ADD RESPONSE FOR INVALID CHOICE!!
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

from random import randint, choice

def can_place_ship(board, row, col, ship_size, direction):
    if direction == 'horizontal':
        if col + ship_size > len(board[0]):
            return False
        for i in range(ship_size):
            if board[row][col + i] == 'X':
                return False
    else:  # direction == 'vertical'
        if row + ship_size > len(board):
            return False
        for i in range(ship_size):
            if board[row + i][col] == 'X':
                return False
    return True

def place_ship(board, row, col, ship_size, direction):
    if direction == 'horizontal':
        for i in range(ship_size):
            board[row][col + i] = 'X'
    else:  # direction == 'vertical'
        for i in range(ship_size):
            board[row + i][col] = 'X'

def create_ships(board, board_size, ship_sizes):
    for ship_size in ship_sizes:
        placed = False
        while not placed:
            row = randint(0, board_size - 1)
            col = randint(0, board_size - 1)
            direction = choice(['horizontal', 'vertical'])
            if can_place_ship(board, row, col, ship_size, direction):
                place_ship(board, row, col, ship_size, direction)
                placed = True

"""

def create_ships(board, board_size, ship_sizes):
    for ship_size in ship_sizes:
        placed = False
        while not placed: 
            vertical = randint(0,1) == 0 
            if vertical: 
                row = randint(0, board_size, - ship_size)
                col = randint(0, board_size - 1)
                empty = all(board[row + i][col] == ' ' for i in range(ship_size))
                if empty: 
                    for i in range(ship_size):
                        board[row + i][col] = 'X'
                    placed = True
            else:  
                row = randint(0, board_size - 1)
                col = randint(0, board_size - ship_size)
                empty = all(board[row][col + i] == ' ' for i in range(ship_size))
                if empty:
                    for i in range(ship_size):
                        board[row][col + i] = 'X'
                    placed = True

"""

"""
Code from previous function to set ships on the board. Keep in case new code doesn't work. Delete before I submit if it works!!
    for ship in range(6):
        ship_row, ship_column = randint(0, board_size - 1), randint(0, board_size - 1)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, board_size - 1), randint(0, board_size - 1)
        board[ship_row][ship_column] = 'X'

"""

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

ship_sizes_for_game = ship_sizes[difficulty]


#create boards
RED_BOARD = [[' '] * board_size for _ in range(board_size)]
BLUE_BOARD = [[' '] * board_size for _ in range(board_size)]

# Set ships on opponent board 
create_ships(RED_BOARD, board_size, ship_sizes_for_game)

#Game loop 

turns = 30 
prev_sunk_ships = 0
while turns > 0:
    print('Prepare for Battleships')
    show_board(BLUE_BOARD, board_size)
    row, column = get_target_location(board_size)
    if BLUE_BOARD[row][column] == '-':
        print('Select another target location. You already aimed there')
    elif RED_BOARD[row][column] == 'X':
        print ('Congratulations You hit a battleship')
        BLUE_BOARD[row][column] = 'X'
        turns -= 1
        #checking to see if the hit managed to sink a ship
        current_sunk_ships = sunk_ships(BLUE_BOARD)
        sunk_this_turn = current_sunk_ships > prev_sunk_ships
        if sunk_this_turn:
            print("Congratulations. You sunk a battleship!")
            prev_sunk_ships = current_sunk_ships 
        if current_sunk_ships == 6:
            print("Congratulations You Sunk All Of Your Opponent's Battleships")
            break     
    else: 
        print('You missed! :(')
        BLUE_BOARD[row][column] = '-'
        turns -= 1
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('You Have No More Turns - Game Over')
        break


