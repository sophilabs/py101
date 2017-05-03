Functions
---------

A function is a block of organized, reusable code that is used to perform a single, related action. Python already define many built-in functions like print() or len(), but new functions can be defined in the code, which are called user-defined functions.

.. sourcecode:: python

    def say_hello():
        print("Hello")
        print("How are you?")

Functions may also receive arguments (variables passed from the caller to the function). For example:

.. sourcecode:: python

    def say_hello_with_name(name):
        print("Hello {{0}}".format(name))
        print("How are you?")

Also they may return a value to the caller, using "return" keyword. For example:

.. sourcecode:: python

    def make_division(x, y):
        if y != 0:
            return x / y
        else:
            print("y can't be zero")
            return 0

In rare cases some functions may be empty and do nothing. For example if they are planned to be written later. In those cases, those functions have only the  "pass" keyword on the body:

.. sourcecode:: python

    def will_be_written_tomorrow(list_of_ingredients):
        pass


Calling a Function
------------------

Defining a function only gives it a name, specifies the parameters that are to be included in the function and structures the blocks of code. Once the basic structure of a function is finalized, it can be executed by calling it. Following is the example to call the previous defined functions:

.. sourcecode:: python

    result = make_division(2343, 22)
    say_hello_with_name("Alex")
    print("Result is {{0}}".format(result))

Challenge
---------

Create a program that prints the even numbers from 2 through 100 defining at least a function and calling it.

