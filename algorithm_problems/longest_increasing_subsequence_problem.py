# Longest increasing subsequence (problem)

# Given an array of integers arr, find the 
# length of its longest increasing subsequence, 
# its longest subsequence where each element 
# is strictly greater than the previous one.


# Example 1:

# input:
# arr = [7, 5, 2, 4, 7, 2, 3, 6, 4, 5, 12, 1, 7]
# output: 5
# explanation: A possible longest increasing 
# subsequence is [2, 3, 4, 5, 7], its length is 5

# Example 2:

# input:
# arr = [8, 5, 5, 3]

# output: 1

# explanation: The longest increasing subsequences 
# that we can make are those that contain one element only, like [8]

# Constraints:

# len(arr) >= 1

# Parameters:
#  arr: List[int]

# Return type: int

def lis(arr):
    n = len(arr)
    dp = [0]*n 
    dp[0] = 1

    for i in range(1,n):
        max_len = 0

        for j in range(i):
            if arr[j] < arr[i] and dp[j] > max_len:
                max_len = dp[j]

        dp[i] = 1+max_len

    return max(dp)