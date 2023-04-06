import TicTacToeNonGUI
import GUIexp
#prints the list of options 
def listgames():
    print("1. Tic Tac Toe")
    print("2. Get the Square")
    print("3. Show Scores")
    print("4. Exit")


game = 0
while game != -1:
    listgames()
    #asks user to pick an option
    try:
        game = int(input("Please enter the number of the game you want to play: "))
    except:
        game = 0
    #if the user picks to play Tic Tac Toe
    if game == 1:
        
        #opens the score file and if its not real makes one        
        try:
            score = open("score.txt")
        except:
            score = open("score.txt", "w")
            score.write("0\n0\n0\n0\n0")

            score.close()
            score = open("score.txt")
        #gets the scores
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
        #asks if the player wants to play vs a computer and runs the game
        while vsComputer == "":
            vsComputer = input("do you want to play vs a computer yes or no: ")
            if vsComputer == "yes":
                winner = TicTacToeNonGUI.Playgame(True)
            elif vsComputer == "no":
                winner = TicTacToeNonGUI.Playgame(False)
            else: 
                vsComputer = ""

        #ups the score based on who won
        if winner == 1:
            player1Wins += 1
        elif winner == 2:
            player2Wins += 1
        elif winner == 3:
            ComputerWins += 1
        elif winner == -1:
            Ties += 1
        #rewrites the file with the new scores
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

    #runs the get the square game
    elif game == 2:
        #opens the score file and makes one if the score file isn't real
        try:
            score = open("score.txt")
        except:
            score = open("score.txt", "w")
            score.write("0\n0\n0\n0\n0")

            score.close()
            score = open("score.txt")
        
        #runs the game 
        highScore = int(score.readline())
        score.close()
        gameScore = GUIexp.playgame()
        #checks to see if the score is higher than the highscore and replaces the highscore if it is 
        if gameScore > highScore:
            score = open("score.txt", "r")
            lines = score.readlines()
            score.close()
            lines[4] = str(gameScore)
            score = open("score.txt", "w")
            score.writelines(lines)
            score.close()
    #displays the score
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
    #exits from the game and ends the program
    elif game == 4:
        game = -1
