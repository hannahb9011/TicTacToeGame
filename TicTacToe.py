import random

#Create a new board which represents all the possible places a piece can go
#then returns the created board
def CreatNewBoard():
    board = [' ' for i in range(9)]#populates an array of 9 (0-8) empty strings 
    return board

#Use the information of where each piece goes and print it inside a formatted board
def PrintBoard(board):
    print('   |   |')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('   |   |')
    
#Takes the index of the move that was chosen and fills that array position with the provided piece
#then returns the updated version of the board
def UpdateBoard(curr_board, move, piece):
    board = curr_board[:]
    board[move] = piece
    return board

#Checks if all the positions are filled with something other than a space which indiactes a full board.
#If the board is full it returns True, otherwise its False
def IsBoardFull(board):
    if board.count(' ') == 0:
        return True
    else:
        return False
    
#Checks if all the positions are blank which indiactes an empty board
#If the board is empty it returns True, otherwise its False
def IsBoardEmpty(board):
    if board.count(' ') == 9:
        return True
    else:
        return False

#looks at the provided board position and examines positions representing the vertical, horiziontal, and diaginal
#wins to see if there any piece is lined up in each indicated position. If a winning position is found, it returns True,
#otherwise its False.
def IsWinner(board, player):
    winner = False
    test1 = (0,3,6)
    test2 = (0,1,2)
    for i in test1:
        if board[i] == player and board[i+1] == player and board[i+2] == player: #Horizontal win
            winner = True
    for i in test2:
        if board[i] == player and board[i+3] == player and board[i+6] == player: #Vertical win
            winner = True
    if board[4] == player and (board[0] == player and board[8] == player or board[2] == player and board[6] == player): #Diagonal win
        winner = True
    return winner
 
 #Takes a look at all the possible array positions and create a list of all the remain choices/where its still blank.
 #Once all the positions are searched, the list of avaliablle postions is returned
def AvaliableMoves(board):
    avaliable = []
    for i in range(len(board)):
        if board[i] == ' ':
            if avaliable:
                avaliable.append(i)
            else:
                avaliable = [i]
    return avaliable
 
 #Provides a move choice based on the current position of the board and the rules of the game.
 #The chosen move is sent back
def ComputerMove(board, piece):
    print("\nComputer's Move:")
    possibleMoves = AvaliableMoves(board)
    move = -1 #if says -1 theres an error
    
    #orders to search computer's piece first so it can see its avaliable win before seeing opponents 
    #avaliable win that it thinks it needs to block
    if piece == 'X':
        order = ['X','O']
    else:
        order = ['O', 'X']

    if len(possibleMoves) == 9: #all spots open / first move
        move = 4  #pick middle square, since its the most valuable spot to occupy on the board
        return move
    
    for piece in order: #check for a winning move
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = piece
            if IsWinner(boardCopy, piece):
                move = i
                return move

    cornersOpen = [] #corners tend to be the second strongest move after someone chooses the middle
    for i in possibleMoves: #check for any possible open corner moves
        if i in [0,2,6,8]:
            cornersOpen.append(i) #track the index of the open corner moves
            
    if len(cornersOpen) > 0: #if there is at least one corner move to play chose a random one
        rand = random.randrange(0,len(cornersOpen))
        move = cornersOpen[rand]
        return move

    edgesOpen = [] #if theres no other choices for the middle or corners, an edge must be chosen
    for i in possibleMoves: #check for any possible open corner moves
        if i in [1,3,5,7]:
            edgesOpen.append(i) #track the index of the open corner moves
            
    if len(edgesOpen) > 0: #if there is at least one corner move to play chose a random one
        rand = random.randrange(0,len(edgesOpen))
        move = edgesOpen[rand]
        return move
        
    return move # incase error

#Allows the computer's opponent/the user to type in a position based on the provided number for each space.
#The user much pick a number in the stated range and a posotion that is not already occupied. If the users chosen move,
#is valid it is returned
def UserMove(board):
    print("\nYour turn")
    while True:
        move = input('Please select an empty spot [0-8]: ')#provided the index of a space by the user
        try:#needs this inaces the int conversion creates an error due to a number not being what was entered
            move = int(move)#convert string to an int to do checks on the number
            if move >= 0 and move <= 8:#checks to make sure the user chose a number in the range of 0-8
                if board[move] == ' ':
                    return move
                else:
                    print('Type a different number, this one is taken!')
            else:
                print('Entered number is out of range, try again')
        except:
            print('Invalid, please type a number!')
            

#'Main' part of the program, where the actual game is played through 
numbering = ['0','1','2','3','4','5','6','7','8']
print("For this game of Tic-Tac-Toe the boxes are respresented by the diagram below:")
PrintBoard(numbering) #print a board with numbers 0-8 labeling each position

while True:
    answer = input('\nWant to start a game? (Y/N)')
    if answer.upper() == 'Y' or answer.upper() == 'YES':
        board = CreatNewBoard() #Create an fresh empty board
        PrintBoard(board)
        turn = 'X' #starting turn
         
        while True:
            player = input("Want to play as 'X' or 'O' ('X' goes first)")
            if player.upper() == 'X': #user will start
                move = UserMove(board)
                break
            elif player.upper() == 'O': #computer will start
                move = ComputerMove(board, turn)
                break
            else:
                print("Invalid piece, enter 'X' or 'O'.")
            
        board = UpdateBoard(board, move, turn) #play chosen move
        PrintBoard(board) #print new position
        
        while not IsBoardFull(board):
            if IsWinner(board, turn): #check if the board has a win
                break
            else: #continue playing 
                #change to next turn
                if turn == 'X':
                        turn = 'O'
                else:
                    turn = 'X'
                    
                if player.upper() == 'X': #if player chose 'X' piece, computer will play 'O'
                    if turn == 'X':
                        move = UserMove(board)
                    else:
                        move = ComputerMove(board, turn)
                else: #else player chose 'O' piece, computer will play 'X'
                    if turn == 'O':
                        move = UserMove(board)
                    else:
                        move = ComputerMove(board,turn)
                        
                board = UpdateBoard(board, move, turn) #play chosen move
                PrintBoard(board) #print new position
                
                
        if IsWinner(board, turn):
                print("'%s' is the winner!" % turn)
        else:
            print('Tie Game!')
       
    elif answer.upper() == 'N' or answer.upper() == 'NO':
        print("Come back when you want to play! Goodbye\n")
        break
    else:
        print("Invalid response, try again (Enter Y/N)")