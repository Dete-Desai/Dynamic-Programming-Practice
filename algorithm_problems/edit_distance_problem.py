# Given two strings word1 and word2, 
# calculate their edit distance.
# The edit distance in this problem is 
# defined as the minimum number of 
# insertions, deletions, and substitutions 
# of characters to go from word1 to word2.

# Example:

# input:
# word1 = "inside"
# word2 = "index"

# output: 3

# explanation: To go from "inside" to 
# "index", we can delete the character 's', 
# delete the second character 'i', and 
# insert a character 'x' at the end, 
# in total we need 3 operations
# "inside" -> "inide" -> "inde" -> "index"

def dist(word1, word2):
    n, m = len(word1), len(word2)

    dp = [[0]*(m+1) for i in range(n+1)]

    for j in range(1, m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        dp[i][0] = i

    for i in range(1, n+1):
        for j in range(1, m+1):

            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[n][m]