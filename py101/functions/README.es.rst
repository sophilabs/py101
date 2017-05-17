Funciones
---------

Una función es un bloque de código organizado y reusable que puede ser utilizado para realizar cierta acción. Python ofrece un número importante de funciones predefinidas como print() o len(), pero se pueden definir nuevas funciones en el código, que son denominadas funciones definidas por el usuario.

.. sourcecode:: python

    def di_hola():
        print("Hola")
        print("¿Cómo estás?")

Las funciones también pueden recibir argumentos: variables que se pasan desde el invocador a la función. Por ejemplo:

.. sourcecode:: python

    def decir_hola_con_nombre(name):
        print("Hola {}".format(name))
        print("¿Cómo estás?")

Las funciones también pueden retornar un valor al invocador, usando la palabra clave "return", por ejemplo:

.. sourcecode:: python

    def hacer_division(x, y):
        if y != 0:
            return x / y
        else:
            print("y no puede ser 0")
            return 0

En algunos casos las funciones pueden ser vacías y no hacer nada. Por ejemplo si se planea escribirlas luego. En esos casos, esas funciones solo tienen la palabra clave "pass" en el cuerpo.

.. sourcecode:: python

    def a_ser_escrita_luego(lista_de_ingredientes):
        pass


Llamando a una función
----------------------
Definir una función solo le da un nombre, especifica los parámetros que se van a incluir en la función y estructura los bloques de código. Una vez que la estructura de una función está terminada, puede ser ejecutada llamándola. En el siguiente ejemplo se llaman a las funciones que fueron definidas previamente:

.. sourcecode:: python

    result = hacer_division(2343, 22)
    decir_hola_con_nombre("Alex")
    print("Resultado es {}".format(result))

Desafío
---------

Crea un programa que imprima los números pares desde el 2 al 100 inclusive, definiendo al menos una función y llamándola.
