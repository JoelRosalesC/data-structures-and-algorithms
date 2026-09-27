# Retorna true si cualquier valor aparece por lo menos dos veces en el array, 
#   y retorna false si cada elemento es distinto.

# Example:
#   input: [1, 2, 3, 1] --> True porque el elemento 1 aparece en los indices 0 y 3.
#   input: [1, 2, 3, 4] --> False
#   input: [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] --> True

# ------- Solutions --------

from collections import Counter

class Solution(object):
    # Primera version: 
    def containsDuplicate_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        checks = {}  # nros vistos
        flag = False
        for i in range(len(nums)):
            if nums[i] in checks:
                checks[nums[i]]+= 1
            else:
                checks[nums[i]] = 1
            
            if checks[nums[i]] == 2:
                flag = True
                break
        
        return flag

    # Segunda version: otra idea (pseudo talvez)
    def containsDuplicate_v2(self, nums):
        count = Counter(nums) # Crea un diccionario con las frecuencias
        for val in count.values():
            if val > 1:
                return True
        return False
    # si o si esta obligado a contar todos los numeros O(n)

    # Tercera version: 
    def containsDuplicate_v3(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        checks = set() # vistos
        for num in nums:
            if num in checks:
                return True         # Puede revisar todos los nros (O(n)), pero tambien permite retorno
            checks.add(num)         # temprano, por ej -> [1, 1, 2, 3]: se detiene en el segundo elemento.
        
        return False

    # Óptima: Comparación de longitudes
    def containsDuplicate_v4(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums)) # sin son diferentes ambas longitudes, significa que se eliminaron elementos repetidos


#Prueba
if __name__ == "__main__":
    solucion = Solution()
    
    # Casos de prueba
    test_1 = [1, 2, 3, 1] # Debe dar True
    test_2 = [1, 2, 3, 4] # Debe dar False
    
    print("--- Probando Test 1 [1, 2, 3, 1] ---")
    print(f"V1: {solucion.containsDuplicate_v1(test_1)}")
    print(f"V2: {solucion.containsDuplicate_v2(test_1)}")
    print(f"V3: {solucion.containsDuplicate_v3(test_1)}")
    print(f"Óptima: {solucion.containsDuplicate_v4(test_1)}\n")

    print("--- Probando Test 2 [1, 2, 3, 4] ---")
    print(f"Óptima Test 2: {solucion.containsDuplicate_v4(test_2)}")
    