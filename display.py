import copy, time, threading

class Display:
    
    def clear_line(n=1):
        LINE_UP = '\033[1A'
        LINE_CLEAR = '\x1b[2K'
        for i in range(n):
            print(LINE_UP, end=LINE_CLEAR) 

    def display(grid):
        for col in range(len(grid[0])-1, -1, -1):
            print(Color.GRID + "|" + Color.END, end="")
            for row in range(len(grid)):
                cell = grid[row][col]
                print(" " if cell is None else Color.PLAYER_A + "O" if cell == "A" else Color.PLAYER_B + "O" if cell == "B" else Color.ERROR + cell, end=Color.GRID + "|" + Color.END)
            print()
        print(Color.GRID + "---------------" + Color.END)
        print(" 1 2 3 4 5 6 7")
        print()

    def animation(game,column):
        grid = game.get_grid()
        if(grid[column].count(None) <= 0):
            Display.display(grid)
            return
        x = grid[column].index(None)-1
        top = 5
        value = grid[column][x]
        bufGrid = copy.deepcopy(grid)
        bufGrid[column][5] = value
        bufGrid[column][x] = None
        while top >= x+1:
            bufGrid[column][top] = value
            if(top <= 4):
                bufGrid[column][top+1] = None
            Display.clear_line(9) if top != 5 else None
            top -=1
            Display.display(bufGrid)
            time.sleep(0.1)

    def displayMenu():
        print("               Press Enter")
        time.sleep(0.5)
        Display.clear_line()
        print("")
        Display.clear_line()
        time.sleep(0.5)
    
    def inputKb(value):
        input()
        value.append(True)

    def menu():
        menu = open("menu.txt","r").read()
        print(menu)
        a_list = []
        x = threading.Thread(target=Display.inputKb, args=(a_list,))
        x.start()
        while not a_list:
            Display.displayMenu()
        Display.clear_line(8)

class Color:
        PLAYER_A = '\033[91m' # red
        PLAYER_B = '\033[93m' # yellow
        GRID = '\033[94m' # blue
        WIN = '\033[92m' # green
        DRAW = '\033[95m' # purple
        ERROR = '\033[33m' # orange
        END = '\033[0m' # end color