board = [[1,2,3], [4,5,6], [7,8,9]]
for row in board:
    print(row)

space1 = board[0][0]
space2 = board[0][1]
space3 = board[0][2]
space4 = board[1][0]
space5 = board[1][1]
space6 = board[1][2]
space7 = board[2][0]
space8 = board[2][1]
space9 = board[2][2]

move1 = (int(input('Player X, make your move...')))

def move(player, board, location):
    while move1 == 1:
        space1 = 'X'
        print(board)
    
move()