String Formatting
-----------------

Python's format() operation of the string class allows  to do variable substitutions and value formatting. This allows to concatenate elements together within a string through positional formatting. It work by putting in one or more replacement fields or placeholders, defined by a pair of curly braces ({}), into a string and calling the format() operation:

.. sourcecode:: python

    print('Hello {}. How are you?'.format('Josh'))
    # prints out 'Hello Josh. How are you?

In the previous example places the value of Josh into the string where the curly braces were.

Multiple pairs of curly braces can be used to do multiple substitutions.

.. sourcecode:: python
    print('Hello {}. Do you like {}?'.format('Anne', 'Pizza'))
    # prints 'Hello Anne. Do you like Pizza?'

Challenge
---------

Make a program that outputs the string 'Talk is cheap. Show me the code.' using the format function.
