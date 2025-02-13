import math
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

def init_board():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_board_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

def check_winner(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def alpha_beta(board, depth, alpha, beta, maximizing_player):
    if check_winner(board, PLAYER_X):
        return -10 + depth
    if check_winner(board, PLAYER_O):
        return 10 - depth
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = alpha_beta(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = alpha_beta(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                move_val = alpha_beta(board, 0, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

def play_game():
    board = init_board()
    current_player = PLAYER_X

    while True:
        print_board(board)
        if current_player == PLAYER_X:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
        else:
            print("AI is making a move...")
            row, col = find_best_move(board)

        if board[row][col] == EMPTY:
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()
