class Display:
    def display(game):
        for col in range(len(game.get_grid()[0])-1, -1, -1):
            print("|", end="")
            for row in range(len(game.get_grid())):
                cell = game.get_grid()[row][col]
                print(" " if cell is None else cell, end="|")
            print()
        print("---------------")
        print(" 1 2 3 4 5 6 7")
        print()
