# 📍 Módulo 1 — Arrays & Hashing

## 📚 Arrays
### ¿Qué es un array?:
- Un array (también llamado arreglo, vector o matriz) es, en términos sencillos, una lista organizada de elementos que se guardan bajo el mismo nombre.
- Ej:
    - Sin array:
        - fruta1 = "Manzana", fruta2 = "fresa", ...
    - Con array:
        - frutas = ["Manzana", "Fresa", ...]
### Características más importantes:
1. Usa índices (posiciones):
    - Cada elemento tiene un nro asignado para poder encontrarlo.
    - Ej: ["elm1", "elm2", "elm3"] -> elm1 corresponde a la ***posición 0***, elm2 corresponde a la ***posición 2*** y elm3 a la ***posición 3***.
2. Tipos de datos: 
    - Dependiendo del lenguaje de programación, un array puede guardar solo un tipo de dato (ej. solo nros o texto).
### Ej de inserción y eliminación en Python:
- En Python la estructura equivalente a un array es la lista (list).
1. Insercicón:
    ```python
    frutas = ["manzana", "fresa"]
    frutas.append("platano")
    frutas.insert(1, "uva")
    frutas_extra = ["Mango", "pera"]
    frutas.extend(frutas_extra)
    ```
    - insert() agrega un elemento en una POSICIÓN ESPECÍFICA, si hacemos un print de frutas, "uva" estara en la pos 1 (manzana, uva, fresa).
    - extend() une otra lista al final de la lista que la utiliza.
2. Eliminación:
    ```python
    frutas.remove("platano")
    fruta_eliminada = frutas.pop(1) #retorna el elemento eliminado
    del frutas[0]
    frutas.clear() # borra todo
    ```

## 📚 Hash Tables
### ¿Qué es una Hash Table?
- Es una estructura de datos orientada a la búsqueda rápida. A diferencia de un array común (donde se busca por índice numérico como 0, 1, 2), en una HashTable se usa palabras/identificadores únicos como clave para encontrar directamente un valor.
    - Clave (key): Identificador único. ej: "usuario_123", "RUC", "email", ...
    - Valor (value): La información asociada. ej: {nombre: "Ana", edad: 20}
- En lenguajes populares se les conoce como:
    - dict (python)
    - Object o Map (JavaScript)
    - HashMap (Java)
### ¿Cómo funciona internamente?
- El "truco" para saber en qué posición del array va cada clave, consiste en usar una función Hash:
    1. Se proporciona una clave -> Ej: "Juan"
    2. La función Hash convierte la clave en un nro (ej: 4)
    3. El valor se guarda en la pos 4 del array interno
    4. Cuando se solicita nuevamente el valor de "Juan", se recalcula el Hash y como resultado se obtiene el 4, entonces se va directamente a esa posición en la memoria para buscarlo.
### Función de Hash:
- Es un algoritmo matemático puro que transforma cualquier entrada de texto/datos en un nro de tamaño fijo.
- Para que sirva en una HashTable debe cumplir algunas reglas clave:
    1. Determinismo: La función de Hash debe ser determinista, debe generar exactamente el mismo nro siempre (para la misma clave, no para todas).
    2. Eficiencia: Debe ser muy rápida de calcular.
    3. Distribución uniforme: Debe repartir las claves lo mejor posible a lo largo de todo el array interno para evitar amontonamientos.
### Colisiones:
- Ocurre cuando 2 claves distintas obtienen el mismo resultado despues de pasar por la función de Hash.
- Como dos datos no pueden ocupar la misma "casilla" a la vez, se usan estrategias de resolución para estos casos.
    - Direccionamiento encadenado
    - Direccionamiento Abierto (Prueba lineal, Prueba cuadrática, Doble Hash, ... )
    - ...

| Hashing Estático y Hashing Dinámico se refieren a cómo gestiona la tabla el tamaño de su memoria. 
### ¿Por qué el acceso suele ser O(1)?:
- Se dice que es constante (O(1)) porque no importa si la Hash Table tiene 10 elementos o 10.000.000:
    1. Aplicar la función Hash otorga el mismo nro siempre.
    2. Acceder a una posición de un array por su índice es directo en memoria O(1).
- No hay que recorrer elemento por elemento para buscar el que queremos O(n).
### ¿Cuándo deja de ser O(1)?:
- El rendimiento se degrada a O(n) tiempo lineal en estos escenarios:
    1. Muchas colisiones:
        - Si la función Hash es mala o la tabla esta muy llena, muchas claves terminarán en la misma casilla. En el peor caso (todas las claves en el mismo índice) la tabla se convierte en una lista enlazada y hay que recorrerlo completo.
    2. Rehash / Resizing (Redimensionamiento):
        - Cuando la tabla se llena demasiado (supera cierto Load Factor), debe crear un arraay interno más grande y volver a calcular la posición de todos los elementos existentes uno por uno.

