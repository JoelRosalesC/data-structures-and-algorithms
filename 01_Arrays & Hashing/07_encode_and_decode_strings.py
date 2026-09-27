# Se tiene una lista de strings ["hello", "world"]. 
# Implementar dos funciones:
#   Encode: Convierte la lista de strings en un solo string
#   Decode: Debe poder tomar ese único string y reconstruir exactamente la lista original.
# Los strings pueden contener cualquier carácter, incluyendo espacios, símbolos, nros, etc...

# ------- Solutions --------
class Solution(object):
    def encode(self, list_str):
        code = ""
        for s in list_str:
            cant = len(s)
            code += str(cant) + "#" + s

        return code

    def decode(self, strg):
        i = 0; list_str = []; cant = ""
        while i < len(strg):
            char = strg[i]
            cant += char
            i += 1
            if char == "#":
                lenght = int(cant)
                cant = ""
                s = strg[i:i+lenght]
                list_str.append(s)
                i += lenght
        return list_str