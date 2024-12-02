# House robber (problem)
# Given an array of integers arr where arr[i] represents the amount of money in the house i, 
# you are asked to find the maximum amount of money that a robber can steal knowing that 
# he can't steal two adjacent houses because the security systems would automatically call the police

# Example:
# input: arr = [2, 10, 3, 6, 8, 1, 7]
# output: 25
# explanation: The greatest amount of money that a robber can get is 25, 
# by the stealing the house 1, 4, and 6 (arr[1]+arr[4]+arr[6] = 10+8+7 = 25)

# Constraints:

# len(arr) >= 1
# arr[i] >= 0

def rob(arr, i=0, lookup=None):
    lookup = {} if lookup is None else lookup

    if i in lookup:
        return lookup[i]
    
    if i >= len(arr):
        return 0
    
    # Calculate the max loot recursively
    else:
        lookup[i] = max(arr[i] + rob(arr, i + 2, lookup), rob(arr, i + 1, lookup))
        print(f'The value of the items found in the houses is worth: {lookup[i]}')
        return lookup[i]
