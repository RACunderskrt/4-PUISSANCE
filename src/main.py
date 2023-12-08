
from display import Display
from game import Game
import sys

def main():
    p1Name = "Thomas"
    p2Name = "Alexandre"
    gm = "10"
    while(int(gm) > 3):
        gm = Display.launchGame()
        match gm:
            case "4":
                p1Name, p2Name = Display.change_names()
            case "5":
                sys.exit()
    Game().playGame(gm, p1Name, p2Name)
    Display.end()

if __name__ == "__main__":
    main()