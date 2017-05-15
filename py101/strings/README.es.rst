Operations con cadenas de caracteres
------------------------------------

Las cadenas de caracteres son uno de los tipos más usados en Python. Son un tipo de secuenca de caracteres. Para acceder a los substring se debe usar los paréntesis rectos para indicar qué partes de la cadena se pueden obtener. Se pueden usar índices negativos para contar desde el final.

.. sourcecode:: python

    mystring = 'Show me the code'
    print(mystring[0])   # Imprime S
    print(mystring[0:4]) # Imprime Show
    print(mystring[-4:]) # Imprime code

La función "len" puede ser utilizada para obtener el largo de una cadena

.. sourcecode:: python

    print(len('hola'))  # Imprime 4

Adicionalmente hay una variedad de funciones para transformar o consultar una cadena:


* upper: Convierte unca cadena a mayúsculas
* lower: Transforma todos los caracteres a minúsculas
* startswith: Usado para saber si una cadena empieza con cierta subcadena
* endswith: Usado para saber si un cadena termina con una subcadena específica
* find: Busca una subcadena dentro de la cadena y retorna el índice de la primera ocurrencia, o -1 si la subcadena no fue encontrada.
* split: Genera una lista de cadenas a partir de una cadena, separando por cierto sentinela.
* join: Concatena una lista de cadenas usando cierta subcadena como unión.

.. sourcecode:: python

    mystring = 'Big Movie'

    mystring.upper() # BIG MOVIE
    mystring.lower() # big movie
    mystring.startswith('Big') # True
    mystring.startswith('Movie') # False
    mystring.endswith('Movie') # True
    mystring.find('Movie') # 4
    mystring.find('Big') # this is 0
    mystring.find('TV') # this is -1

    ingredients = [ 'Tomato', 'Ham', 'Eggs' ]
    'and '.join(ingredients) # 'Tomato and Ham and Eggs'

    comma_values = '1,2,3,4,5,6'
    comma_values.split(',') # [ '1', '2' , '3', '4', '5']

Desafío
-------

Haz un programa usando funciones de cadena que imprima las siguientes líneas en este orden.

* 17
* THIS IS MY STRING
* this is my string
* [ 'This', 'Is', 'My', 'string' ]

Debes usar la función len para imprimir la primer línea, y la función splic para imprimir la cuarta línea.
