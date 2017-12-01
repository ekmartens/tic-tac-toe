
start_board = "1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9"

win_p1 = ["x | x | x\n4 | 5 | 6\n7 | 8 | 9", "1 | 2 | 3\nx | x | x\n7 | 8 | 9", "1 | 2 | 3\n4 | 5 | 6\nx | x | x","x | 2 | 3\nx | 5 | 6\nx | 8 | 9", "1 | x | 3\n4 | x | 6\n7 | x | 9", "1 | 2 | x\n4 | 5 | x\n7 | 8 | x", "x | 2 | 3\n4 | x | 6\n7 | 8 | x", "1 | 2 | x\n4 | x | 6\nx | 8 | 9"]


win_p2 = ["O | O | O\n4 | 5 | 6\n7 | 8 | 9", "1 | 2 | 3\nO | O | O\n7 | 8 | 9", "1 | 2 | 3\n4 | 5 | 6\nO | O | O","O | 2 | 3\nO | 5 | 6\nO | 8 | 9", "1 | O | 3\n4 | O | 6\n7 | O | 9", "1 | 2 | O\n4 | 5 | O\n7 | 8 | O", "O | 2 | 3\n4 | O | 6\n7 | 8 | O", "1 | 2 | O\n4 | O | 6\nO | 8 | 9"]

def player_move(player, board):
    if player == 1:
        move = str(input('Player 1, enter a cell...'))
        for i in board:
            if i == move:
                new_board = board.replace(i, 'x')
        print new_board
        if new_board[0] == 'x' and new_board[4] == 'x' and new_board[8] == 'x':
            print 'Player 1 Wins!'
        elif new_board[0] == 'x' and new_board[4] == 'x' and new_board[8] == 'x':
            print 'Player 1 Wins!'
        elif new_board[10] == 'x' and new_board[14] == 'x' and new_board[18] == 'x':
            print 'Player 1 Wins!'
        elif new_board[20] == 'x' and new_board[24] == 'x' and new_board[28] == 'x':
            print 'Player 1 Wins!'
        elif new_board[0] == 'x' and new_board[10] == 'x' and new_board[20] == 'x':
            print 'Player 1 Wins!'
        elif new_board[4] == 'x' and new_board[14] == 'x' and new_board[24] == 'x':
            print 'Player 1 Wins!'
        elif new_board[8] == 'x' and new_board[18] == 'x' and new_board[28] == 'x':
            print 'Player 1 Wins!'
        elif new_board[0] == 'x' and new_board[14] == 'x' and new_board[28] == 'x':
            print 'Player 1 Wins!'
        elif new_board[8] == 'x' and new_board[14] == 'x' and new_board[20] == 'x':
            print 'Player 1 Wins!'
        elif new_board[0] != '1' and new_board[4] != '2' and new_board[8] != '3' and new_board[10] != '4' and new_board[14] != '5' and new_board[18] != '6' and new_board[20] != '7' and new_board[24] != '8' and new_board[28] != '9':
            print 'Draw!'
        else:
            player = 2
            player_move(2, new_board)
    else:
        move = str(input('Player 2, enter a cell...'))
        for i in board:
            if i == move:
                new_board = board.replace(i, 'o')
        print new_board
        if new_board[0] == 'o' and new_board[4] == 'o' and new_board[8] == 'o':
            print 'Player 2 Wins!'
        elif new_board[10] == 'o' and new_board[14] == 'o' and new_board[18] == 'o':
            print 'Player 2 Wins!'
        elif new_board[20] == 'o' and new_board[24] == 'o' and new_board[28] == 'o':
            print 'Player 2 Wins!'
        elif new_board[0] == 'o' and new_board[10] == 'o' and new_board[20] == 'o':
            print 'Player 2 Wins!'
        elif new_board[4] == 'o' and new_board[14] == 'o' and new_board[24] == 'o':
            print 'Player 2 Wins!'
        elif new_board[8] == 'o' and new_board[18] == 'o' and new_board[28] == 'o':
            print 'Player 2 Wins!'
        elif new_board[0] == 'o' and new_board[14] == 'o' and new_board[28] == 'o':
            print 'Player 2 Wins!'
        elif new_board[8] == 'o' and new_board[14] == 'o' and new_board[20] == 'o':
            print 'Player 2 Wins!'
        elif new_board[0] != '1' and new_board[4] != '2' and new_board[8] != '3' and new_board[10] != '4' and new_board[14] != '5' and new_board[18] != '6' and new_board[20] != '7' and new_board[24] != '8' and new_board[28] != '9':
            print 'Draw!'
        else:
            player = 1
            player_move(1, new_board)

print start_board
player_move(1, start_board)
