def print_board(board) : 
    print_board("---------")
    for n in range(3):
        print("|", end="")
        for m in range(3):
            print(" " + board[n][m] + "|", end="")
        print("\n---------")

def check_win(board, player):
    # Check rows
    for n in range(3):
        if board [0][n] == player and board[n][1]== player and board[n][2] == player:
            return True
    # Check diagonals
    if board [0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board [0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False
def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " "," ",]]
    players = ["x", " O"]
    current_player = players[0]
    print_board(board)
    while True:
        row = int(input("Enter row (0-2)for" + current_player + ": "))
        col = int(input("Enter column (0-2) for" + current_player + ": "))
        if board[row][col]==" ":
            board[row][col]== current_player
            if check_win(board):
                print_board(board)
                print(current_player + "wins!")
                break
            if check_win(board):
                print_board(board)
                print("Tie game!")
                break
          
