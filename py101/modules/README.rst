Modules
-------

Python has a way to put definitions in a file and use them in another script.
Such a file is called a module. Definitions from a module can be imported into
other modules or into the main program file.

A module is a file containing Python definitions and statements. The file name
is the module name with the suffix ".py" appended to it. Within a module, its
name (as a string) is available as the value of the global variable __name__.
For instance, supposing there is file called mymodule.py in the current
directory with the following contents:

.. sourcecode:: python

    # counts how many fibonacci numbers are less than n
    def how_many_fib(n):
        a = 0
        b = 1
        result = 0
        while b < n:
            temp = a
            a = b
            b = temp + b
            result = result + 1
        return result

    def say_hello():
        print("Say my name")

In other files, mymodule can be imported using the following syntax:

.. sourcecode:: python

    import mymodule
    print(mymodule.how_many_fib(1000) # prints 16

Standard Modules
----------------

Python comes with a library of standard modules, called the Python Standard Library.
Some modules are built into the interpreter; these provide access to
operations that are not part of the core of the language but are nevertheless
built in, either for efficiency or to provide access to operating system
primitives such as system calls.

Two very important functions come in handy when exploring modules in
Python: the "dir" and "help" functions. The "dir" function can look for which functions are
implemented in each module. If help is needed, then the "help" function may be used.

.. sourcecode:: python

    import http
    dir(http)
    # prints [ 'HTTPStatus','IntEnum','__all__','__builtins__','__cached__',
    # '__doc__','__file__','__loader__','__name__','__package__','__path__',
    # '__spec__']

    help(http.HTTPStatus)
    # prints a large description if this field


Writing modules
---------------

To create a module of your own, simply create a new .py file with the module
name, and then import it using the Python file name (without the .py extension)
using the import command.

Challenge
---------

Create a module called "numbers" that defines a tangent() function that
computes the tangent using the functions "sin" and "cos" from the standard math
library, and then a program that prints the value of tangent(1) from the
numbers module. The program should print one line "1.557407724654902"

