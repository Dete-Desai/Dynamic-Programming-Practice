
# Shortest common 
# supersequence (problem)
# Given two strings s1 and s2, find the 
# length of their shortest common supersequence, 
# the shortest string that has both s1 and s2 subsequences.

# A string A is a supersequence of a 
# string B if B is a subsequence of A.

# Example:

# input:
# s1 = "abdacebfcab"
# s2 = "acebfca"

# output: 11

# explanation: The shortest common supersequence 
# of s1 and s2 is "abdacebfcab", its length is 11

def scs(s1, s2, i=0, j=0, lookup=None):
    lookup = {} if lookup is None else lookup

    if(i,j) in lookup:
        return lookup[(i,j)]
    
    if i == len(s1):
        return len(s2)-j
    
    if j == len(s2):
        return len(s1)-i 
    
    elif s1[i] == s2[j]:
        lookup[(i,j)] = 1 + scs(s1, s2, i+1, j+1, lookup)
        return lookup[(i,j)]

    else:
        lookup[(i,j)] = 1 + min(scs(s1, s2, i+1, j, lookup), scs(s1, s2, i, j+1, lookup))
        return lookup[(i,j)]