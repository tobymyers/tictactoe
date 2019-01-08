from tictac import TicTac
import time

def main():
    print("Welcome to Tic Tac Toe")
    game = TicTac()
    game.print()
    while True:
        game.player_turn()
        game.cats()
        game.find_win()
        if game.cats() or game.find_win():
            break
        game.computer_turn()
        game.cats()
        game.find_win()
        if game.cats() or game.find_win():
            break
main()
