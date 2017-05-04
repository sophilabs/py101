Decision making
---------------

Decision making is anticipation of conditions occurring while execution of the program and specifying actions taken according to the conditions. Decision structures evaluate multiple expressions which produce True or False. The program determine which action to take and which statements to execute, depending of the value of the expressions. Following is an example of a typical decision making structure found in most of the programming languages:

.. sourcecode:: python

    age = 45

    if age > 18:
        print('You are too old')

Python provides the "if" statements, consisting of a boolean expression followed by one or more statementsIf statements can be followed by an else "else" statements executed if the top "if" condition doesn't held.

.. sourcecode:: python

    x = 32
    y = 2

    if y == 0:
        print('divisor y should not be zero')
    else:
        print('Result is {}'.format(x/y))

If statements can be nested allowing more complex logic to be executed:

.. sourcecode:: python

    age = 23
    if age < 18:
        if age < 0:
            print('Age is invalid')
        print('You are too young to drive')
    else:
        print('You are allowed to drive')



Challenge
---------

Using the following program, modify the variables so the program prints the lines "1", "2", and "3"

.. sourcecode:: python

    # change this code
    first_number = 0
    second_number = 0

    # don't change this code
    if first_number > 15:
        print("1")
        if second_number > 15:
            print("2")

    if first_number < second_number:
        print("3")
    else:
        print("Error")

