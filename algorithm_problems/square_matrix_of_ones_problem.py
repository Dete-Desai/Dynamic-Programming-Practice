# Square matrix of ones (problem)
# Given a matrix of ones and zeros, 
# find the area of the greatest square submatrix full of ones.
# A square matrix is a matrix whose the number of rows is equal to the number of columns.

# Example:

# intput:
# matrix = [
#    [0, 0, 1, 1, 1, 0],
#    [1, 0, 1, 1, 1, 1],
#    [0, 1, 1, 1, 1, 0],
#    [1, 1, 1, 1, 0, 1],
#    [0, 1, 0, 1, 1, 1]
# ]

# output: 9

# Constraints:

# len(matrix) >= 1
# len(matrix[i]) >= 1
# matrix[i][j] is equal to 0 or 1

def rec(matrix, i, j, lookup=None):
    lookup = {} if lookup is None else lookup
    
    if i and j in lookup:
        return lookup[(i, j)]
    
    if i < 0 or j < 0 or matrix[i][j] == 0:
        return 0
    
    else:
        lookup[(i, j)] = 1 + min(rec(matrix, i-1, j, lookup), rec(matrix, i, j-1, lookup), rec(matrix, i-1, j-1, lookup))
        
        return lookup[(i, j)]
    
    
def square(matrix):
    n = len(matrix)
    m = len(matrix[0])
    max_size = 0
    lookup = {}
    
    for i in range(n):
        for j in range(m):
            max_size = max(max_size, rec(matrix, i, j, lookup))
            
    return max_size**2