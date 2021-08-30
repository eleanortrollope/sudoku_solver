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


# box (row box = y, col box = x )
# 0,0 | 0,1 | 0,2
# 1,0 | 1,1 | 1,2
# 2,0 | 2,1 | 2,2

def valid(bo, num, pos):
    # Check row, pos[0] = row picked, pos[1] = col picked, if = j value added
    for j in range(len(bo[0])):
        if bo[pos[0]][j] == num and pos[1] != j: 
            return False
        
    # check col 
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
        
    # check square 3x3, determine which box
    box_x = pos[1] // 3 # col = j
    box_y = pos[0] // 3 # row = i
    
    # loop all elements check box 
    for i in range(box_y*3, box_y*3 + 3): # start of box row
        for j in range(box_x*3, box_x*3 + 3): # start of box col
            if bo[i][j] == num and (i,j) != pos:
                return False
    # if makes to end, all check okay, valid position
    return True


# Make solver, recursive = call the function from inside of itself 
# Base case is that bo is full = filled entire board 
# Backtrack = end of board = found solution 
def solve(bo): 
    
    find = find_empty(bo)
    
    if not find: # if find = None => no empty space = found all positions = found solution 
        return True 
    else: 
        row, col = find # returned i, j 
    
    # checking through all values
    for i in range(1,10):
        # try this value inside of our solution 
        if valid(bo, i, (row, col)): # default if its true
            bo[row][col] = i
            
            if solve(bo): # recurvsive
                return True
            
            bo[row][col] = 0 # backtrack and reset 
           
    return False 


print_board(board)
solve(board)
print('=======================')
print_board(board)

