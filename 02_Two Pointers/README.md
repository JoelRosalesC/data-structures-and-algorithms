# 📍 Módulo 2 — Two Pointers

### ¿Qué es Two Pointers?:
- Es una técnica para recorrer una estructura lineal - normalmente un array o string - utilizando dos índices que se mueven de manera coordinada.
- Ej: 
    ```python
    nums = [1, 2, 3, 4, 5, 6]
    left = 0
    right = len(nums) - 1
    # ---> 
    #      [1, 2, 3, 4, 5, 6]
    #     left            rigth
    ```
- Podemos moverlos y eventualmente pueden coincidir en la misma posición.
- **La idea importante es:** No tenemos dos punteros simplemente porque hay dos índices. Los tenemos porque necesitamos controlar dos posiciones del array simúltaneamente.
### ¿Por qué podemos mover un pointer sin tener que revisar todas las posibilidades?:
- Aquí es donde esta la verdadera razón por la que Two Pointers puede convertir una solución que ingenuamente sería O(n^2) en una O(n).
- Ej:
    - Supongamos un array ordenado: 
    ```python
          [1, 2, 4, 6, 8, 10] 
    #    left            Rigth
    ```
    - y queremos encontrar dos nros cuya suma sea 11.
    - Tenemos 1 + 10 = 11 -> Encontrado rápidamente
    - Y si en lugar de 10, sea este un 9. 1 + 9 = 10 -> distinto y menor que 11.
        - Si se sabe de antemano que el array esta ordenado y la suma de L + R ya es menor que 11. Mover R hacia la izquierda solamente haría que la suma fuera todavía menor.
        - No tiene sentido mover R, pero si tiene sentido mover L
            ```python
                  [1, 2, 4, 6, 8, 9] 
            #        left        Rigth
            ```
        - L + R = 2 + 9 = 11 -> Encontrado
        - Este razonamiento es el corazon del patrón, no estamos probando combinaciones al azar. Estamos descartando posibilidaades que sabemos que no pueden funcionar.
- **Two Pointers** funciona cuando la información que tenemos nos permite decidir que pointer mover y, al hacerlo, descartar posibilidades sin revisarlas individualmente.
### ¿Qué tiene que ver esto con O(n^2)?:
- Imaginemos que se tiene n elementos y queremos probaar todas las parejas posibles.
- Una solución ingenua podría hacer:
    ```python
    for i in range(n):
        for j in range(i+1, n):
            # code ...
    ```
- En el peor caso estamos considerando aproximadamente todas las parejas: n x n -> O(n^2).
- Tener dos pointers no significa automaticamente O(n).
### Cuándo y por qué funciona Two Pointers?:
- Two pointers no consiste simplemente en tener dos índices, consiste en poder moverlos de manera inteligente y descartar posibilidades.
1. ¿Cuándo suele aparecer Two Pointers?
    - Hay varios escenarios muy frecuentes, por ejemplo uno de ellos es el Array ordenado
    - Si avanzo -> Los valores no disminuyen
    - Si retrocedo -> Los valores no aumentan
2. La propiedad que realmente necesitamos:
    - Monoticidad: Algo es monotónico cuando, al movernos en una dirección, sabemos que cierto valor solo puede aumentar o solo puede disminuir.
3. Otro caso típico: Comparar los extremos
    - Two pointers no se limita a buscar sumas.
    - Otro escenario muy común es comparar elementos desde ambos extremos.
    - Por ejemplo, comprobar si un string es palíndromo:
        ```python
        palabra -> "racecar"
        # -->
        #         r a c e c a r
        #         L           R    ---> L = R
        # Then:     L       R      ---> L = R
        ```
4. Otro caso típico: Dos posiciones que recorren en la misma dirección
    - No todos los pointers empiezan en los extremos.
    - Ej:
        ```python
        [1, 1, 2, 2, 3, 3]
        #    i-->
        #    j-->
        ```
    - Uno de los pointers puede representar una posición de escritura/resultado y otro una posición de exploración.
    - Esto aparece por ejemplo, en problemas donde queremos:
        - Eliminar duplicados
        - Compactar elementos
        - Modificar un array "in-place"
        - Fusionar o recorrer secuencias
        - Separar determinados elementos
5. ¿Qué señales deberíamos buscar?
    - Suele aparecer en estructuras lineales.
    - ¿Estoy buscando una relación entre dos elementos?, por ej:
        - Dos nros que sumen un valor en específico.
        - Dos elementos que cumplan una condición.
        - Extremos que deban coincidir.
        - Pares
        - Diferencias
        - Comparaciones
    - ¿Puedo mover un índice y saber qué posibilidades estoy descartando?
6. Explicación para el primer ejemplo:
    - "Como los elementos estan ordenados, puedo determinar qué región ya no puede contener una solución después de comparar los extremos. Por eso puedo mover uno de los punteros y descartar múltiples posibilidades a la vez. Cada puntero avanza como máximo a través del arreglo una vez, por lo que el recorrido es O(n) y no se necesita espacio adicional."