board = "1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9"

def player_move(player, board):
    game_won = False
    if player == 1:
        move = str(input('Player 1, enter a cell...'))
        for i in board:
            if i == move:
                new_board = board.replace(i, 'X')
        print new_board
        while game_won == True:
            #print win message
            print 'Player ' + winner + ' has won!'
            break
        else:
             player = 2
             player_move(2, new_board)

    else:
        move = str(input('Player 2, enter a cell...'))
        for i in board:
            if i == move:
                new_board = board.replace(i, 'O')
        print new_board
        game_won = False
        while game_won == True:
            print 'Player has won!'
            break
        else:
             player = 1
             player_move(1, new_board)

print board
player_move(1, board)
