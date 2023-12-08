from display import Display
from game import Game

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
    Game().playGame(Display.launchGame())
    return

if __name__ == "__main__":
    main()