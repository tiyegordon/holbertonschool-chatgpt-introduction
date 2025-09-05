def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)

def check_winner(board):
    # rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return row[0]
    # cols
    for c in range(len(board[0])):
        if board[0][c] != " " and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]
    # diagonals
    if board[1][1] != " ":
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
    return None  # no winner yet

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0

    while True:
        print_board(board)

        # input with validation
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Please enter numbers 0, 1, or 2.\n")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Out of bounds. Use 0, 1, or 2.\n")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.\n")
            continue

        # make move
        board[row][col] = player
        moves += 1

        # check winner RIGHT AFTER the move (before toggling)
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # draw
        if moves == 9:
            print_board(board)
            print("It's a draw!")
            break

        # toggle player
        player = "O" if player == "X" else "X"

tic_tac_toe()

