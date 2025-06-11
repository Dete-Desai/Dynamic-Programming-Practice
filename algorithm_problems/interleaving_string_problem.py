
# Interleaving string (problem)
# Given 3 strings s1, s2, and s3, check if s3 
# can be formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration 
# where they are divided into non-empty substrings such that:

# s = s1 + s2 + ... + sn

# t = t1 + t2 + ... + tm

# |n - m| <= 1

# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

# Example:

# input:
# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"

# output: true

# explanation:
# s1 = "aabcc" = "aa" + "bc" + "c"
# s2 = "dbbca" = "dbbc" + "a"
# s3 = "aadbbcbcac" = "aa" + "dbbc" + "bc" + "a" + "c"
# You can see that we could make s3 by taking "aa" from s1, 
# "dbbc" from s2, "bc" from s1, "a" from s2, and "c" from s1

# Parameters:
#  s1: str
#  s2: str
#  s3: str

# Return type: bool

# SOLUTION 1

# T(n,m) = O(nm)
# S(n,m) = O(nm)

def inter(s1, s2, s3, i=0, j=0, lookup=None):
    
    lookup = {} if lookup is None else lookup
    
    if (i, j) in lookup:
        return lookup[(i, j)]
        
    if len(s1) + len(s2) != len(s3):
        return False
        
    elif i == len(s1) and j == len(s2):
        return True
        
    else:
        lookup[(i, j)] = (i < len(s1) and s1[i] == s3[i + j] and inter(s1, s2, s3, i + 1, j, lookup) or j < len(s2) and s2[j] == s3[i + j] and inter(s1, s2, s3, i, j + 1, lookup))
        return lookup[(i, j)]