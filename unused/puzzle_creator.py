import random

board = [[0 for i in range(9)] for j in range(9)]
number_list = [1,2,3,4,5,6,7,8,9]
random.shuffle(number_list)
board[0] = number_list

def unsolve(bo,limits,dp_board = []):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            dp_board.append((i,j))
    num_unfilled = 81 - random.randint(limits[0],limits[1])
    unfill = random.sample(dp_board, num_unfilled)
    for pos in unfill:
        bo[pos[0]][pos[1]] = '  '
    return list(set(dp_board) - set(unfill)),unfill
    


def generate_sudoku(bo):
    find = find_empty(bo,0)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        j = random.randint(1,9)
        if valid(bo, j, (row, col)): 
            bo[row][col] = j

            if solve(bo):
                return True

            else:
                bo[row][col] = 0 

    return False

def solve(bo):
    find = find_empty(bo,0)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(bo, i, (row, col)): 
            bo[row][col] = i

            if solve(bo):
                return True

            else:
                bo[row][col] = 0 

    return False

def valid(bo, num, pos):    
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and i != pos[1]:
            return False

    # Check col
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and i != pos[0]:
            return False 
    
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3): 
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    
    return True

def find_empty(bo,x):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == x:
                return (i, j)  # row, col

    return None

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0: 
            print("- - - - - - - - - - - - -")

        for j in range(len(bo[0])): 
            if j % 3 == 0 and j != 0: 
                print(" | ", end="")

            if j == 8:
                print(bo[i][j]) 
            else:
                print(str(bo[i][j])+ " ", end="")
