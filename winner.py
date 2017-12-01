board = "1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9"
print len(board)
print board[0]
print board[4]
print board[8]
print board[10]
print board[14]
print board[18]
print board[20]
print board[24]
print board[28]
#1 = 0
#2 = 4
#3 = 8
#4 = 10
#5 = 14
#6 = 18
#7 = 20
#8 = 24
#9 = 28
#123 new_board[0] == 'X' and new_board[4] == 'X' and new_board[8] == 'X'
#456 new_board[10] == 'X' and new_board[14] == 'X' and new_board[18] == 'X'
#789 new_board[20] == 'X' and new_board[24] == 'X' and new_board[28] == 'X'
#147 new_board[0] == 'X' and new_board[10] == 'X' and new_board[20] == 'X'
#258 new_board[4] == 'X' and new_board[14] == 'X' and new_board[24] == 'X'
#369 new_board[8] == 'X' and new_board[18] == 'X' and new_board[28] == 'X'
#159 new_board[0] == 'X' and new_board[14] == 'X' and new_board[28] == 'X'
#357 new_board[8] == 'X' and new_board[14] == 'X' and new_board[20] == 'X'
