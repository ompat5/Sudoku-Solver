board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def print_board(bo):
    for i in range(0,9):
        if i % 3 == 0:
            print("-------------------------")

        for j in range(0,9):
            if j % 3 == 0:
                print("| ", end="")

            if j == 8:
                print(str(bo[i][j]) + " |")
            else:
                print(str(bo[i][j]) + " ", end="")
    
    print("-------------------------")

def solve(board):
    find = find_empty(board)
    if find == None:
        return True
    else:
        row, col = find

    for num in range(1,10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)

    return None

def valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for row in range(box_y*3, box_y*3 + 3):
        for col in range(box_x * 3, box_x*3 + 3):
            if board[row][col] == num and (row,col) != pos:
                return False

    return True

print_board(board)
solve(board)
print("___________________")
print_board(board)