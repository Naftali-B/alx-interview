#!/usr/bin/python3
""" N queens backtracking """
import sys


class NQueensSolver:
    """ Class for solving the N queens problem """

    def __init__(self, n):
        """ Constructor """
        self.n = n
        self.solutions = []

    def is_safe(self, board, row, col):
        """ Check if placing a queen at (row, col) is safe """
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(self, board, row):
        """ Recursively solve N queens problem """
        if row == self.n:
            self.solutions.append(list(board))
            return
        for col in range(self.n):
            if self.is_safe(board, row, col):
                board[row] = col
                self.solve(board, row + 1)
                board[row] = -1

    def find_solutions(self):
        """ Find all solutions for N queens """
        self.solve([-1] * self.n, 0)

    def print_solutions(self):
        """ Print all found solutions """
        for solution in self.solutions:
            print([[i, col] for i, col in enumerate(solution)])


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            raise ValueError
    except ValueError:
        print("N must be a number and at least 4")
        sys.exit(1)

    solver = NQueensSolver(N)
    solver.find_solutions()
    solver.print_solutions()


if __name__ == "__main__":
    main()
