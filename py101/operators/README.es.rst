Operators
---------

Hay cinco tipos básicos de operadores en Python. Los aritméticos, concatenación y duplicación.

Como muchos lenguajes de programación, los números pueden interactuar usando la adición (+), substracción (-), división (/) y resto de división (%) que es conocido como el operador módulo. Los paréntesis pueden ser usados para agrupar expresiones, que puede ayudar a eliminar la ambigüedad y mejorar la legibilidad del código.

.. sourcecode:: python

    the_order = 1 + 2 * 3   # 7
    matters   = (1 + 2) * 3 # 9

    some_division = 22 / 8  # 2.75
    remainder = 22 % 8      # 6

Usar dos símbolos de multiplicación permite exponenciar el resultado.

.. sourcecode:: python

    big_number = 2 ** 8      # 256
    small_number = 2 ** (-8) # 0.00390625

Tanto las cadenas como las listas pueden ser concatenadas usando el operador +, como en el siguiente ejemplo:

.. sourcecode:: python

    hello = 'hello' + ' ' + 'world' # 'Hello World'
    prime_numbers = [1,3,5,7]
    other_numbers = [2,4,6,8,9]
    print(prime_numbers + other_numbers) # Prints [1, 3, 5, 7, 2, 4, 6, 8, 9]

Las cadenas y las listas pueden ser duplicadas para formar secuencias más grandes usando el operador de multiplicación.

.. sourcecode:: python

    print('lo' * 10 + 'l') # prints lolololololololololol
    print([0,3] * 2 + [4,5,6]) # prints [0, 3, 0, 3, 4, 5, 6]

Desafío
---------

Haz un programa que imprima la cadena 'ka' 108 veces utilizando dupliación de cadenas.
