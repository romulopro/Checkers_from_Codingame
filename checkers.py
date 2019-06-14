import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def get_possible_next_move(pos_of_piece, list_of_board_lines, my_color):
    # position of piece(line(1 to 8), column(1 to 8), next line
    #is_king_piece true or false
    #set columns nums to lines
    
    if my_color.lower() == 'b':
        next_pos = 1
    else:
        next_pos = -1 
        
    next_line = list_of_board_lines[pos_of_piece[1] + next_pos]
    previous_line = list_of_board_lines[pos_of_piece[1] - next_pos]   
    char_of_colums = '-ABCDEFGH-'
    print(my_color, file = sys.stderr)
    get_moves = []
    #process all empty spaces moves for line 1-8
    '''first tuple =colum
    second tuple element - line'''
    #get pos to string
    init_piece_pos_string = char_of_colums[pos_of_piece[0]] + str(pos_of_piece[1])
    if next_line[pos_of_piece[0] + 1] == '.' :
        get_moves.append(init_piece_pos_string + char_of_colums[pos_of_piece[0] + 1] + str(pos_of_piece[1] + next_pos))
    if next_line[pos_of_piece[0] - 1] == '.' :
        get_moves.append(init_piece_pos_string + char_of_colums[pos_of_piece[0] - 1] + str(pos_of_piece[1] + next_pos))
    #process empty space for king pieces
    if my_color.isupper():
        print('the king', file = sys.stderr)
        if previous_line[pos_of_piece[0] + 1] == '.' :
            get_moves.append(init_piece_pos_string + char_of_colums[pos_of_piece[0] + 1] + str(pos_of_piece[1] - next_pos))
        if previous_line[pos_of_piece[0] - 1] == '.' :
            get_moves.append(init_piece_pos_string + char_of_colums[pos_of_piece[0] - 1] + str(pos_of_piece[1] - next_pos))
    #print(get_moves, file = sys.stderr)        
    return get_moves



#jump forward
def get_possible_jump(pos_of_piece, list_of_board_lines, my_color):
    list_of_jumps = [] # a list of tuples with 2 tuples each
    count = 0
    pos_of_piece = pos_of_piece
    if my_color.lower() == 'b':
        next_pos = 1
    else:
        next_pos = -1 
    #getting isolated single 
    print(pos_of_piece, 'jump loop', file = sys.stderr)
    while (len(list_of_jumps) >= count):
        #check jump forward left   
        if list_of_board_lines[pos_of_piece[1]+next_pos][pos_of_piece[0]-1].lower() == enemy_color:
            if list_of_board_lines[pos_of_piece[1]+2*next_pos][pos_of_piece[0]-2] == '.':
                list_of_jumps.append((pos_of_piece, (pos_of_piece[0]-2,pos_of_piece[1]+2*next_pos)))
        #check jump forward right
        if list_of_board_lines[pos_of_piece[1]+next_pos][pos_of_piece[0]+1].lower()== enemy_color:
            if list_of_board_lines[pos_of_piece[1]+2*next_pos][pos_of_piece[0]+2] == '.':
                list_of_jumps.append((pos_of_piece, (pos_of_piece[0]+2,pos_of_piece[1]+2*next_pos)))
        #process for king pieces backwards jumps
        
        if my_color.isupper():
            #check jump backward left
            if list_of_board_lines[pos_of_piece[1]-next_pos][pos_of_piece[0]-1].lower()== enemy_color:
                if list_of_board_lines[pos_of_piece[1]-2*next_pos][pos_of_piece[0]-2] == '.':
                    list_of_jumps.append((pos_of_piece, (pos_of_piece[0]-2,pos_of_piece[1]-2*next_pos)))
            #check jump backward right
            if list_of_board_lines[pos_of_piece[1]-next_pos][pos_of_piece[0]+1].lower() == enemy_color:
                if list_of_board_lines[pos_of_piece[1]-2*next_pos][pos_of_piece[0]+2] == '.':
                    list_of_jumps.append((pos_of_piece, (pos_of_piece[0]+2,pos_of_piece[1]-2*next_pos)))

        #
        count += 1
        print(list_of_jumps, count, file= sys.stderr)
        if(len(list_of_jumps) >= count):
            pos_of_piece = list_of_jumps[count - 1][1]
    if (len(list_of_jumps) == 0):
        return []
    #ckecking if have multiple jump

    print(list_of_jumps, file= sys.stderr)
    list_of_jumps_string = []
    for move in list_of_jumps:
        list_of_jumps_string.append(convert_tuple_of_positions_to_string(move))
    
    last_lenght_of_list_of_jumps = 0
    while (last_lenght_of_list_of_jumps != len (list_of_jumps_string)):
        last_lenght_of_list_of_jumps = len(list_of_jumps_string)
    for move in list_of_jumps_string:
        for move_tail in list_of_jumps_string:
            if move[-2:] == move_tail[:2]:
                list_of_jumps_string.append(move + move_tail[-2:])
        
    #return biggest moves
    aux_list_of_jumps_string = []
    for move in list_of_jumps_string:
        if len(move) >= len(*list_of_jumps_string[-1:]):
            aux_list_of_jumps_string.append(move)
    print(list_of_jumps_string, "4" , file= sys.stderr)
    return aux_list_of_jumps_string# list with biggest moves


