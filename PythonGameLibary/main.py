import TicTacToeNonGUI
import GUIexp

def listgames():
    print("1. Tic Tac Toe")
    print("2. Get the Square")
    print("3. Show Scores")
    print("4. Exit")


game = 0
while game != -1:
    listgames()
    try:
        game = int(input("Please enter the number of the game you want to play: "))
    except:
        game = 0
    #if the user picks to play Tic Tac Toe
    if game == 1:
        
                
        try:
            score = open("score.txt")
        except:
            score = open("score.txt", "w")
            score.write("0\n0\n0\n0\n0")

            score.close()
            score = open("score.txt")
        player1Wins = score.readline()
        player2Wins = score.readline()
        ComputerWins = score.readline()
        Ties = score.readline()
        
        score.close()
        player1Wins = int(player1Wins)
        player2Wins = int(player2Wins)
        Ties = int(Ties)
        ComputerWins = int(ComputerWins)
        vsComputer = ""
        while vsComputer == "":
            vsComputer = input("do you want to play vs a computer yes or no: ")
            if vsComputer == "yes":
                winner = TicTacToeNonGUI.Playgame(True)
            elif vsComputer == "no":
                winner = TicTacToeNonGUI.Playgame(False)
            else: 
                vsComputer = ""
    
        if winner == 1:
            player1Wins += 1
        elif winner == 2:
            player2Wins += 1
        elif winner == 3:
            ComputerWins += 1
        elif winner == -1:
            Ties += 1
        score = open("score.txt", "r")
        lines = score.readlines()
        score.close()
        
        lines[0] = str(player1Wins) + "\n"
        lines[1] = str(player2Wins) + "\n"
        lines[2] = str(ComputerWins) + "\n"
        lines[3] = str(Ties)+ "\n"

        score = open("score.txt", "w")

        score.writelines(lines)

        score.close()
    elif game == 2:
        try:
            score = open("score.txt")
        except:
            score = open("score.txt", "w")
            score.write("0\n0\n0\n0\n0")

            score.close()
            score = open("score.txt")
        
        
        highScore = int(score.readline())
        score.close()
        gameScore = GUIexp.playgame()
        if gameScore > highScore:
            score = open("score.txt", "r")
            lines = score.readlines()
            score.close()
            lines[4] = str(gameScore)
            score = open("score.txt", "w")
            score.writelines(lines)
            score.close()
            
    elif game == 3:
        try:
            score = open("score.txt")
        except:
            score = open("score.txt", "w")
            score.write("0\n0\n0\n0\n0")

            score.close()
            
        score = open("score.txt")    
        player1Wins = score.readline()
        player2Wins = score.readline()
        ComputerWins = score.readline()
        Ties = score.readline()
        highScore = score.readline()
        score.close()
        print("Player One: " + player1Wins, end = "")
        print("Player Two: " + player2Wins, end = "")
        print("Computer: " + ComputerWins, end = "")
        print("Ties: " + Ties, end = "")
        print("High Score: " + highScore)
        
    elif game == 4:
        game = -1
