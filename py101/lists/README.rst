Lists
-----

Python is unique in the way it can handle sequences of other objects. One type used to handle sequences is the "list". The following examples create lists with four elements.

.. sourcecode:: python

    my_list = [ "nasa", 1958, "Moon", 1969 ];
    ingredients = [ "tomato", "bread", "cheese", "ham" ]
    quantities = [ 1, 2, 3, 4 ]

Lists objects are referenced by the index. First index is zero, which stores the first object, second index is one, and so on. To access values in lists, use the square brackets to obtain the value on that specific index:

.. sourcecode:: python

  print(my_list[0]) # nasa
  print(ingredients[1]) # bread
  print(quantities[3]) # 4


Challenge
---------

Create a file that defines a list of the following languages: ADA, Pascal, Fortran, Smalltalk (in that order). The list must be called "languages". Then it must print the value of that list in the console using print.

