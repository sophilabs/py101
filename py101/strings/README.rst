String Operations
-----------------

Strings are amongst the most popular types in Python. They are an special type of sequence of characters. To access substrings, use the square brackets for slicing along with the index or indices to obtain a particular substring. Negative indexes refer to the string counting back from the end.

.. sourcecode:: python

    mystring = 'Show me the code'
    print(mystring[0])   # prints S
    print(mystring[0:4]) # prints Show
    print(mystring[-4:]) # prints code

The "len" function can be used to get the length of a particular string.

.. sourcecode:: python

    print(len('hello'))  # prints 5

In addition, there are a variety of functions to transform and query a string, such as:

* upper: Transforms all characters to UPPERCASE.
* lower: Transforms all characters to lowercase.
* startswith: Used to know if a string begins with some substring.
* endswith: Used to know if a string ends with some substring.
* find: Used to know if a string is contained in other string. Returns the index of the first occurrence or -1 if it was not found.
* split: Generates a list of substrings, separated by a other substring.
* join: Concatenates a lists of string by using a particular string.

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

Challenge
---------

Make a program using string functions that prints the following lines in this order:

* 17
* THIS IS MY STRING
* this is my string
* [ 'This', 'Is', 'MY', 'string' ]

You must use the len function to print the first line, and the split function to print the fourth line.
