Bucles While
------------

En general las sentencias son ejecutadas secuencialmente: la primera sentencia es ejecutada el princio, seguida por la segunda, y así sucesivamente. En algunas situaciones es necesario ejecutar un bloque de código varias veces. El siguiente ejemplo imprime los números del 1 al 100 y luego "Terminado"

.. sourcecode:: python

    mynumber = 1
    while mynumber < 100:
       print(mynumber)
       mynumber = mynumber + 1
    print("Terminado!")

Los lenguages de programación proveen varias estructuras de control que permiten flujos de control más complejos, entre los que se encuentran los búcles "while" y "for".

Bucles while
------------

Los bucles "while" ejecutan las sentencias dentro de él siempre y cuando cierta condición se cumpla. Cuando la condición deja de cumplirse el flujo pasa a la línea exactamente debajo del bucle.

Bucles for
----------

Los bucles "for" tienen la habilidad de iterar sobre los items de cualquier secuencia, ya sea lista o cadena de caracteres.

.. sourcecode:: python
    ingredients = ['banana', 'manzana',  'mango']
    for ingredient in ingredients:
        print('Ingrediente actual: {}'.format(ingredient))

    for some_char in 'Python':
        print(some_char)

The previous example will generate the following output:

.. sourcecode::
    Ingrediente actual: banana
    Ingrediente actual: manzana
    Ingrediente actual: mango
    P
    y
    t
    h
    o
    n

La función "range" puede ser usada para iterar sobre una lista de números.

.. sourcecode:: python
    for number in range(100):
       print(number)
    print("Fin!")

Desafío
-------

Usando sentencias "while", "for" e "if", escribe un programa que imprima todos los números impares del 1 al 100, uno por línea.
