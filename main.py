from game import Game
from player import Player
from display import Display, Color

def play_game():
    print("Aligne 4 jetons et la victoire est à toi", end="\n\n")
    p1 = Player("A")
    p2 = Player("B")
    active_player = None

    g1 = Game(p1, p2)
    grid = g1.get_grid()

    Display.display(grid)

    while not g1.verify_all() and not g1.grid_full():
        active_player = p2 if active_player == p1 else p1
        print("Player " + active_player.get_char())
        column = None
        error = False
        while column is None or column < 1 or column > 7 or g1.columnFull(column - 1):
            try:
                column = int(input("Enter column (1-7): "))
                if column < 1 or column > 7:
                    Display.clear_line(1+error)
                    print("Invalid input. Please enter a number between 1 and 7.")
                    error = True
                elif g1.columnFull(column - 1):
                    Display.clear_line(1+error)
                    print("Column is full. Please choose another column.")
                    error = True
            except ValueError:
                Display.clear_line(1+error)
                print(Color.ERROR + "Invalid input. Please enter a number between 1 and 7." + Color.END)
                error = True
        print()
        Display.clear_line(11+error)
        g1.insert(column - 1, active_player)
        Display.animation(g1, column - 1)
        Display.clear_line(9)
        Display.display(grid)

    if g1.verify_all():
        print(Color.WIN + "Player " + active_player.get_char() + " won" + Color.END)
    else:
        print(Color.DRAW + "Draw" + Color.END)

def main():
    Display.menu()
    play_game()

if __name__ == '__main__':
    main()