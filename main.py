from game import Game
from player import Player
from display import Display, Color
import re

REG = '^[1-7][rR]?$'

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
        print("Player " + active_player.get_char(), end='')
        print(' - Reverse token available') if active_player.get_token() else print('')
        inputVar = ' '
        error = False
        column = -1
        while g1.columnFull(column) or active_player.verify_token_error(inputVar) or not re.search(REG, inputVar):
            try:
                inputVar = str(input("Enter column (1-7): "))
                if(not len(inputVar)):
                    raise ValueError()
                
                column = int(inputVar[0])-1

                if column < 0 or column > 6:
                    raise ValueError()

                if g1.columnFull(column):
                    Display.clear_line(1+error)
                    print(Color.ERROR +"Column is full. Please choose another column." + Color.END)
                    error = True

                if(active_player.verify_token_error(inputVar)):
                    Display.clear_line(1+error)
                    print(Color.ERROR + "Reverse token already used. Please choose another column." + Color.END)
                    error = True

            except ValueError:
                Display.clear_line(1+error)
                print(Color.ERROR + "Invalid input. Please enter a number between 1 and 7." + Color.END)
                error = True
        print()
        Display.clear_line(12+error)
        g1.insert(column, active_player)
        Display.animation(g1, column)
        Display.clear_line(9)
        Display.display(grid)
        if(len(inputVar)>1 and (inputVar[1] == 'R' or inputVar[1] == 'r')):
            g1.reverse(column)
            active_player.set_tokenFalse()
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