# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

RED_BOARD = [[' '] * 10 for x in range(11)]
BLUE_BOARD = [[' '] * 10 for x in range(11)]

"""
RED GAME BOARD FOR COMPUTER
BLUE BOARD FOR PLAYER
"""

letters_to_numbers = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9}

def show_board(board):
    print ('A B C D E F G H I J')
    print ('-------------------')
    row_number = 1
    for row in board: 
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

"""
Function to show board. Letter headings displayed for colmuns and number rows. The rows and columns are separated by pipe symbols
"""

def create_ships():
    pass

"""
Set loaction of ships
"""

def get_target_location():
    pass
"""
function to ask player for the target
"""

def strike_success():
    pass

"""
display if strike was successful
"""

def sunk_ships():
    pass

"""
Shows how many ships have been sunk
"""

create_ships()
turns = 15 
