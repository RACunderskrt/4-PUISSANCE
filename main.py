from game import Game
from player import Player
from display import Display

from colorama import Fore

def play_game():
    print("Jeu de puissance 4", end="\n\n")
    p1 = Player("A")
    p2 = Player("B")
    active_player = None

    g1 = Game(p1, p2)
    grid = g1.get_grid()

    Display.display(g1)

    while not g1.verify_all():
        active_player = p2 if active_player == p1 else p1
        print("Player " + active_player.get_char())
        column = None
        while column is None or column < 1 or column > 7:
            try:
                column = int(input("Enter column (1-7): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 7.")
        print()
        g1.insert(column - 1, active_player)
        Display.display(g1)

    if g1.verify_all():
        print("Player " + active_player.get_char() + " won")
    else:
        print("Draw")

def main():
    print("in main")
    print(Fore.RED + 'some red text')

if __name__ == '__main__':
    main()