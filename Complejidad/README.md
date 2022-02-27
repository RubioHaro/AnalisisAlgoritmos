# Complejidad Algoritmica

¿Cómo se puede medir la complejidad de un algoritmo?

Pensar en el mejor caso, caso promedio, y en el peor de los casos.

## Notación

O Mayúscula (mejor)

Ommega Mayúscula (medio)

Teteta Mayúscula (peor)

$Z^+$ $\implies$ $R^+$ 

Tener en consideración:
- Las instrucciones simples
    - tiempo constante:
        - Evaluación de expresiones aritmeticass
        - Comparación de datos simples
        - Operaciones de asignación, lectura, y escritura
        - Operaciones de acceso a una componente de un array, a un campo de un registro.
        Ejemplo:

        ~~~
            def codigo(n):
                j = 20*30 + n
                return j
                
            print(codigo(1))
            print(codigo(2))
            print(codigo(3))
            print(codigo(100))

            Complejidad simple: O(1), siempre se va a tardar lo mismo independientemente del valor de n
        ~~~

- La composición de instrucciones
- Las instrucciones de selección 
- bucles
- subprogramas
