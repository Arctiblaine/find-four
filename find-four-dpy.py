ff_board = [[':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:']]

ff_player = 'Player 1'

def ff_valid_moves(board):
    valid = []
    for row in board:
        for slot in row:
            if slot == ':black_circle:':
                valid.append(slot)

    return valid

def ff_is_valid_move(board, pos):
    if pos < 0 or pos > 6:
        return False
    else:
        sample = board[0][pos]
        if sample == ':red_circle:' or sample == ':blue_circle:':
            return False

    return True

def ff_is_game_over(L):
    h, w = len(L), len(L[0])
    diags = [[L[h-1-q][p-q] for q in range(min(p, h-1), max(0, p-w+1)-1, -1)] for p in range(h+w-1)]
    anti_diags = [[L[p - q][q] for q in range(max(p-h+1,0), min(p+1, w))] for p in range(h + w - 1)]
    horiz = L
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

    if type(search(diags)) is not bool:
        return search(diags)
    elif type(search(anti_diags)) is not bool:
        return search(anti_diags)
    elif type(search(horiz)) is not bool:
        return search(horiz)
    else:
        if type(search(vert)) is not bool:
            return search(vert)

    return False

def search(config):
    for row in config:
        n = 0
        while n < len(row):
            for i in range(len(row)):
                if len(row[n:i+1]) == 4:
                    if row[n:i+1] == [':red_circle:', ':red_circle:', ':red_circle:', ':red_circle:']:
                        return 'Player 1 won!'
                    elif row[n:i+1] == [':blue_circle:', ':blue_circle:', ':blue_circle:', ':blue_circle:']:
                        return 'Player 2 won!'
                    
            n += 1

    return False

def ff_move(board, pos, player):
    if player == 'Player 1':
        puck = ':red_circle:'
    else:
        puck = ':blue_circle:'

    i = -1
    MAX = -7
    while i > MAX:
        if board[i][pos] == ':black_circle:':
            board[i][pos] = puck
            break

        i -= 1
        
    return board

@bot.command()
async def ff(ctx, pos=''):
    global ff_board
    global ff_player

    try:
        if pos == '':
            embed = discord.Embed(title = "Board", description = "|--------------------------------------|", color=0x45F4E9)
            embed.add_field(name = "| :zero: | :one: | :two: | :three: | :four: | :five: | :six: |", value = "|=======================|", inline = False)
            for row in ff_board:
                sect = '| ' + ' | '.join(row) + ' |'
                embed.add_field(name = sect, value = '|--------------------------------------|', inline = False)
            await ctx.send(embed=embed)
            return
        if pos == 'reset':
            ff_board = [[':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
            [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
            [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
            [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
            [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
            [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:']]
            await ctx.send('The board has been reset.')
            return ff_board
        pos = int(pos)
    except ValueError:
        await ctx.send('Sorry, only numbers are allowed.')
        return

    if ff_is_valid_move(ff_board, pos):
        msg = ff_player + ' entered index ' + str(pos)
        await ctx.send(msg)
        if ff_player == 'Player 1':
            ff_move(ff_board, pos, ff_player)
            ff_player = 'Player 2'
        else:
            ff_move(ff_board, pos, ff_player)
            ff_player = 'Player 1'

        embed = discord.Embed(title = "Board", description = "|--------------------------------------|", color=0x45F4E9)
        embed.add_field(name = "| :zero: | :one: | :two: | :three: | :four: | :five: | :six: |", value = "|=======================|", inline = False)
        for row in ff_board:
            sect = '| ' + ' | '.join(row) + ' |'
            embed.add_field(name = sect, value = '|--------------------------------------|', inline = False)
        await ctx.send(embed=embed)

        is_game_won = ff_is_game_over(ff_board)
        if type(is_game_won) is not bool:
            await ctx.send(is_game_won)
            ff_board = [[':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:']]
            await ctx.send('The board has been reset.')
            return ff_board

        if len(valid) == 0:
            await ctx.send('No one won. Resetting the board...')
            ff_board = [[':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:'],
             [':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:', ':black_circle:']]
            return ff_board
            

        msg = 'It is ' + player + "'s turn."
        await ctx.send(msg)
        return ff_player
    
    if not ff_is_valid_move(ff_board, pos):
        await ctx.send('That move is either out of bounds or occupied. Try again.')
