
# Longest common subsequence (problem)

# Given two strings s1 and s2, 
# find the length of their longest common subsequence.
# A subsequence of a string s is a subset of its characters that 
# are not necessarily adjacent but have to be in the right order.

# Example:

# input:
# s1 = "abdacbab"
# s2 = "acebfca"

# output: 4

# explanation: A possible longest common subsequence of s1 and s2 is "abca"

def lcs(s1, s2, i = 0, j = 0, lookup = None):
    lookup = {} if lookup is None else lookup

    if (i, j) in lookup:
        return lookup[(i, j)]
    
    if i == len(s1) or j == len(s2):
        return 0
    
    elif s1[i] == s2[j]:
        lookup[(i, j)] = 1 + lcs(s1, s2, i + 1, j + 1, lookup)
        return lookup[(i, j)]
    
    else:
        lookup[(i,j)] = max(lcs(s1, s2, i + 1, j), lcs(s1, s2, i, j + 1))
        return lookup[(i, j)]