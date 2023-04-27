#!/usr/bin/python3
""" N queens, 
Retrieves and validates this program's argument.
Returns:
int: The size of the chessboard.
"""
import sys


p=sys.argv
if len(p) != 2:
    print("Usage: nqueens N")
    exit(1) 
if not p[1].isdigit():
    print("N must be a number")
    exit(1)
if int(p[1]) < 4:
    print("N must be at least 4")
    exit(1)
    
q = int(p[1])


def cheek_queen(q, i=0, x=[], y=[], z=[]):
    """ Checks and find possible positions of queens 
    Args:
        q : list of queens.
        i: The first queen's position.
        x: lists
        y=lists
        z=lists
    """
    if i < q:
        for l in range(q):
            if l not in x and i + l not in y and i - l not in z:
                yield from cheek_queen(q, i + 1, x + [l], y + [i + l], z + [i - l])
    else:
        yield x
        
        
def solve_queens(q):
    """solve N queens problems.
    Args:
        q:list of queens
    """
    h = []
    i = 0
    for soln in cheek_queen(q, 0):
        for s in soln:
            h.append([i, s])
            i += 1
        print(h)
        h = []
        i = 0
solve_queens(q)