Dictonaries
-----------

A dictionary is a data type similar to lists, but works with keys and
values instead of indexes. Each value stored in a dictionary can be accessed
using a key, which is any type of object, for example strings
instead of using its index to address it.

For example, a database of phone numbers could be stored using a dictionary
like this: {}

.. sourcecode:: python

    phonebook = {}
    phonebook["Alex"]    = '2203-3434'
    phonebook["Rick"]    = '+543 3232320'
    phonebook["Rolling"] = '9476-62781'

Alternatively, a dictionary can be initialized using the following notation:

.. sourcecode:: python

    ages = {
        'Alex': 23,
        'Rick': 42,
        'Rolling' : "I don't know"
    }

Iteration
---------

Dictionaries can be iterated over. To iterate over the dictionary keys, use
 the following syntax:

.. sourcecode:: python

    for name in ages:
        print("Age of {} is {}".format(name, ages[name]))

The previous example will print something similar to

.. sourcecode::

    Age of Rick is 42
    Age of Rolling is I don't know
    Age of Alex is 23

However, a dictionary, unlike a list, does not keep the order of the values
stored in it.

Key removal
-----------

To remove a specified index, use the "del" keyword as shown in the following
example:

.. sourcecode:: python

    ages = {
        'Alex': 39,
        'Rick': 42,
        'Rolling' : "I don't know"
    }
    del ages['Rolling']
    print(ages) # prints {'Rick': 42, 'Alex': 39}


Challenge
---------

Modify the program below, so the "print_only_even_keys" function prints
 only the name of the keys whose values are even numbers

.. sourcecode:: python

    def print_only_even_keys(some_dict):
        # put your code here
        pass

    # Don't modify this code
    print_only_even_keys({ 'Alfred': 28, 'Mary': 29 })
    print_only_even_keys({ 'Alfred': 31, 'María': 29 })

The program should Output "Alfred" in the first line and nothing else
