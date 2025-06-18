# Count sorted vowel strings (problem)
# Given an integer n, return the number of strings 
# of length n that consist only of vowels (a, e, i, o, u) 
# and are lexicographically sorted. A string s is lexicographically 
# sorted if each character comes before or same as the next one in the alphabet.


# Example 1:
# Input: n = 2
# Output: 15
# Explanation: sorted vowel strings of size 2 are:
# aa, ae, ai, ao, au, ea, ee, ei, eo, eu, ii, io, iu, oo, ou, uu

# Example 2:
# Input: n = 9
# Output: 715

# Constraints:
# n >= 1

# Parameters:
#  n: int

# Return type: int

# T(n, m) = O(1)
# S(n, m) = O(n)
def count(n):
    NB_VOWELS = 5
    previous = [1] * NB_VOWELS
    current = [0] * NB_VOWELS
    
    for i in range(1, n):
        current[0] = previous[0] + previous[1] + previous[2] + previous[3] + previous[4]
        current[1] = previous[1] + previous[2] + previous[3] + previous[4]
        current[2] = previous[2] + previous[3] + previous[4]
        current[3] = previous[3] + previous[4]
        current[4] = previous[4]
        
        for j in range(NB_VOWELS):
            previous[j] = current[j]
            
    return sum(previous)