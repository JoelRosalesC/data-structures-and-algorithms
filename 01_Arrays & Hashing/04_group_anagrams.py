# Dado un array de strings, agrupar los anagramas juntos. Se puede retornar la respuesta en cualquier orden.

# Example:
#   input: str = ["eat", "tea", "tan", "ate", "nat", "bat"]
#       --> [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

# ------- Solutions --------
class Solution(object):
    def groupAnagrams(self, strs):
        dic = {} # anagram --> lista de sus otros anagramas
        for word in strs:
            key = "".join(sorted(word))
            dic[key].append(word)
        return list(dic.values())