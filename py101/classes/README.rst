Classes and Objects
-------------------

Classes are an encapsulation of state and behaviour, defined by variables and
members respectively, into a single type. Objects are instances of classes,
which get their variables and functions from classes. Classes are
essentially a template to create objects.

A basic class would look something like this:

.. sourcecode:: python

    class Person(object):
        def __init__(self, name):
            self.name = name

        def print_name(self):
            print("Hello {}".format(self.name))

The special "__init__" function is called when a Person object is created.
It can define and assign variables inside a created Person object. For
example the class above assigns a new variable inside a Person object called
 name using the value provided to the __init__ function. The "self" parameter
 makes reference to the implicit object which was created. In other
 programming languages the implicit object is called "this".

The following code creates an instance of Person, passing 'Alex' to the
__init__ function.

.. sourcecode:: python

    myperson = Person('Alex')

In the Person class, "print_name" is a user defined function that can be
invoked to perform custom behaviour. The difference between a function
defined inside a class and a function defined outside a class is that functions
inside classes have access to the individual variables, those variables
are referenced by accessing the self object.

To invoke a function from an object, the following syntax can be used:

.. sourcecode:: python

    alex = Person('Alex')
    alex.print_name() # Prints 'Hello Alex'


Object variables can be accessed as well, by using a similar syntax

.. sourcecode:: python

    alex = Person('Alex')
    john = Person('Johnnie')
    print(alex.name) # Prints 'Alex'
    print(john.name) # Prints 'Johnnie'
    john.name = 'John Walker'
    print(john.name) # Prints 'John Walker'


Challenge
---------

Consider a class called "Vehicle" that stores a Vehicle cost, and a
function that returns information about the vehicle as a string. Write a
program that prints the lines "Vechicle cost is 12000" and "Vechicle cost is
5999.99" in that order using the Vehicle class and the description function

.. sourcecode:: python

    # dont modify this code
    class Vehicle:
        def __init__(self, cost):
            self.cost = cost

        def description(self):
            return "Vehicle cost is {}".format(self.cost)

    # your code goes here

