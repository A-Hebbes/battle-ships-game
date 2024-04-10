# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#https://www.youtube.com/watch?v=tF1WRCrd_HQ Used this video for guidance

"""
Issues to sort. 




"""

#Imports 

from random import randint, choice

#Settings for difficulty and game boards

letters_to_numbers = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9}
ship_sizes = {
    'easy': [3, 3, 2, 2, 1, 1],  
    'hard': [1, 1, 1, 1, 1, 1] 
}

#Functions for user choice of game type 

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

#Function for Game Rules 
def display_rules():
    print("Welcome to Battleships!")
    print("Rules:")
    print("- You will be playing against the computer.")
    print("- Your goal is to sink all of your opponent's battleships.")
    print("- You will choose a location on the opponent's board to target.")
    print("- If your shot hits a battleship, it will be marked with 'X'.")
    print("- If your shot misses, it will be marked with '-'.")
    print("- If you make a successful hit, you will activate a sonar to scan adjacent squares")
    print("- The game ends when you sink all of your opponent's battleships or run out of turns.")
    print("\nLet's get started!\n")

#Board Creation and Display 
#--------------------------

#Function for board display

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
    for row in board: 
        print("%2d|%s|" % (row_number, "|".join(row)))
        row_number += 1


#Functions for placement of ships and board initial setup

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


#Functions for game play

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

#FUnction for sonar 

def sonar(board, row, col, board_size):
    sonar_range = 1
    start_row = max(0, row - sonar_range)
    end_row = min(board_size - 1, row + sonar_range)
    start_col = max(0, col - sonar_range)
    end_col = min(board_size - 1, col + sonar_range)
    print("Sonar Results:")
    for r in range(start_row, end_row + 1):
        for c in range(start_col, end_col + 1):
            if board[r][c] == 'X':
                print(f"Ship detected at {r + 1}, {chr(c + 65)}")  
            else:
                print(f"No ship detected at {r + 1}, {chr(c + 65)}")  




#Check if the game is over

def check_game_over(red_board, blue_board):
    total_ships = sum(row.count('X') for row in red_board)
    total_hits = sum(row.count('X') for row in blue_board)
    return total_hits == total_ships

#Game loop 
print("Would you like to read the game rules? (Y/N)")
read_rules = input().upper()
if read_rules == 'Y':
    display_rules()
elif read_rules == 'N':
    pass
else: 
    print("Invalid input. Starting game.")
turns = 30 
while turns > 0:
    print('Prepare for Battleships')
    #change back to BLUE_BOARD AFTER TESTING GAME
    show_board(RED_BOARD, board_size)
    print("---------------")
    row, column = get_target_location(board_size)
    if BLUE_BOARD[row][column] == '-':
        print('Select another target location. You already aimed there')
        print("---------------")
        print("---------------")
    elif RED_BOARD[row][column] == 'X':
        print ('Congratulations You hit a battleship')
        print("---------------")
        print("---------------")
        BLUE_BOARD[row][column] = 'X'
        sonar(RED_BOARD, row, column, board_size)
        turns -= 1
        if check_game_over(RED_BOARD, BLUE_BOARD):
            print("Congratulations! You've sunk all of your opponent's battleships!")
            break
    else: 
        print('You missed! :(')
        print("---------------")
        print("---------------")
        BLUE_BOARD[row][column] = '-'
    turns -= 1
    print('You have ' + str(turns) + ' turns remaining')
    if turns == 0:
        print('You Have No More Turns - Game Over')
        break


