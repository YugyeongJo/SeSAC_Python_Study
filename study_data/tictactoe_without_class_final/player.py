from random import randint 
import random

def random_player(x_or_o, x_positions, o_positions):
    move = (0, 0)
    while move in x_positions + o_positions:
        x = randint(0, 2)
        y = randint(0, 2)
        move = (x, y)
    return move 

def smart_player(x_or_o, x_positions, o_positions):
    move = (1, 1)
    unavailable = x_positions + o_positions
    board_table = [(0,0), (1,0), (2,0), (0,1), (1,1), (2,1),(0,2), (1,2), (2,2)]
    sides = [(0,0),(2,0),(0,2),(2,2)]
    not_sides = [(1,0),(0,1),(2,1),(1,2)]
    
    if move not in unavailable:
        return move
        
    while move in unavailable:
        
        for remove_positions in unavailable:
            if remove_positions in board_table:
                board_table.remove(remove_positions)
                
        if move in x_positions : 
            if len(o_positions) == 1:
                if o_positions[0] in not_sides:
                    move = tuple(0 if x == 1 else x for x in o_positions[0])
                else: 
                    move = random.choice(board_table)
            else: 
                move = random.choice(board_table)
    
        if move in o_positions : 
            if len(o_positions) == 1:
                if o_positions[0] in not_sides:
                    move = tuple(0 if x == 1 else x for x in o_positions[0])
                else: 
                    move = random.choice(board_table)
            else: 
                move = random.choice(board_table)
        return move
