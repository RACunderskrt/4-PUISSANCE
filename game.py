from player import Player
from display import Display, Color

import re, random

class Game:
    def __init__(self):
        self.player1 = Player("Thomas", "A")
        self.player2 = Player("Alexandre", "B")
        self.grid = [[None for _ in range(6)] for _ in range(7)]
        self.gridHorizontal = [[None for _ in range(7)] for _ in range(6)]
        self.gridDiagonalLeft = [[None for _ in range(i)] for i in range(4, 7)] + [[None for _ in range(i)] for i in range(6, 3, -1)]
        self.gridDiagonalRight = [[None for _ in range(i)] for i in range(4, 7)] + [[None for _ in range(i)] for i in range(6, 3, -1)]
    
    def get_player1(self):
        return self.player1
    
    def get_player2(self):
        return self.player2
    
    def get_grid(self):
        return self.grid
    
    def get_grid_horizontal(self):
        return self.gridHorizontal
    
    def get_grid_diagonal(self):
        return self.gridDiagonalLeft, self.gridDiagonalRight
    
    def reset_grid(self):
        self.grid = [[None for _ in range(6)] for _ in range(7)]
        self.gridHorizontal = [[None for _ in range(7)] for _ in range(6)]
        self.gridDiagonalLeft = [[None for _ in range(i)] for i in range(4, 7)] + [[None for _ in range(i)] for i in range(6, 3, -1)]
        self.gridDiagonalRight = [[None for _ in range(i)] for i in range(4, 7)] + [[None for _ in range(i)] for i in range(6, 3, -1)]


    def playGame(self, gm, p1Name, p2Name):
        print("Aligne 4 jetons et la victoire est à toi !", end="\n\n")
        p1 = self.player1
        p2 = self.player2
        p1.set_name(p1Name)
        p2.set_name(p2Name)
        activePlayer = None
        input = None
        colAI = None
        error = 0

        Display.displayGrid(self.grid)
        while not self.checkWin()[0]:
            activePlayer = p2 if activePlayer == p1 else p1
            match(gm):
                case "1":
                    if activePlayer == p1:
                        if colAI != None:
                            print("The AI played in " + str(colAI))
                        print("Player " + activePlayer.name, end='')
                    else:
                        print("The AI is playing... ", end='')
                case "2":
                    print("Player " + activePlayer.name, end='')
                case "3":
                    print("L'AI joue..." if colAI == None else "L'IA a joué en " + str(colAI + 1), end='')
            print(" - Reverse token available" if activePlayer.token else "")
            match(gm):
                case "1":
                    input, colAItmp, error = self.testInput(activePlayer) if activePlayer == p1 else self.aiChoice(activePlayer) + (0,)
                    Display.clearLine(10 + error + (activePlayer == p1) + (activePlayer == p1 and colAI != None))
                    colAI = colAItmp
                case "2":
                    input, colAI, error = self.testInput(activePlayer)
                    Display.clearLine(11 + error)
                case "3":
                    input, colAI = self.aiChoice(activePlayer)
                    Display.clearLine(10)
            col = int(input[0]) - 1
            self.insert(col, activePlayer.id)
            Display.animationDown(self.grid, col)
            Display.clearLine(9)
            if len(input) > 1 and re.search("[rR]", input[1]):
                self.reverse(col)
                activePlayer.set_tokenFalse()
                Display.animationReverse(self.grid, col)
                Display.clearLine(9)
            Display.displayGrid(self.grid)
        result = self.checkWin()
        if result[1] == "draw":
            print("Draw")
        else:
            match(gm):
                case "1":
                    print("Player " + p1.name + " won" if result[1] == p1.id else "IA won")
                case "2":
                    print("Player " + (p1.name if result[1] == p1.id else p2.name) + " won")
                case "3":
                    print("The AI " + ("number 1" if result[1] == p1.id else "number 2") + " won")
    
    def columnFull(self, col):
        return self.grid[col].count(None) <= 0
    
    def gridFull(self):
        return all([self.columnFull(i) for i in range(7)])
    
    def insert(self, col, id):
        if self.columnFull(col):
            raise Exception("Column " + str(col) + " is full")
        row = self.grid[col].index(None)
        self.grid[col][row] = id
        self.gridHorizontal[row][col] = id
        indexLeft = col + row - 3
        indexRight = row - col + 3
        if 0 <= indexLeft < 6:
            self.gridDiagonalLeft[indexLeft][row if indexLeft < 4 else 6 - col] = id
        if 0 <= indexRight < 6:
            self.gridDiagonalRight[indexRight][row if indexRight < 4 else col] = id
    
    def reverse(self, col): 
        if(self.grid[col].count(None)): 
            x = self.grid[col].index(None)
        else:
            x = 6 #if the column is full we reverse all the column
        bufArr = self.grid[col][0:x]
        self.grid[col][0:x] = bufArr[::-1]
        self.reverseHorizontal()
        self.reverseDiagonal()

    def reverseHorizontal(self):
        bufGridHorizontal = [[None for i in range(7)] for j in range(6)]
        for i in range (len(self.grid)):
            for j in range (len(self.grid[i])):
                bufGridHorizontal[j][i] = self.grid[i][j]
        self.gridHorizontal = bufGridHorizontal

    def reverseDiagonal(self):
        max_col = len(self.grid[0])
        max_row = len(self.grid)
        fdiag = [[] for _ in range(max_row + max_col - 1)]
        bdiag = [[] for _ in range(len(fdiag))]
        min_bdiag = -max_row + 1
        for x in range(max_col):
            for y in range(max_row):
                fdiag[x+y].append(self.grid[y][x])
                bdiag[x-y-min_bdiag].append(self.grid[y][x])
        self.gridDiagonalLeft = fdiag[3:-3]
        self.gridDiagonalRight = bdiag[3:-3]

    def checkWin(self):
        if self.gridFull():
            return True, "draw"
        else:
            for gridToCheck in [self.grid, self.gridHorizontal, self.gridDiagonalLeft, self.gridDiagonalRight]:
                result = self.check(gridToCheck)
                if result[0]:
                    return True, result[1]
            return False, None

        
    def check(self, grid):
        for arr in grid:
            for i in range(len(arr) - 3):
                if arr[i] == arr[i + 1] == arr[i + 2] == arr[i + 3] != None:
                    return True, arr[i]
        return False, None
    
    def testInput(self, activePlayer):
        choice = ''
        col = -1
        error = 0

        while not re.search("^[1-7]([rR])?$", choice) or activePlayer.verifyToken(choice) or self.columnFull(col):
            try:
                choice = str(input("Enter column (1-7) : "))
                if not len(choice) or len(choice) > 2 or (len(choice) > 1 and not re.search("[rR]", choice[1])):
                    raise ValueError()
                
                col = int(choice[0]) - 1

                if col < 0 or col > 6:
                    raise ValueError()
                
                if self.columnFull(col):
                    Display.clearLine(1 + error)
                    print(Color.ERROR + "Column " + str(col + 1) + " is full. Please choose another one." + Color.END)
                    error = 1

                elif activePlayer.verifyToken(choice):
                    Display.clearLine(1 + error)
                    print(Color.ERROR + "Reverse token already used. Try without." + Color.END)
                    error = 1

            except ValueError:
                Display.clearLine(1 + error)
                print(Color.ERROR + "Invalid input. Please enter a number between 1 and 7." + Color.END)
                error = 1

        return choice, None, error

    def aiChoice(self, activePlayer):
        non_full_columns = [i for i in range(len(self.grid)) if not self.columnFull(i)]

        if not non_full_columns:
            return None, None

        col = random.choice(non_full_columns) + 1
        choice = str(col) + ('r' if activePlayer.token and random.random() < 0.2 else '')

        return choice, col