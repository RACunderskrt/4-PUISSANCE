import re, copy, time, threading, sys, keyboard

class Display:
    ANIMATION_RATE = 0.2

    def clearLine(n=1):
        LINE_UP = '\033[1A'
        LINE_CLEAR = '\x1b[2K'
        for _ in range(n):
            print(LINE_UP, end=LINE_CLEAR)

    def displayGrid(grid):
        for col in range(len(grid[0]) - 1, -1, -1):
            print(Color.GRID + "|" + Color.END, end="")
            for row in range(len(grid)):
                cell = grid[row][col]
                if cell is None:
                    toBePrinted = "  "
                elif re.search("A|iaA", cell):
                    toBePrinted = Color.PLAYER_A + "🔴"
                elif re.search("B|iaB", cell):
                    toBePrinted = Color.PLAYER_B + "🟡"
                else:
                    toBePrinted = Color.ERROR + cell
                print(toBePrinted, end=Color.GRID + "|" + Color.END)
            print()
        print(Color.GRID + "----------------------" + Color.END)
        print(" １ ２ ３ ４ ５ ６ ７")
        print()
    
    def animationDown(grid, col):
        if grid[col].count(None) <= 0:
            Display.displayGrid(grid)
            return
        
        top = grid[col].index(None) - 1
        value = grid[col][top]
        bufGrid = copy.deepcopy(grid)
        bufGrid[col][top] = None
        bufGrid[col][5] = value
        Display.displayGrid(bufGrid)

        for row in range(4, top-1, -1):
            time.sleep(Display.ANIMATION_RATE)
            bufGrid[col][row] = value
            bufGrid[col][row + 1] = None
            Display.clearLine(9)
            Display.displayGrid(bufGrid)

    def animationReverse(grid, col):
        # top = grid[col].index(None) - 1 if grid[col].count(None) > 0 else 5
        # bufGrid = copy.deepcopy(grid)
        # for i in range(top // 2 + top % 2):
        #     time.sleep(Display.ANIMATION_RATE)
        #     bufGrid[col][i], bufGrid[col][top - i] = bufGrid[col][top - i], bufGrid[col][i]
        #     Display.clearLine(9)
        #     Display.displayGrid(bufGrid)
        top = grid[col].index(None) - 1 if grid[col].count(None) > 0 else 5
        bufGrid = copy.deepcopy(grid)
        for i in range(top // 2 + top % 2):
            bufGrid[col][i], bufGrid[col][top - i] = bufGrid[col][top - i], bufGrid[col][i]
        bufGrid2 = copy.deepcopy(grid)
        for i in range(top // 2 + top % 2):
            time.sleep(Display.ANIMATION_RATE)
            bufGrid2[col][i] = None
            bufGrid2[col][top - i] = None
            Display.clearLine(9)
            Display.displayGrid(bufGrid2)
        for i in range(top // 2 + top % 2 - 1, -1, -1):
            time.sleep(Display.ANIMATION_RATE)
            bufGrid2[col][i] = bufGrid[col][i]
            bufGrid2[col][top - i] = bufGrid[col][top - i]
            Display.clearLine(9)
            Display.displayGrid(bufGrid2)

    def displayMenu():
        print(Color.GRID + "               Press Enter" + Color.END)
        time.sleep(0.5)
        Display.clearLine()
        print("")
        Display.clearLine()
        time.sleep(0.5)

    def inputKb(value):
        input()
        value.append(True)

    def menu():
        menu = open("menu.txt", "r").read()
        print(menu)
        a_list = []
        t = threading.Thread(target=Display.inputKb, args=(a_list,))
        t.start()
        while not a_list:
            Display.displayMenu()
        Display.clearLine()

    def choiceGM():
        choix = open("choixGM.txt", "r").read()
        print(choix)
        while True:
            gm = input()
            Display.clearLine()
            if re.search("[1-3]", gm):
                break
        Display.clearLine(11)
        return gm
    
    def choiceGM2():
        select = 0
        Display.changeMenu(select)
        ui = None 
        while (ui != 'space'):
            ui = keyboard.read_key(True)
            match ui:
                case 'z':
                    select = (select-1)%5
                    Display.clearLine(7)
                    Display.changeMenu(select)
                    time.sleep(0.2)
                case 's':
                    select = (select+1)%5
                    Display.clearLine(7)
                    Display.changeMenu(select)
                    time.sleep(0.2)
                case 'q':
                    sys.exit()
        Display.clearLine(14)
        return str(select+1)
    
    def changeMenu(index):
        print("          ", '\u2192' if index == 0 else " ", "1. Singleplayer")
        print("          ", '\u2192' if index == 1 else " ", "2. Multiplayer")
        print("          ", '\u2192' if index == 2 else " ", "3. No gaming")
        print("          ", '\u2192' if index == 3 else " ", "4. Change Names")
        print("          ", '\u2192' if index == 4 else " ", "5. Quit")
        print()
        print("z: up | s: down | space: select | q: quit")
    
    def launchGame():
        Display.menu()
        return Display.choiceGM2()
    
    def change_names():
        print("Select names for the Player A:")
        p1 = input()
        Display.clearLine(2)
        print("Select names for the Player B:")
        p2 = input()
        Display.clearLine(2)
        return p1, p2

class Color:
    PLAYER_A = '\033[91m' # red
    PLAYER_B = '\033[93m' # yellow
    GRID = '\033[94m' # blue
    WIN = '\033[92m' # green
    DRAW = '\033[95m' # purple
    ERROR = '\033[33m' # orange
    END = '\033[0m' # end color