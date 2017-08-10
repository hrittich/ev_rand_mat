#!/usr/bin/env python3
#
# (C) 2017  H. Rittich
# For license information see LICENSE file.
#
from sympy import *
import random

def add_row(M, a, i1, i2):
    """ Add multiple of row i1 to row i2. """
    P = zeros(*M.shape)
    P[i2, i1] = 1
    return M + a * P * M

def add_col(M, a, j1, j2):
    """ Add multiple of column j1 to column j2. """
    Q = zeros(*M.shape)
    Q[j1, j2] = 1
    return M + a * M * Q

def alter(M, a, i, j):
    
    M = add_row(M, a, j, i)
    # Now M is invalid in the position (i, j)

    M = add_col(M, -a, i, j)
    # Matrix is fixed

    return M

def inf_norm(A):
    return max(max(A), max(-A))

def prescribed(eigenvals, prevent_growth=True, iterations=20):
    M = diag(*eigenvals)
    m,n = M.shape

    for k in range(iterations):
        # pick a position at random
        i = random.randint(0,m-1)
        j = random.randint(0,n-1)

        if i != j:
            a = random.randint(-3, 3)
            M_new = alter(M, a, i, j)

            if prevent_growth:
                # see if -a makes the inf norm smaller
                M_alt = alter(M, -a, i, j)

                if inf_norm(M_new) > inf_norm(M_alt):
                    M_new = M_alt

            M = M_new


    return M

def test():
    M = diag(3, 1, 2)
    M = alter(M,-2, 1, 0)
    M = alter(M, 3, 2, 0)
    M = alter(M, 2, 0, 1)
    M = alter(M, 1, 0, 2)
    return M

if __name__ == '__main__':
    line = input("Enter eigenvalues separated by a comma: ")
    evs = [int(i) for i in line.split(',')]

    while True:
        A = prescribed(evs)
        #print(A.eigenvals())
        pprint(A)
        yn = input('Another one (Y/n)? ')
        if yn == 'n':
            break

