
from display import Display
from game import Game
import sys

def main():
    # grid = [["A", "B", "A", "B", "A", "B"],
    #         ["B", "A", "B", "A", "B", "A"],
    #         ["A", "B", "A", "B", "A", "B"],
    #         ["B", "B", "B", "A", "A", None],
    #         ["A", "B", "A", "B", "A", "B"],
    #         ["B", "A", "B", "A", "B", "A"],
    #         ["A", "B", "A", "B", "A", "B"]]
    # Display.displayGrid(grid)
    # Display.displayGrid(grid)
    # Display.animationReverse(grid, 3)
    # game = Game()
    # game.playGame(Display.launchGame())
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

if __name__ == "__main__":
    main()