# Paths in matrix (problem)
# Given a matrix where a cell has the value of 1 if it's a wall and 0 if not, 
# find the number of ways to go from the top-left cell to the bottom-right cell, 
# knowing that it's not possible to pass from a wall and we can only go to the right or to the bottom

# Example:

# input:
# matrix = [
#     [0, 0, 1, 0, 1],
#     [0, 0, 0, 0, 1],
#     [0, 0, 1, 0, 0],
#     [1, 0, 0, 0, 0]
# ]

# output: 7

def paths(matrix, i = 0, j = 0):
    n, m = len(matrix), len(matrix[0])

    if i == n or j == m or matrix[i][j] == 1:
        return 0
    
    elif i == n-1 and j == m-1:
        return 1
    
    else:
        return paths(matrix, i + 1, j) + paths(matrix, i, j + 1)
