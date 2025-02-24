# Partition (problem)
# Given an array of strictly positive integers arr, 
# check if we can split it into two subsets that have 
# the same sum of elements.

# Example 1:

# input:
# arr = [4, 5, 3, 2, 5, 1]

# output: true

# explanation: We can split arr into [4, 3, 2, 1] and [5, 5], and they have the same sum
# 4+3+2+1 = 5+5 = 10

# Example 2:

# input:
# arr = [5, 6, 2, 3, 8, 1]

# output: false

# explanation: We can't split arr into two subsets that have the same sum

# Constraints:

# len(arr) >= 1
# arr[i] >= 1

def subsets(arr, k):
    n = len(arr)
    
    if k > sum(arr) or n == 0:
        return 0
    
    dp = [[0] * (k+1) for i in range(n)]
    dp[0][0] = 1
    
    if arr[0] <= k:
        dp[0][arr[0]] = 1
        
    for i in range(1, n):
        for j in range(k + 1):
            dp[i][j] = dp[i-1][j] + (dp[i-1][j - arr[i]] if j - arr[i] >= 0 else 0)
            
    return dp[n - 1][k]
    
def partition(arr):
    
    s = sum(arr)
    
    if s%2 == 1:
        return False
    else:
        return subsets(arr, s//2) > 0
    
    
# First, the subsets function takes an array arr and an integer k. 
# The goal seems to be to find the number of subsets of arr that sum up to k. Let me check the code.
# In subsets, the first line calculates n as the length of arr. 
# Then there's a check: if k is greater than the sum of arr or if the array is empty, return 0. 
# That makes sense because if the target k is bigger than the total sum, 
# there's no way to get that subset. Also, an empty array can't have subsets.

# Then, they initialize a 2D array dp with n rows and k+1 columns. dp[0][0] is set to 1. 
# This probably represents that there's one way to make sum 0 with zero elements. 
# Then, if the first element is less than or equal to k, dp[0][arr[0]] is set to 1. 
# That means if the first element itself is a valid sum, there's one subset (the element itself).

# Then, the loops: for each i from 1 to n-1, and for each j from 0 to k, 
# they calculate dp[i][j] as dp[i-1][j] plus dp[i-1][j-arr[i]] if j >= arr[i]. 
# This looks like the standard dynamic programming approach for subset sum problem, 
# where each entry dp[i][j] represents the number of ways to get sum j using the first i elements. 
# So the recurrence is adding the number of ways without including the current element and the number of ways including it.

# Wait, but the problem here is that the standard subset sum counts the number of subsets. 
# So this function is returning the number of subsets that sum to k. Then, 
# the partition function is checking if the array can be partitioned into two subsets with equal sum. 
# The partition function first checks if the total sum is even. If not, returns False. 
# If it's even, then it checks if there's at least one subset that sums to s/2 by calling subsets(arr, s//2) and checking if the count is greater than 0.

# But wait, the partition problem is about whether such a subset exists, 
# not how many there are. So the subsets function is counting the number of subsets, 
# and partition returns True if that count is more than zero. That makes sense.

# But wait, in the standard partition problem, even if there is one subset that sums to half the total, 
# it's possible. So this code is correct in that sense. However, there's a possible issue here. 
# The dynamic programming approach here is counting the number of subsets, including those that might be empty. 
# Wait, no. Because the initial condition is dp[0][0] = 1, which represents the empty subset. But when we compute the subsets for sum s/2, 
# including the empty subset would not be valid unless the total sum is zero, which is not the case here. 
# Wait, but in the context of the partition problem, s is the sum of the array, which is even. 
# So s/2 can't be zero unless all elements are zero. But in that case, it's possible.

# Wait, but the code returns subsets(arr, s//2) > 0. Suppose the array is [2, 2]. 
# The total sum is 4, so s//2 is 2. The subsets function would count the number of subsets that sum to 2. 
# For this array, there are two subsets: the first element and the second. 
# So the count is 2. Thus, partition would return True, which is correct.

# But another example: [1,1]. Sum is 2, s//2 is 1. 
# Subsets returns 2, so partition returns True. So the code works for these cases.

# But what about a case where the sum is even, 
# but there's no way to split it? Like [1,2,5]. Sum is 8, s//2 is 4. 
# But there's no subset that sums to 4. So subsets returns 0, and partition returns False. That's correct.

# So the code seems correct. However, the way the DP is set up counts the number of subsets. 
# But for the partition problem, we only need to know if there's at least one subset. 
# So this code is using a count method, but it's correct as long as the count is non-zero.

# But let's check the base case. What if the array is empty? The subsets function returns 0. 
# So partition would return False, which is correct.

# Another edge case: arr = [3,1]. Sum is 4, so s//2 is 2. 
# There's a subset [1], but 1 is not equal to 2. Wait, no. Wait, the sum of 3 and 1 is 4. 
# The subsets that sum to 2: none. So partition returns False. Correct.

# But wait, wait: 3 is larger than 2. So the subsets can't have 3. 
# So the code would return 0 for subsets([3,1], 2), hence partition returns False. Correct.

# So the code is correctly solving the partition problem by checking 
# if there's at least one subset that sums to half of the total sum.

# So in summary, the partition function checks if the array can be divided into two subsets with equal sums. 
# The subsets function uses dynamic programming to count the number of subsets that add up to k, 
# and partition uses this to check if such a subset exists.

# The code is solving two related problems:

# subsets(arr, k) Function:

# Purpose: Counts the number of subsets of the array arr that sum up to exactly k.

# Approach: Uses dynamic programming (DP) with a 2D table dp, where:

# dp[i][j] = Number of ways to achieve sum j using the first i elements.

# Base cases: There’s 1 way to make sum 0 (empty subset), and 1 way to make sum arr[0] (if valid).

# Transition: For each element, either include it (if possible) or exclude it.

# partition(arr) Function:

# Purpose: Determines if the array arr can be split into two subsets with equal sums.

# Logic:

# If the total sum of arr is odd, returns False (impossible to split evenly).

# If even, checks if there’s at least one subset summing to sum(arr)//2 using subsets(arr, s//2) > 0.

# Key Observations:
# Partition Problem: The code solves the classic "Equal Subset Sum Partition" problem.

# Efficiency: The DP approach has a time complexity of O(n * k), where n is the array length and k is the target sum.

# Edge Cases:

# Handles empty arrays and invalid targets gracefully.

# Correctly returns False when the total sum is odd.

# Example:
# For arr = [1, 5, 11, 5]:

# Total sum = 22 (even), so s//2 = 11.

# subsets(arr, 11) returns 2 (subsets [11] and [5, 5, 1]).

# partition(arr) returns True because there’s at least one valid subset.