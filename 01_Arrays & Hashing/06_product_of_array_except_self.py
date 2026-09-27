# Dado un arraay de enteros [nums], retornar un array [answer] donde cada [answer[i]] es igual al producto 
# de todos los elementos de [nums] excepto si mismo [nums[i]].

# Example:
#   input: nums = [1, 2, 3, 4] --> [24, 12, 8, 6]
#   input: nums = [-1, 1, 0, -3, 3] --> [0, 0, 9, 0, 0]

# ------- Solutions --------
class Solution(object):
    # Primera version: (PseudoCode) Calculr el producto de todo el array, dividir para answer[i] -> prod_total/nums[i]
    def productExceptSelf_v1(self, nums):
        prod_total = 1
        
        answer = []; i = 1 # Declarados solo para quitar el error.

        for num in nums:
            prod_total += prod_total * num

        for num in nums:
            answer[i] = prod_total/num

        return answer # ERROR: El enunciado menciona explicitamente que no se permite el uso de la operación división ("/")
                      #         y aunque se pudiera, hay casos donde prod_total = 0.

    # Segunda version:
    def productExceptSelf_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)  # Declarando array
        product = 1
        for i in range(len(nums)):
            left[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(len(nums)-1, -1, -1):    # range(inicio, límite, paso)
            left[i] = left[i] * product 
            product *= nums[i]

        return left      
    # Algunas correcciones como: 
    #   left --> answer
    #   product = product * ... ---> product *= ...