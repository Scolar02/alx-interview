#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if it's safe to place a queen at board[row][col]

    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, results):
    # Base case: If all queens are placed, return True
    if col >= len(board):
        result = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    result.append([i, j])
        results.append(result)
        return True

    # Consider this column and try placing this queen in all rows one by one
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place the rest of the queens
            res = solve_nqueens(board, col + 1, results) or res

            # If placing queen in board[i][col] doesn't lead to a solution
            # then remove queen from board[i][col]
            board[i][col] = 0

    return res

def nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    results = []
    solve_nqueens(board, 0, results)
    for result in results:
        print(result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)
