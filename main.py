import random


def print_board_with_numbers_and_player_and_score_and_move(board):
    for row in board:
        print(row)
    print()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                print(" ", end=" ")
            elif board[row][col] == 1:
                print("X", end=" ")
            elif board[row][col] == 2:
                print("O", end=" ")
        print()
    print()
    print("Score:")
    print("X:", score[0])
    print("O:", score[1])
    print()
    print("Move:", move)
    print()


board = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
score = [0, 0]
move = 0


def check_if_game_is_over(board):
    for row in board:
        if 0 in row:
            return False
    return True


def check_if_player_won(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(len(board[0])):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def check_if_player_won_or_tie(board, player):
    if check_if_player_won(board, player):
        return True
    if check_if_game_is_over(board):
        return True
    return False


def check_if_player_won_or_tie_and_print_board(board, player):
    if check_if_player_won_or_tie(board, player):
        print_board_with_numbers_and_player_and_score_and_move(board)
        print("Player", player, "won!")
        return True
    if check_if_game_is_over(board):
        print_board_with_numbers_and_player_and_score_and_move(board)
        print("Tie!")
        return True
    return False


def check_if_player_won_or_tie_and_print_board_and_return_score(board, player):
    if check_if_player_won_or_tie(board, player):
        print_board_with_numbers_and_player_and_score_and_move(board)
        print("Player", player, "won!")
        return score[player - 1]
    if check_if_game_is_over(board):
        print_board_with_numbers_and_player_and_score_and_move(board)
        print("Tie!")
        return 0
    return False


def check_if_player_won_or_tie_and_print_board_and_return_score_and_move(board, player):
    if check_if_player_won_or_tie(board, player):
        print_board_with_numbers_and_player_and_score_and_move(board)
        print("Player", player, "won!")
        return score[player - 1], move
    if check_if_game_is_over(board):
        print_board_with_numbers_and_player_and_score_and_move(board)
        print("Tie!")
        return 0, move
    return False


def check_if_player_won_or_tie_and_print_board_and_return_score_and_move_and_board_and_player(board, player):
    if check_if_player_won_or_tie(board, player):
        print_board_with_numbers_and_player_and_score_and_move(board)
        print("Player", player, "won!")
        return score[player - 1], move, board, player
    if check_if_game_is_over(board):
        print_board_with_numbers_and_player_and_score_and_move(board)
        print("Tie!")
        return 0, move, board, player
    return False


while True:
    print_board_with_numbers_and_player_and_score_and_move(board)
    print("Player", move % 2 + 1, "to play")
    print()
    print("Enter row and column:")
    row = int(input("Row: ")) - 1
    col = int(input("Column: ")) - 1
    if board[row][col] != 0:
        print("Invalid move!")
        continue
    board[row][col] = move % 2 + 1
    move += 1
    if move % 2 == 0:
        print("Computer's turn")
        print()
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if board[row][col] == 0:
                board[row][col] = move % 2 + 1
                break
        if check_if_player_won_or_tie_and_print_board_and_return_score_and_move_and_board_and_player(board, move % 2 + 1):
            break
        move += 1
    else:
        print("Your turn")
        print()
        while True:
            row = int(input("Row: ")) - 1
            col = int(input("Column: ")) - 1
            if board[row][col] == 0:
                board[row][col] = move % 2 + 1
                break
        if check_if_player_won_or_tie_and_print_board_and_return_score_and_move_and_board_and_player(board, move % 2 + 1):
            break
        move += 1