def convert_tuple_of_positions_to_string(pos_init_final_piece):
    #get: a tuple of two tuples
    #return: a String
    char_of_colums = '-ABCDEFGH-'
    char_of_lines = '012345678'
    pos_init_piece = pos_init_final_piece[0]
    pos_final_piece = pos_init_final_piece[1]
    return char_of_colums[pos_init_piece[0]]+char_of_lines[pos_init_piece[1]]+char_of_colums[pos_final_piece[0]]+char_of_lines[pos_final_piece[1]]

def convert_string_to_tuple_of_tuples(string_of_move):
    list_of_tuples_position = []
    char_of_colums = '-ABCDEFGH-'
    for x in range (0, len(string_of_move), 2):
        list_of_tuples_position.append((char_of_colums.find(string_of_move[x]),int(string_of_move[x+1])))

    return tuple(list_of_tuples_position)


my_color = input()  # r or b
if my_color == 'w':
    enemy_color = 'b'
    my_color = 'r'
else:
    enemy_color = 'r'


# game loop
list_of_jumps = []
list_of_moves = []
selected_jumps = []
list_of_board_lines = []



while True:
    list_of_board_lines.append('----------')
    for i in range(8):
        input_line = input()  # board line
        list_of_board_lines.append('-' + input_line + '-')
            
        #print(input_line, i, file=sys.stderr)
        #print('reading tabvle' , file=sys.stderr)
    list_of_board_lines.append('----------')
        #for line in list_of_board_lines:
    list_of_board_lines.reverse()

    #for line in list_of_board_lines:
        #print(line, file=sys.stderr)
        #print('2', file = sys.stderr)
    for line in range (1,9):#line
        for column in range(1,9):#
            #print(list_of_board_lines[line][column] , file=sys.stderr)
            print(list_of_board_lines[line][column], column, line , file = sys.stderr)
            if list_of_board_lines[line][column].lower() == my_color:
                
                pos_of_piece = (column, line)
                print(pos_of_piece, file=sys.stderr)
                #print("24", file=sys.stderr)
                #print(jump(pos_of_piece, list_of_board_lines, my_color), file=sys.stderr)
                print(list_of_jumps, file=sys.stderr)

                list_of_jumps.extend(get_possible_jump(pos_of_piece, list_of_board_lines, list_of_board_lines[line][column]))
                if len(list_of_jumps) == 0:
                    list_of_moves.extend(get_possible_next_move(pos_of_piece, list_of_board_lines, list_of_board_lines[line][column]))
                

    if len(list_of_jumps) > 0:
        len_of_string_of_shortest_jump = 4
        for jump in list_of_jumps:
            if len(jump) > len_of_string_of_shortest_jump:
                len_of_string_of_shortest_jump = len(jump)
                selected_jumps = []
                selected_jumps.append(jump)
            elif len(jump) == len_of_string_of_shortest_jump:
                selected_jumps.append(jump)
        legal_moves = int(input())  # number of legal moves
        for i in range(legal_moves):
            move_string = input()  # move
        print(random.choice(selected_jumps))
        
    else:
        legal_moves = int(input())  # number of legal moves
        for i in range(legal_moves):
            move_string = input()  # move
        print(random.choice(list_of_moves))
    #list_of_board_lines.clear()
    list_of_jumps.clear()
    list_of_moves.clear()
    selected_jumps.clear()
    


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)




'''

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

my_color = input()  # r or b

# game loop
while True:
    for i in range(8):
        input_line = input()  # board line
    legal_moves = int(input())  # number of legal moves
    for i in range(legal_moves):
        move_string = input()  # move

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print("E3F4")'''