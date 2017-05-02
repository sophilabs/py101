While loops
-----------

In general, statements are executed sequentially: The first statement in a function is executed first, followed by the second, and so on. There may be a situation when is need to execute a block of code several number of times. The following example will print the number 1 through 100 and then "Done!":

.. sourcecode:: python

    mynumber = 1
    while mynumber < 100:
       print(mynumber)
       mynumber = mynumber + 1
    print("Done!")

Programming languages provide various control structures that allow for more complicated execution paths. They are "while" loops and "for" loops

While loops, which repeatedly executes a target statement as long as a given condition is true. When the condition becomes false, program control passes to the line immediately following the loop.

For loops
---------

The for loops have the ability to iterate over the items of any sequence, such as a list or a string.

.. sourcecode:: python
    ingredients = ['banana', 'apple',  'mango']
    for ingredient in ingredients:
        print('Current ingredient: {{0}}'.format(ingredient))

    for some_char in 'Python':
        print(some_char)

The previous example will generate the following output:

.. sourcecode::
    Current ingredient: banana
    Current ingredient: apple
    Current ingredient: mango
    P
    y
    t
    h
    o
    n

Also the "range" function can be used to iterate through a list of numbers

.. sourcecode:: python
    for number in range(100):
       print(number)
    print("Done!")

Challenge
---------

Using while, for and if statements, write a program that prints all the odd integers from 1 through 100, one per line.
