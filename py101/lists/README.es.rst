Lists
-----

Python es único en la manera en la que maneja secuencias y otros objetos. Un tipo de dato usado para manejar secuencias es el tipo "list". El siguiente ejemplo muestra como crear una lista con cuatro elementos

.. sourcecode:: python

    my_list = [ "nasa", 1958, "Moon", 1969 ];
    ingredients = [ "tomato", "bread", "cheese", "ham" ]
    quantities = [ 1, 2, 3, 4 ]

Los objetos de una lista son referenciados por índice. El primer índice es 0, que almacena el primer elemento, el segundo es uno, y así sucesivamente. Para obtener los valores en listas se debe usar las llaves "[]" para obtener el valor en ese índice:

.. sourcecode:: python

  print(my_list[0]) # nasa
  print(ingredients[1]) # bread
  print(quantities[3]) # 4


Desafío
-------

Crea un archivo que defina una lista de los siguientes lenguajes de programación: ADA, Pascal, Fortran, Smalltalk (en ese orden). La lista debe llamarse "languages". Luego debe imprimir la lista usando la sentencia print.
