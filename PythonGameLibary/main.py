import TicTacToeNonGUI

def listgames():
    print("1. Tic Tac Toe")
    print("2. Show Scores")
    print("3. Exit")


game = 0
while game != -1:
    listgames()
    try:
        game = int(input("Please enter the number of the game you want to play: "))
    except:
        game = 0

    if game == 1:
        
                
        try:
            score = open("PythonGameLibary/score.txt")
        except:
            score = open("PythonGameLibary/score.txt", "w")
            score.write("0\n0\n0\n0")

            score.close()
            score = open("PythonGameLibary/score.txt")
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
        score = open("PythonGameLibary/score.txt", "w")

        score.write(str(player1Wins) + "\n" + str(player2Wins) + "\n" + str(ComputerWins) + "\n" + str(Ties))

        score.close()
    elif game == 2:
        try:
            score = open("PythonGameLibary/score.txt")
        except:
            score = open("PythonGameLibary/score.txt", "w")
            score.write("0\n0\n0\n0")

            score.close()
            
        score = open("PythonGameLibary/score.txt")    
        player1Wins = score.readline()
        player2Wins = score.readline()
        ComputerWins = score.readline()
        Ties = score.readline()
        score.close()
        print("Player One: " + player1Wins, end = "")
        print("Player Two: " + player2Wins, end = "")
        print("Computer: " + ComputerWins, end = "")
        print("Ties: " + Ties)
    elif game == 3:
        game = -1
