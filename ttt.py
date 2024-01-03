from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    print (' '+board[7]+' | '+board[8]+' | '+board[9])
    print ('-----------')
    print (' '+board[4]+' | '+board[5]+' | '+board[6])
    print ('-----------')
    print (' '+board[1]+' | '+board[2]+' | '+board[3])
board = [' ']*10

def player_input():
    
    marker = ''
    
    while marker.capitalize() !='X' and marker.capitalize() !='O':
        marker = input('Player 1, chose X or O :')
    
    player1=marker.capitalize()
    
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return (player1,player2) 

def place_marker(board,marker,position):
	board[position]=marker
def win_check(board,mark):
    return ((board[1]==board[2]==board[3]==mark) or 
    (board[4]==board[5]==board[6]==mark) or 
    (board[7]==board[8]==board[9]==mark) or
    
    (board[7]==board[4]==board[1]==mark) or
    (board[8]==board[5]==board[2]==mark) or
    (board[9]==board[6]==board[3]==mark) or
    
    (board[7]==board[5]==board[3]==mark) or
    (board[9]==board[5]==board[1]==mark))

import random

def chose_first():
    
    flip = random.randint(0,1)
    
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'
def space_check(board,position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True    
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Chose a position(1-9): '))
    return position
def replay():
    choice = input('Play Again? Enter Yes or No : ')
    return choice.upper() == 'YES'

#-----------------------------------------------------------------------------#    
print('Welcome to TIC TAC TOE')
#While loop to keep running the game
while True:
    #Play the game
    
    #SET Everything up(board, markers X or O, Chosing who playes first)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = chose_first()
    print(turn + ' will go first')
    
    play_game = input('Ready to play? Y or N : ')
    if play_game.capitalize()=='Y':
        game_on = True
    else:
        game_on = False
        
    ##Gameplay
    while game_on:
        if turn =='Player 1':
            #Display the board
            display_board(the_board)
            #chose  a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
            #check if the player has won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLayer 1 Has Won the Game!')
                game_on = False
            #or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a Tie')
                    game_on = False
                else:
                    turn = 'Player 2'
            #No tie and No Win? Then it will be next player's turn
           ###Player 1 turn
        else:
            #Display the board
            display_board(the_board)
            #chose  a position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player2_marker,position)
            #check if the player has won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLayer 2 Has Won the Game!')
                game_on = False
            #or check if there is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a Tie')
                    game_on = False
                else:
                    turn = 'Player 1'
        ###Player 2 turn

    if not replay():
        break
# break out the while loop with the replay function                            	