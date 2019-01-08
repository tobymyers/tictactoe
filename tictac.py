from random import randint
import time

class TicTac:
    def __init__(self):
        row = ["-", "-", "-"]
        #self.board = [row for i in range(3)]
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    def print(self):
        [print(self.board[i][0]+"|"+self.board[i][1]+"|"+self.board[i][2]) for i in range(3)]


    def find_win(self):
        w = ["X","X","X"]

        col_check = [[self.board[i][j] for i in range(3)] for j in range(3)]
        diag_check1 = [[self.board[i][i] for i in range(3)]]
        diag_check2 = [[self.board[0][2], self.board[1][1], self.board[2][0]]]
        #print(col_check, 'c', diag_check1, 'd1',diag_check2, 'd2')
        if w in self.board or w in col_check or w in diag_check1 or w in diag_check2:
            print("You Win!!")
            return True

        l = ["O","O","O"]
        if l in self.board or l in col_check or l in diag_check1 or l in diag_check2:
            print("You Lose :()")
            return True

        return False



    def player_turn(self):
        while True:
            move = eval(input("Your turn!  Choose a [row,col] e.g. [0,1]   "))
            if self.board[move[0]] [move[1]] in ['X','O']:
                print("that spot's already been taken")
            else:
                self.board[move[0]] [move[1]] = "X"
                print("move recorded")
                break
        self.print()
        time.sleep(1)

    def cats(self):
        cat = [val for row in self.board for val in row if val == "-" ]
        if len(cat) == 0:
            print("Cat's Game :/ for sure")
            return True
        return False

    def computer_turn(self):
        print("my turn...")
        while True:
            move = (randint(0,2), randint(0,2))
            if self.board[move[0]] [move[1]] not in ('X','O'):
                self.board[move[0]] [move[1]] = "O"
                break
        self.print()
        time.sleep(1)
