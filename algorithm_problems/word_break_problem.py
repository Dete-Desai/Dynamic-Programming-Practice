# Word break (problem)
# Given a string s and a list of words, 
# check if we can break s into words from the list 
# (A same word can be used multiple times).

# Example:
# input:
# s = "catsandogsareanimals"
# words = ["cats", "dog", "sand", "and", "cat", "mals", "san", "dogs", "are", "animal", "ani", "og", "sar"]
# output: true
# explanation: s is also equal to "cat"+"san"+"dogs"+"are"+"ani"+"mals", and all of these parts are in words

# Constraints:
# len(s) >= 1
# len(words) >= 1
# len(words[i]) >= 1

# Parameters:
#  s: str
#  words: List[str]
# Return type: bool

# SOLUTION ONE

# T (n, m, k) = O(k^3)
# S (n, m, k) = O(k)

def word_break(s, words):
    
    def rectangle(s, words, i = 0, lookup = None):
        
        lookup = {} if lookup is None else lookup
        
        if i in lookup:
            return lookup[i]
        
        if i == len(s):
            return True
        
        else:
            for j in range(i + 1, len(s) + 1):
                
                if s[i:j] in words and rectangle(s, words, j, lookup):
                    lookup[i] = True
                    return lookup[i]
                
            lookup[i] = False
            return lookup[i]
        
    words = set(words)
    return rectangle(s, words)

# SOLUTION TWO

# T (n, m, k) = O(k^2 + nm)
# S (n, m, k) = O(k + m)

# class Trie:
#     def __init__(self, is_end=False):
#         self.children = {}
#         self.is_end = is_end
 
#     def insert(self, s):
#         node = self
#         for ch in s:
#             if ch not in node.children:
#                 node.children[ch] = Trie()
#             node = node.children[ch]
#         node.is_end = True
 
 
# def word_break(s, words):
#     k = len(s)
#     trie = Trie()
#     for word in words:
#         trie.insert(word)
#     dp = [False]*(k+1)
#     dp[0] = True
#     for i in range(len(s)):
#         node = trie
#         for j in range(i, len(s)):
#             if s[j] not in node.children:
#                 break
#             node = node.children[s[j]]
#             if node.is_end and dp[i]:
#                 dp[j+1] = True
#     return dp[k]
        