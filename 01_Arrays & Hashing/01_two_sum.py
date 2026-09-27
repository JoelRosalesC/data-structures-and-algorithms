# Retornar los índices de los "two numbers" que sumados resulte en "target":

# example:
#   input: nums = [2, 7, 11, 15], target = 9
#   output: [0, 1], porque 2 + 7 = 9
#   
#   input: [3, 2, 4], target = 6 --> [1, 2]
#   input: [3, 3], target = 6 --> [0, 1]

# ----> Solution:

class Solution(object):
    def twoSum(self, nums, target):
        elements = {} # valor --> indice
        for i in range(len(nums)):
            if nums[i] in elements:
                return [elements[nums[i]], i]
            complement = target - nums[i]
            elements[complement] = i


# Prueba
if __name__ == "__main__":
    # 1. Instanciar la clase
    solucion = Solution()
    
    # 2. Definir los datos de entrada 
    nums_test = [2, 7, 11, 15]
    target_test = 9
    
    # 3. Ejecutar el método y mostrar el resultado
    resultado = solucion.twoSum(nums_test, target_test)
    print(f"Resultado esperado: [0, 1] | Tu resultado: {resultado}")