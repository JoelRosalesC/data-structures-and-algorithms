# Dos strings "s" y "t", retornan true si t es un anagrama de s, y false caso contrario.

# Example:
#   input: s = "anagram", t = "nagaram" --> True
#   input: s = "rat", t = "car" --> False

# ------- Solutions --------
from collections import Counter as C

class Solution(object):
    # Primera version:
    def isAnagram(self, s, t):
        return C(s) == C(t)

    # Segunda version:
    def isAnagram_v2(self, s, t):
        if len(s) != len(t):
            return False
        return C(s) == C(t)
