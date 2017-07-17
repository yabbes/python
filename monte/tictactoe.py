#! /usr/bin/env python3
# tic tac toe game :P

import random
import sys


board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

win_stacks = []
win_stacks.append(list((0, 3, 6)))
win_stacks.append(list((1, 4, 7)))
win_stacks.append(list((2, 5, 8)))
win_stacks.append(list((0, 1, 2)))
win_stacks.append(list((3, 4, 5)))
win_stacks.append(list((6, 7, 8)))
win_stacks.append(list((0, 4, 8)))
win_stacks.append(list((2, 4, 6)))


def show_board():
    print("{} | {} | {}\n"
          "{} | {} | {}\n"
          "{} | {} | {}\n".format(
            board[0], board[1], board[2],
            board[3], board[4], board[5],
            board[6], board[7], board[8]))


def main():
    print("Welcome to basic Tic Tac Toe\n"
          "To quit game, enter q"
          "\n")
    while True:
        show_board()
        print("Where do you want to place your move?")
        player_move = input()
        if player_move is 'q':
            sys.exit(0)
        else:
            player_move = int(player_move)
        if not check_if_occupied(player_move):
            board[player_move] = "O"
        else:
            while True:
                print("place taken")
                print("Where do you want to place your move?")
                player_move = int(input())
                if not check_if_occupied(player_move):
                    board[player_move] = "O"
                    break
        # computer move
        computer_move = random.randint(0, 8)
        if not check_if_occupied(computer_move):
            board[computer_move] = "X"
        else:
            while True:
                computer_move = random.randint(0, 8)
                if not check_if_occupied(computer_move):
                    board[computer_move] = "X"
                    break

        print("The computer played X on {}".format(computer_move))
        computer, player = "X", "O"
        if (check_win_condition(player)):
            print("Player wins")
            show_board()
            sys.exit(0)
        elif (check_win_condition(computer)):
            print("Computer wins")
            show_board()
            sys.exit(0)


def check_if_occupied(n):
    if isinstance(board[n], int):
        return False
    else:
        return True


def check_win_condition(cible):
    for stack in win_stacks:
        j = 0
        for i in stack:
            if board[i] is cible:
                j += 1
                if j is 3:
                    return True

    return False


if __name__ == '__main__':
    main()