## 📚 HashMap / Dictionary
###
- No se necesita saber en qué posición física está la información; solo conocer la etiqueta (clave) para obtener el contenido (valor)

    [ Clave ] ----(función Hash)----> [ Posición en Memoria ] -----> [ Valor ]

    "user_id" ------(aplicando función)--------- [8] ---------------- "Ana Lopez"
### ¿Cuándo usar un diccionario?:
- Idealmente:
    - Búsquedas directas por identificador único: Cuando se conoce un dato clave (ID, DNI, email, código de producto) y se necesita obtener el resto de la información en tiempo récord.
    - Conteo y frecuencias.
    - Indexación o Caché en memoria: Guardar resultados de operaciones costosas asociándolos a una clave para no tener que recalcularlos.
    - Relacionar pares de datos: Mapear equivalencias (ej: código de moneda -> tasa de cambio)
- No recomendaado:
    - Cuando el orden importa primordialmente
    - Cuando se necesita buscar por el Valor y no por la Clave: Buscar que clave tiene un valor determinado requiere revisar todo el diccionario elemento por elemento, perdiendo toda la ventaja de rendimiento.
### Operaciones Básicas:
- Búsqueda (Lookup) - O(1):
    - Se proporciona una clave, se calcula el Hash y el sistema va directamente al dato.
    - Ej: 
        ```python
        users = {"usr_101" : "Ana", "usr_102" : "carlos"}
        #Acceso directo
        nombre = users["usr_101"] # se obtiene "Ana" -> O(1)
        ```
- Inserción (Insertion) - O(1):
    - Para agregar un nuevo par clave-valor, el algoritmo calcula el hash de la clave, ubica la casilla y guarda el valor.
    - Ej:
        ```python
        #Agregar o actualizar
        users["usr_103"] = "Laura" # O(1)
        # si la clave ya existe, el valor se sobreescribe
        ``` 
- Eliminación (Deletion) - O(1):
    - Consiste en ubicar la casilla mediante el hash de la clave y remover la referencia al valor guardado.
    - Ej:
        ```python
        #Eliminación simple
        del users["usr_102"] #O(1)

        #Eliminar obteniendo el valor
        deleted_user = users.pop("usr_101", None) #O(1)
        ```

## 📚 HashSet
- Es como una bolsa transparente de elementos únicos.
- No contiene elementos repetidos.
- Los elementos no tienen un orden o posición fija.
- Podemos "meter la mano" y saber al instante si un elemento específico está dentro o no.
### ¿Cuándo usar Set?:
- Cuando se necesiten cumplir 2 condiciones:
    - Garantizar unicidad: Se necesita asegurar que no existan valores duplicados en una colección de datos.
    - Verificar pertenencia ultra rápido: Se necesita responder constantemente a la preguntaa -> ¿Este elemento ya fue procesado o existe en la lista?
### Diferencia con HashMap: 
- Por dentro, un set usa la misma tabla Hash que un diccionario, pero solo utiliza las claves. No guarda ningún valor asociado (o guarda un valor nulo interno).
### Casos de Uso:
- Eliminar duplicados de un listado.
- Rastreo de elementos visitados:
    - En algoritmos de grafos o matrices (como encontrar la salida de un laberinto), se usa un set para guardar las coordenadas (X, Y) por las que ya paso y evitar ciclos infinitos.
- Filtros de permisos o roles:
    - Guardar los permisos de un usuario para validar en nanosegundos si puede ejecutar una acción.
- Operaciones Matemáticas de conjuntos: Intersección, unión o diferencia.

## 📚 Complejidad
- O(1) - Tiempo constante (El caso ideal y común):
    - Gracias a la función de hash, no se recorre elemento por elemento para saber si un dato existe. Calcula la posición y va directo a revisar.
- O(N) - Tiempo lineal (Peor caso / Operaciones globales):
    - Poblado o conversión: Crear un set a partir de una lista de n elementos toma O(n).
    - Colisiones masivas: Si muchos elementos generan la misma posición Hash (el peor escenario teórico), la búsqueda se degrada a O(n).
    - Recorrido: Iterar sobre todos los elementos toma O(n).
- O(N^2) - Tiempo cuadrático (Malas prácticas):
    - Se recorre 2 veces una lista de n elementos dentro de un mismo bucle (ej: n x n, for dentro de otro for).