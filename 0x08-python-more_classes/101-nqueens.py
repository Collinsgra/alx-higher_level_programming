#!/usr/bin/python3
"""Solving puzzle for nqueens"""

import sys


def init_board(n):
    """initializing"""
    _board_ = []
    [_board_.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in _board_]
    return _board_


def board_deepcopy(_board_):
    """Return a deepcopy of a chessboard."""
    if isinstance(_board_, list):
        return list(map(board_deepcopy, _board_))
    return _board_


def get_solution(_board_):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(_board_)):
        for c in range(len(_board_)):
            if _board_[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def xout(_board_, row, col):
    """X out spots on a chessboard.

    All that non-playing queens are X-ed out.

    Args:
        _board_ (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(_board_)):
        _board_[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        _board_[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(_board_)):
        _board_[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        _board_[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(_board_)):
        if c >= len(_board_):
            break
        _board_[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        var = _board_[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(_board_):
            break
        _board_[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(_board_)):
        if c < 0:
            break
        _board_[r][c] = "x"
        c -= 1


def recursive_solve(_board_, row, queens, results=None):
    """solve  the N-queens puzzle recus.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        results (list): A list of lists of results.
    Returns:
        results
        :param _board_: 
        :param row: 
        :param queens: 
        :param results: 
    """
    if queens == len(_board_):
        results.append(get_solution(_board_))
        return results

    for c in range(len(_board_)):
        if _board_[row][c] == " ":
            tmp_board = board_deepcopy(_board_)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            results = recursive_solve(tmp_board, row + 1,
                                      queens + 1)

    return results


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    results = recursive_solve(board, 0, 0)
    for sol in results:
        print(sol)
