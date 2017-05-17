Operators
---------

There are five basic types of operators in Python: arithmetic, concatenation and duplication.

Just as many programming languages, numbers can interact by using addition (+), subtraction (-), multiplication (\*), division (/) and division remainder (%), known as the modulo operator. Parenthesis can be used to group expressions, that help to remove ambiguity in results and improve code legibility.

.. sourcecode:: python

    the_order = 1 + 2 * 3   # 7
    matters   = (1 + 2) * 3 # 9

    some_division = 22 / 8  # 2.75
    remainder = 22 % 8      # 6

Using two multiplication symbols means exponentiation:

.. sourcecode:: python

    big_number = 2 ** 8      # 256
    small_number = 2 ** (-8) # 0.00390625

Strings or lists can be joined together by using the plus operator:

.. sourcecode:: python

    hello = 'hello' + ' ' + 'world' # 'Hello World'
    prime_numbers = [1,3,5,7]
    other_numbers = [2,4,6,8,9]
    print(prime_numbers + other_numbers) # Prints [1, 3, 5, 7, 2, 4, 6, 8, 9]

Both strings and lists can be duplicated to form larger sequences using the multiplication operator:

.. sourcecode:: python

    print('lo' * 10 + 'l') # prints lolololololololololol
    print([0,3] * 2 + [4,5,6]) # prints [0, 3, 0, 3, 4, 5, 6]

Challenge
---------

Make a program that outputs the string 'ka' repeated 10 times using string duplication.
