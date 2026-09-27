# Dado un array de enteros desordenado [nums], retornr la longitud más larga de la ssecuencia consecutiva de elementos

# Example:
#   input: nums = [100, 4, 200, 1, 3, 2] ---> 4
        #Explicación: La secuencia consecutiva de elementos más larga es [1,2,3,4], tamaño 4.
#   input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] ---> 9
#   input: nums = [1, 0, 1, 2] ---> 3

# ------- Solutions --------
class Solution(object):
    # Primera versión: Ordenar y luego recorrer actualizando una variable
    def longestConsecutive_v1(self, nums):
        cont = 0; ult = 0; ult_count = 0; first = True
        nums_sorted = sorted(nums)
        for i in range(len(nums)):
            if first:
                first = False; ult = nums_sorted[i]; continue
            if nums_sorted[i] == ult or nums_sorted[i] != (ult+1):
                ult_count = cont; cont = 0
            cont += 1
        return ult-cont     # Muchos errores de lógica, descartado totalmente

    # Segunda versión:
    def longestConsecutive_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        cont = 1
        ult = 0
        ult_count = 0
        first = True
        nums_sorted = sorted(nums)

        for i in range(len(nums_sorted)):
            if (first):
                first = False
                ult = nums_sorted[i]
                continue
            if (nums_sorted[i] == ult) or (nums_sorted[i] != (ult+1)):
                if (cont > ult_count):
                    ult_count = cont
                if i < len(nums)-1 and nums_sorted[i+1] != (ult+1):
                    cont = 1
            if (nums_sorted[i] == (ult+1)):
                cont += 1
            
            ult = nums_sorted[i]
            
        if cont > ult_count:
            return cont
        else:
            return  ult_count   # No paso la prueba -> para [] retorna 1 lo cual es un error, se espera retorne 0.

    # Tercera versión:
    def longestConsecutive_v3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        cont = 1
        ult = 0
        ult_count = 0
        first = True
        nums_sorted = sorted(nums)

        for i in range(len(nums_sorted)):

            if (first):
                first = False
                ult = nums_sorted[i]
                continue

            if nums_sorted[i] > ult:    # si es igual se ignora
                if nums_sorted[i] == (ult+1):
                    cont +=1
                else:
                    if cont > ult_count:
                        ult_count = cont
                    cont = 1
            
            ult = nums_sorted[i]

        return max(cont, ult_count)

    # Cuarta versión: Usando set pero aun sigue siendo O(n log n)
    def longestConsecutive_v4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        cont = 1
        ult_count = 0
        n = sorted(set(nums))   # sorted: O(n log n) - set: O(n)
        ult = n[0]

        for i in range(1, len(n)):
            if n[i] == (ult+1):
                cont += 1
            else:
                if cont > ult_count:
                    ult_count = cont
                cont = 1
            ult = n[i]

        return max(cont, ult_count)

    # Versión óptima: O(n) espacio y tiempo
    def longestConsecutive_optima(self, nums):
        if not nums:
            return 0
        
        nums_set = set(nums); longest = 0

        for num in nums_set:
            if num-1 not in nums_set: # solo empezamos a contar si num es el comienzo de una secuencia
                current = num
                count = 1

                # Buscamos los siguientes nros consecutivos:
                while current+1 in nums_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest