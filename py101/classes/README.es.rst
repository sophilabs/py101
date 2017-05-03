Clases and Objectos
-------------------

Las clases son una encapsulación de estado y comportamiento, definido por
variables y miembros respectivamente, en un solo tipo. Los objetos son
instancias de clases que tienen sus variables y funciones desde una clase.
Las clases son esencialmente una plantilla para crear objetos

Una clase básica se ve como sigue:

.. sourcecode:: python

    class Persona(object):
        def __init__(self, name):
            self.name = name

        def print_name(self):
            print("Hola {{}}".format(self.name))

La función especial "__init__" se llama cuando se crea un objeto Persona.
Pueded definir y asignar variables que se usan dentro del objeto Persona
creado. Por ejemplo la clase de arriba asigna una nueva variable dentro del
objeto Persona, llamada "name" usando el valor provisto a la función
__init__. El parámetro "self" hace referencia al objeto implícito que se
está creando. En otros lenguajes de programación el objeto implícito se
denomina "this".

El siguiente código crea una instancia de Persona pasando 'Alex' a la
función __init__

.. sourcecode:: python

    myperson = Person('Alex')

En la clase Person "print_name" es una función definida por el usuario que
puede ser invocada para realizar cierta tarea. La difrencia entre una
función definida dentro de una clase y otra que no lo está es que las
funciones definidas dentro de clases tienen acceso a las variables
individuales. Esas variables son referencidas accediendo al objeto self.

Para invocar una función de un objeto se puede utilizar la siguiente sintaxis.

.. sourcecode:: python

    alex = Person('Alex')
    alex.print_name() # Imprime 'Hola Alex'


Las variables del objeto pueden ser accedidas también utilizando una
sintáxis similar:

.. sourcecode:: python

    alex = Person('Alex')
    john = Person('Johnnie')
    print(alex.name) # Imprime 'Alex'
    print(john.name) # Imprime 'Johnnie'
    john.name = 'John Walker'
    print(john.name) # Imprime 'John Walker'


Desafío
-------

Considera la clase "Vehicle" que almacena el costo de un Vehículo, y una
función que retorna información acerca del vehículo como una cadena. Escribe
un programa que imprima las líneas "Vehicle cost is 12000" y "Vechicle cost is
5999.99" en ese orden usando la clase Vehicle y la función description

.. sourcecode:: python

    # No modifiques este código
    class Vehicle:
        def __init__(self, cost):
            self.cost = cost

        def description(self):
            return "Vehicle cost is {{}}".format(self.cost)

    # Tu código va aquí

