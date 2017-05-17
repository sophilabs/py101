Módulos
-------

Python permite escribir definiciones en un archivo y luego usarlas en otro.
Tal archivo es llamado "módulo". Las definiciones de un módulo pueden se importadas
en otros módulos o en el archivo principal del programa.

Un módulo es un archivo que contiene definiciones y sentencias. El nombre de del archivo
es el nombre del módulo más el sufijo ".py". Dentro de un módulo, su nombre (como una
cadena) está disponible en la variable globa __name__. Por ejemplo, suponiendo que hay un
archivo llamado mymodule.py en el directorio actual con el siguiente contenido:

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

En otros archivos, mymodule puede ser importado con la siguiente sintaxis:

.. sourcecode:: python

    import mymodule
    print(mymodule.how_many_fib(1000) # prints 16

Módulos estándares
------------------

Python viene con su propia librería de módulos estándar, llamada "Python Standard
Library". Algunos módulos están integrados al intérprete; estos proveen acceso a
operaciones que no son parte del núcleo del lenguaje pero están integrados de todas
formas, ya sea por eficiencia o para proveer acceso a primitivas del sistema operativo.


Dos funciones muy importantes resultan ser útiles al momento de explorar módulos: "dir"
y "help". La primera puede buscar funciones dentro de cada módulo. Si se necesita
ayuda sobre una función en particular, la función "help" puede ser usada.

.. sourcecode:: python

    import http
    dir(http)
    # prints [ 'HTTPStatus','IntEnum','__all__','__builtins__','__cached__',
    # '__doc__','__file__','__loader__','__name__','__package__','__path__',
    # '__spec__']

    help(http.HTTPStatus)
    # prints a large description if this field


Escribiendo módulos
-------------------

Para crear un módulo propio, simplemente crea un nuevo archivo con su nombre y la
extensión py, y luego importalo usando su nombre con el comando "import".

Desafío
-------

Crea un módulo llamado "numbers" que defina una función tangent() que calcule la
tangete mediante las funciones "sin" (seno) y "cos" (coseno) de la librería estándar,
y luego un programa que imprima el valor de tangent(1) usando la función del módulo
numbers. El programa debería imprimir la línea "1.557407724654902".

