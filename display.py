import copy, time, threading
import time
import keyboard
import sys

class Display:
    
    SELECT = 0

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
                print("  " if cell is None else Color.PLAYER_A + "🔴" if cell == "A" else Color.PLAYER_B + "🟡" if cell == "B" else Color.ERROR + cell, end=Color.GRID + "|" + Color.END)
            print()
        print(Color.GRID + "----------------------" + Color.END)
        print(" １ ２ ３ ４ ５ ６ ７")
        print()

    def animation(game,column): #Create a bunch of temporary grid to do the animation
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
        print(Color.GRID+"               Press Enter"+Color.END)
        time.sleep(0.5)
        Display.clear_line()
        print("")
        Display.clear_line()
        time.sleep(0.5)
    
    def inputKb(value): 
        input()
        value.append(True)

    def menu(): #Create a menu with a flickering "Press Enter"
        menu = open("menu.txt","r").read()
        print(menu)
        a_list = []
        x = threading.Thread(target=Display.inputKb, args=(a_list,))
        x.start()
        while not a_list:
            Display.displayMenu() #Display the menu until the thread transform a_list to stop the loop
        Display.clear_line(8)
    
    def choiceGM():
        menu = open("menu.txt","r").read()
        choix = open("choixGM.txt","r").read()
        print(menu)
        print(choix)
        while True: #Until the right input, the player need to enter a value
            gm = input()
            Display.clear_line()
            if(gm == "1" or gm == "2"):
                Display.clear_line(9)
                return gm


    def choiceGM2():
        menu = open("menu.txt","r").read()
        print(menu)
        choixGM = open("choixGM.txt","r").read()
        print(choixGM)
        select = 0
        Display.changeMenu(select)
        ui = None 
        while (ui != 'space'):
            ui = keyboard.read_key(True)
            match ui:
                case 'z':
                    select = (select-1)%4
                    Display.changeMenu(select)
                    time.sleep(0.2)
                case 's':
                    select = (select+1)%4
                    Display.changeMenu(select)
                    time.sleep(0.2)
                case 'q':
                    sys.exit()
        Display.clear_line(13)
        return select

    def changeMenu(index):
        Display.clear_line(6)
        print("          ", '\u2192' if index == 0 else " ", "1. Singleplayer")
        print("          ", '\u2192' if index == 1 else " ", "2. Multiplayer")
        print("          ", '\u2192' if index == 2 else " ", "3. No gaming")
        print("          ", '\u2192' if index == 3 else " ", "4. Quit")
        print()
        print("z: up | s: down | space: select | q: quit")

class Color:
        PLAYER_A = '\033[91m' # red
        PLAYER_B = '\033[93m' # yellow
        GRID = '\033[94m' # blue
        WIN = '\033[92m' # green
        DRAW = '\033[95m' # purple
        ERROR = '\033[33m' # orange
        END = '\033[0m' # end color