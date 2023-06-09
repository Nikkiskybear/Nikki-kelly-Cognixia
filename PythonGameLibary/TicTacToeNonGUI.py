import random



def setup(computerP):
    #resets the board 
    #would be smarter to use objects so no globals but I didn't think about that till I was half way through
    global board 
    global turn
    global winner
    global computer
    if computerP == False:
        computer = False
    else:
        computer = True
    board = [" ", " ", " ",
             " ", " ", " ",
             " ", " ", " ", ]
    turn = 1
    winner = 0
#prints out the board
def render():
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print('_____|_____|_____')
 
    print("     |     |")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print('_____|_____|_____')
 
    print("     |     |")
 
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")
    print("\n")
#gets the move from who evers turn it is
def getAction():
    action = 0
    if turn % 2 == 0:
        print("Player Two your Turn")
    else:
        print("Player One your Turn")
    #checks to see if you are going against a computer and if your not or it would be the players turn and not the computers gets the move from the player
    if computer == False or turn % 2 != 0:

        while action == 0:
            #gets a number 1-9 from the player that has not already been selected
            try:
                action = int(input("Please enter a vaild move from 1-9: "))
            except:
                print("Not a int")
            else:
                if action >= 1 and action <= 9:    
                    if board[action-1] != " ":
                        print("Not a valid move")
                        action = 0
                else:
                    print("Not a move between 1 and 9")
                    action = 0
    else:
        #computers move gets a random number 1-9 and if its already selcted gets a new random number
        while action == 0:
            action = random.randint(1, 9)
            
            if action >= 1 and action <= 9:    
                    if board[action-1] != " ":
                        
                        action = 0

    return action-1
#updates the board with the action selected
#takes in action which is a number between 0-8
def makeMove(action):
    if turn % 2 == 0:
        board[action] = "O"
    else:
        board[action] = "X"


def CheckForWiner():
    """
    winList exp 
    each element of the list is one of the 8 possible ways to win a tic tac toe game
    elements 0 1 2 are the 3 vertical ways of winning 0 being the left most and 2 being the right most

    eg this would be winList[0,1,1,1,1,1,1,1]
         |     |
      O  |     |
    _____|_____|_____
         |     |
      O  |     |
    _____|_____|_____
         |     |
      O  |     |
         |     |
    Elements 3 4 5 are the 3 Horisiontal ways of winning 3 being the top and 5 being the bottom
    Elements 6 7 are the 2 diagonal ways of winning 6 being the top left to bottom right and 7 being the top right to bottom left   
    """
    winList = [0]*8
    win = False
    global turn
    global winner
    if turn % 2 == 0:
        if board[0] != "O":
            winList[0] = 1
            winList[3] = 1
            winList[6] = 1

        if board[1] != "O":
            winList[1] = 1
            winList[3] = 1
            
        if board[2] != "O":
            winList[2] = 1
            winList[3] = 1
            winList[7] = 1

        if board[3] != "O":
            winList[0] = 1
            winList[4] = 1
            
        if board[4] != "O":
            winList[1] = 1
            winList[4] = 1
            winList[6] = 1
            winList[7] = 1

        if board[5] != "O":
            winList[2] = 1
            winList[4] = 1
            
        if board[6] != "O":
            winList[0] = 1
            winList[5] = 1
            winList[7] = 1
            
        if board[7] != "O":
            winList[1] = 1
            winList[5] = 1
            
        if board[8] != "O":
            winList[2] = 1
            winList[5] = 1
            winList[6] = 1
    else:
        if board[0] != "X":
            winList[0] = 1
            winList[3] = 1
            winList[6] = 1

        if board[1] != "X":
            winList[1] = 1
            winList[3] = 1
            
        if board[2] != "X":
            winList[2] = 1
            winList[3] = 1
            winList[7] = 1

        if board[3] != "X":
            winList[0] = 1
            winList[4] = 1
            
        if board[4] != "X":
            winList[1] = 1
            winList[4] = 1
            winList[6] = 1
            winList[7] = 1

        if board[5] != "X":
            winList[2] = 1
            winList[4] = 1
            
        if board[6] != "X":
            winList[0] = 1
            winList[5] = 1
            winList[7] = 1
            
        if board[7] != "X":
            winList[1] = 1
            winList[5] = 1
            
        if board[8] != "X":
            winList[2] = 1
            winList[5] = 1
            winList[6] = 1
    
    #checks to see if the game has been one
    for n in winList:
        if n != 1:
            win = True
#if someone has one figures how who it is and set the winner
    if win == True:
        if turn % 2 == 0:
            if computer == True:
                print("the Computer Won")
                winner = 3
            else:
                print("Player 2 wins")
                winner = 2
        else:
            print("Player 1 wins")
            winner = 1 
    #checks to see if the game ends in a tie or not
    if turn >= 9:
        winner = -1
        print("Its a Tie")
    turn += 1
    

#runs the game
#takes in a bool for whether or not your vs a computer
def Playgame(computer = False):
    setup(computer)
    global winner
    while winner == 0:
        
        makeMove(getAction())
        render()
        CheckForWiner()
    return winner
        



        
        

        
        

