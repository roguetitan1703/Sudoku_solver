
dp_board = None
board = [
    [7,9,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def duplicator(bo,dp_board = [[0 for i in range(9)] for j in range(9)]):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            dp_board[i][j] = bo[i][j]
    
    return dp_board

def solve(bo,dp_board):
    if not dp_board: 
        dp_board = duplicator(bo)
    find = find_empty(dp_board)
    if not find:
        return dp_board
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(dp_board, i, (row, col)): 
            dp_board[row][col] = i

            if solve(bo,dp_board):
                return dp_board

            else:
                dp_board[row][col] = 0 

    return False


def solve_again(bo,dp_board):
    if not dp_board: 
        dp_board = duplicator(bo)
    find = find_empty(dp_board)
    if not find:
        return dp_board
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(dp_board, i, (row, col)): 
            dp_board[row][col] = i

            if solve(bo,dp_board):
                return dp_board

            else:
                dp_board[row][col] = 0 

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

    
def print_board(bo):
    if bo:
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



def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(solve(board,dp_board))
print_board(board) 
