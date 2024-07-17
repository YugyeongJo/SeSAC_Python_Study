game_status = {'x_positions' : [], 'o_positions' : []} 

def empty_board(width_count = 3, length_count = 3):
    """Create an empty board. 

    The board is made of horizontal lines, made with - and vertical lines, made with |. 

    (optional) When there are no x_cell_size and y_cell_size arguments, default to arbitary size of your choice. Just make it consistent. 
    """
    board = ''
    width = "-"
    length = "|"
    for l in range(length_count):
        width_board = ''
        for i in range(width_count):
            width_board += ' ' + width*10
        width_board = width_board+'\n'
        board += width_board

        length_board = ''
        for j in range(length_count):
            for k in range(width_count+1):
                length_board += length + ' '*10
            length_board = length_board + '\n'
        board += length_board
    board += width_board
    print(board)
    return board 

def play(game_status, x_or_o, coordinate):
    """Main function for simulating tictactoe game moves. 

    Tictactoe game is executed by two player's moves. In each move, each player chooses the coordinate to place their mark. It is impossible to place the mark on already taken position. 

    A move in the tictactoe game is composed of two components; whether who ('X' or 'O') made the move, and how the move is made - the coordinate of the move. 

    Coordinate in our tictactoe system will use the coordinate system illustrated in the example below. 
    
    Example 1. 3 * 4 tictactoe board. 
    
         ---------- ---------- ----------
        |          |          |          |
        |  (0,0)   |  (1,0)   |  (2,0)   |
        |          |          |          |
         ---------- ---------- ----------
        |          |          |          |
        |  (0,1)   |  (1,1)   |  (2,1)   |
        |          |          |          |
         ---------- ---------- ----------
        |          |          |          |
        |  (0,2)   |  (1,2)   |  (2,2)   |
        |          |          |          |
         ---------- ---------- ----------
        |          |          |          |
        |  (0,3)   |  (1,3)   |  (2,3)   |
        |          |          |          |
         ---------- ---------- ----------
        """
    if coordinate in game_status['x_positions'] or coordinate in game_status['o_positions']:
        raise ValueError(f'You can\'t use {coordinate}')
        
    if x_or_o == 'X':
        game_status['x_positions'].append(coordinate)
    else: 
        game_status['o_positions'].append(coordinate) 

def check_winlose(game_status):
    """Check the game status; game status should be one of 'X wins', 'O wins', 'tie', 'not decided'. 
    """
    winning_combinations = []
    # 가로 줄
    for i in range(0, 3):
        winning_combinations.append(tuple((i, j) for j in range(0, 3)))

    # 세로 줄
    for j in range(0, 3):
        winning_combinations.append(tuple((i, j) for i in range(0, 3)))

    # 대각선 줄
    winning_combinations.append(((0, 0), (1, 1), (2, 2)))
    winning_combinations.append(((0, 2), (1, 1), (2, 0)))
    
    for win in winning_combinations:
        if win[0] in game_status['x_positions'] and win[1] in game_status['x_positions'] and win[2] in game_status['x_positions']:
            return print('X wins')
        elif win[0] in game_status['o_positions'] and win[1] in game_status['o_positions'] and win[2] in game_status['o_positions']:
            return print('O wins')
    if len(game_status['x_positions']) + len(game_status['o_positions']) == 9:
        return 'Tie'
    else:
        return 'Not decided'

def display(game_status):
    """Display the current snapshot of the board. 

    'Snapshot' should contain following components. 

    - The board itself 
    - Moves that are already made

    For clarification, see provided examples. 

    Example 1. 
    When TictactoeGame instance t have following attributes; 
    - x_positions = [(0,0), (2,0), (2,1), (1,2)]
    - o_positions = [(1,0), (1,1), (0,2), (2,2)]

    t.display()
    >> 
     ---------- ---------- ----------
    |          |          |          |
    |    X     |    O     |    X     |
    |          |          |          |
     ---------- ---------- ----------
    |          |          |          |
    |          |    O     |    X     |
    |          |          |          |
     ---------- ---------- ----------
    |          |          |          |
    |    O     |    X     |    O     |
    |          |          |          |
     ---------- ---------- ----------

    """
    pass 

if __name__ == '__main__':
    print(play(game_status, 'X', (1, 1)))
    print(check_winlose(game_status))
    print(play(game_status, 'O', (1, 2)))
    print(check_winlose(game_status))
    print(play(game_status, 'X', (2, 2)))
    print(check_winlose(game_status))
    print(play(game_status, 'O', (0, 2)))
    print(check_winlose(game_status))
    print(play(game_status, 'X', (0, 0)))
    print(check_winlose(game_status))