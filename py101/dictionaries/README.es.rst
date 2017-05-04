Diccionarios
------------

Un diccionario es un tipo de datos similar a las listas, pero funciona
asociando claves y valores en en vez de usar índices. Cada valor del
diccionario puede ser accedido usando una clave que puede ser cualquier tipo
 de objeto. Por ejemplo se pueden usar cadenas para referenciar objetos del
 diccionario. Una pequeña base de datos telefónica puede ser almacenada usando
 diccionarios de la siguiente manera

.. sourcecode:: python

    directorio = {}
    directorio["Alex"]    = '2203-3434'
    directorio["Rick"]    = '+543 3232320'
    directorio["Rolling"] = '9476-62781'

De manera alternativa, un diccionario puede ser inicializado usando la
siguiente notación

.. sourcecode:: python

    edades = {
        'Alex': 23,
        'Rick': 42,
        'Rolling' : "No lo sé"
    }

Iteración
---------

Los diccionarios permiten ser iterados. Para iterar sobre las claves del
diccionario se usa la siguiente sintaxis.

.. sourcecode:: python

    for name in ages:
        print("Edad de {} es {}".format(name, ages[name]))

El ejemplo va a imprimir algo similar a:

.. sourcecode::

    Edad de Rick es 42
    Edad de Rolling es No lo sé
    Edad de Alex es 23

Sin embargo, un diccionario no mantiene el orden de los elementos almacenado
 en él.

Borrado de claves
-----------------

Para borrar un índice específico usa la palabra clave "del" como se muestra
en el siguiente ejemplo:

.. sourcecode:: python

    ages = {
        'Alex': 39,
        'Rick': 42,
        'Rolling' : "I don't know"
    }
    del ages['Rolling']
    print(ages) # imprime {'Rick': 42, 'Alex': 39}


Desafío
-------

Modifica el programa provisto abajo para que la función
"print_only_even_keys", imprima solamente los nombres de aquellas claves
cuyos valores son números pares.

.. sourcecode:: python

    def print_only_even_keys(some_dict):
        # pon tu código aquí
        pass

    # no modifiques este código
    print_only_even_keys({ 'Alfred': 28, 'Mary': 29 })
    print_only_even_keys({ 'Alfred': 31, 'Mary': 29 })


