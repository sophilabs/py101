Módulos
-------

Python ofrece una manera de incluir definiciones en un archivo y usarlos
desde otro script. Tal archivo es llamado un módulo. Las definiciones de un
módulo pueden ser importado en otros módulos o al programa principal. El
nombre del archivo es el nombre del módulo más la extensión ".py". Por
ejemplo suponiendo que existe un archivo en la carpeta actual con el
siguiente contenido:

.. sourcecode:: python

    # Cuenta cuantos números de fibonacci son menores que n
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
        print("Di mi nombre")

En otros archivos mymodule puede ser importado usando la siguiente sintaxis:

.. sourcecode:: python

    import mymodule
    print(mymodule.how_many_fib(1000) # prints 16

Módulos Estándar
----------------

Python viene con una biblioteca de módulos estándar, llamada "Python Library
Reference". Algunos módulos ya están provistos en el intérprete, que proveen
acceso a operaciones que no son parte del núcleo del lenguaje pero sin
embargo están incluidas, ya sea por eficiencia o para proveer acceso a
operaciones primitivas del sistema operativo, como las llamadas al sistema
("system calls").

Dos funciones muy importante a la hora de explorar módulos en Python son
"dir" y "help". La primera permite saber qué funciones están implementadas
en un módulo. Si se necesita ayuda, se puede utilizar la función "help" que
muestra un texto acerca de cierta función específica.


    help(http.HTTPStatus)
    # prints a large description if this field


Escribiendo módulos
-------------------

Para crear un módulo propio, simplemente crea un nuevo archivo con su nombre y la
extensión py, y luego importalo usando su nombre con el comando "import".

.. sourcecode:: python

    import http
    dir(http)
    # imprime [ 'HTTPStatus','IntEnum','__all__','__builtins__','__cached__',
    # '__doc__','__file__','__loader__','__name__','__package__','__path__',
    # '__spec__']

    help(http.HTTPStatus)
    # Muestra una descripión larga de ese campo


Escribiendo un módulo
---------------------

Para crear un módulo, simplemente hay que crear un archivo .py con el nombre
del módulo y luego importándolo usando el nombre de archivo usando el
comando import.

Desafío
-------

Crea un módulo llamado "numbers" que defina una función tangent() que
compute la tangente usando las funciones "sin" (seno) y "cos" (coseno) desde
la biblioteca estándar "math", y luego un programa que imprima el valor de
tangent(1) desde el módulo numbers. El progama debería imprimir una línea
"1.557407724654902"
