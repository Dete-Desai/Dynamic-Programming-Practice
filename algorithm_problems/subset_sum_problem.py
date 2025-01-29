# Subset sum (problem)
# Given an array arr of strictly positive integers, 
# and an integer k, create a function that returns 
# the number of subsets of arr that sum up to k.

# Example 1:

# input:
# arr = [1, 2, 3, 1]
# k = 4

# output: 3

# explanation: subsets that sum up to k 
# are [1, 2, 1], [1, 3], and [3, 1]

# Example 2:

# input:
# arr = [1, 2, 3, 1, 4],
# k = 6

# output: 4

# explanation: subsets that sum up to k 
# are [1, 2, 3], [1, 1, 4], [2, 3, 1], and [2, 4]

# Example 3:

# input:
# arr = [2, 4, 2, 6, 8]
# k = 7

# output: 0

# explanation: there are no subsets that sum up to k

# Constraints:

# k >= 1
# arr[i] >= 1

# Parameters:
#  arr: List[int]
#  k: int

# Return type: int

def subsets(arr, k, i=0, lookup = None):
    lookup = {} if lookup is None else lookup

    if k == 0:
        return 1
    
    if i == len(arr) or k < 0:
        return 1
    
    elif i in lookup:
        return lookup[(i,k)]
    
    else:
        lookup[(i,k)] = subsets(arr, k - arr[i], i+1, lookup) + subsets(arr, k, i+1, lookup)

        return lookup[(i,k)]
    