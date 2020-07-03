'''
    Archie's Find Four program
    7/1/2020
'''
def valid_moves(board):
    valid = []
    for row in board:
        for slot in row:
            if slot == ' ':
                valid.append(slot)

    return valid

def is_valid_move(board, pos):
    if pos < 0 or pos > 6:
        return False
    else:
        sample = board[0][pos]
        if sample == 'R' or sample == 'B':
            return False

    return True

def print_board(board):
    print('|---------------------------|')
    print('| 0 | 1 | 2 | 3 | 4 | 5 | 6 |')
    print('|===========================|')
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
        print('|---------------------------|')
    print('|                           |')


def is_game_over(L):
    # get all types of different searches first
    # get ALL diags.
    h, w = len(L), len(L[0])
    diags = [[L[h-1-q][p-q] for q in range(min(p, h-1), max(0, p-w+1)-1, -1)] for p in range(h+w-1)]
    anti_diags = [[L[p - q][q] for q in range(max(p-h+1,0), min(p+1, w))] for p in range(h + w - 1)]
    # get horiz (which is just board)
    horiz = L
    # get vertical/all rows
    i = 0
    j = 0
    vert = []
    while i < w:
        column = []
        while j < h:
            column.append(L[j][i])
            j += 1

        j = 0
        i += 1
        vert.append(column)

    if search(diags):
        return True
    elif search(anti_diags):
        return True
    elif search(horiz):
        return True
    else:
        if search(vert):
            return True

    return False

def search(config):
    for row in config:
        n = 0
        while n < len(row):
            for i in range(len(row)):
                if len(row[n:i+1]) == 4:
                    if row[n:i+1] == ['R', 'R', 'R', 'R']:
                        print('Player 1 won!')
                        return True
                    elif row[n:i+1] == ['B', 'B', 'B', 'B']:
                        print('Player 2 won!')
                        return True
                    
            n += 1

    return False

def move(board, pos, player):
    if player == 'Player 1':
        puck = 'R'
    else:
        puck = 'B'

    i = -1
    MAX = -7
    while i > MAX:
        if board[i][pos] == ' ':
            board[i][pos] = puck
            break

        i -= 1
        
    return board

def main():
    is_game_won = False

    board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

    player = 'Player 1'
    print_board(board)
    valid = valid_moves(board)
    while not is_game_won:
        try:
            pos = int(input(player + ' enter index: '))
        except ValueError:
            print('Invalid input.')
            continue

        if is_valid_move(board, pos):
            if player == 'Player 1':
                move(board, pos, player)
                player = 'Player 2'
            else:
                move(board, pos, player)
                player = 'Player 1'

            is_game_won = is_game_over(board)
            valid = valid_moves(board)
            if len(valid) == 0:
                print('No one won.')
                break

        print_board(board)

if __name__ == '__main__':
    main()
             
