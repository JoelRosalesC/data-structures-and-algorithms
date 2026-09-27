# Dado un array de enteros [nums] y un entero [k], retornar los [k] elementos
# más frecuentes. Se puede retornar la respuesta en cualquier orden.

# Example:
#   input: nums = [1, 1, 1, 2, 2, 3], k = 2 --> [1, 2] 
#   input: nums = [1], k = 1 --> [1]
#   input: nums = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2], k = 2 --> [1, 2]

# ------- Solutions --------
from collections import Counter

class Solution(object):
    # Primera version
    def topKFrequent_v1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequently = Counter(nums) #contamos frecuencia key -> frecuencia
        
        frequently_ordenado = sorted(frequently.items(), key=lambda item: item[1]) #ordenamos por el valor
        
        res = list(frequently_ordenado)[-k:] #obtenemos los k elementos con mayor frecuencia 

        print(res)

        lis = []
        for item in res:
            lis.append(item[0]) #obtenemos solo los "keys"
        
        return lis

    # Segunda version:
    def topKFrequent_v2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequently = Counter(nums) #contamos frecuencia key -> frecuencia
        
        sorted_items = sorted(
            frequently.items(), 
            key=lambda item: item[1]
        ) #ordenamos por el valor
        
        res = sorted_items[-k:] #obtenemos los k elementos con mayor frecuencia 

        return [item[0] for item in res]

    # Otras soluciones: "Heap" - "Bucket Sort"
    def topKFrequent_buckect_sort(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result = []

        for count in range(len(buckets) - 1, 0, -1):

            for num in buckets[count]:
                result.append(num)

                if len(result) == k:
                    return result