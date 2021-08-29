### 
# Sudoku solver 
###

# Functions 
# - Print board
# - Find empty 
# - Test valid and backtrack 
# - Recursive 

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)): 
        if i % 3 == 0 and i != 0: 
            print("- - - - - - - - - - - - ")
        
        for j in range(len(bo[0])): 
            if j % 3 == 0 and j != 0: 
                print(" | ", end="") # printing each row so dont want next line
                
            if j == 8: # if at last position 
                print(bo[i][j])
            else: 
                print(str(bo[i][j]) + " ", end="")
                
def find_empty(bo):
    for i in range(len(bo)): # len first col, loop over rows
        for j in range(len(bo[0])): # len first row, loop over columns 
            if bo[i][j] == 0:
                return (i, j) # row, col
    return None
