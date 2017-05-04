Formateo de Strings
-------------------

El método str.format() de la clase string puede ser utilizado para hacer substitución de variables y formateo de valores. Esto permite concatenar elementos juntos dentro de una cadena usando formateo posicional. Funciona introduciendo uno o más campos de reemplazo, definidos como pares de corchetes ({}) en uan cadena y llamando a la operación format:

.. sourcecode:: python

    print('Hello {}. How are you?'.format('Josh'))
    # prints out 'Hello Josh. How are you?

En el ejemplo anterior el valor de 'Josh' se reemplaza donde estaba el par de corchetes.

Se pueden usar múltiples pares de corchetes si se desea hacer más de un reemplazo.

.. sourcecode:: python

    print('Hello {}. Do you like {}?'.format('Anne', 'Pizza'))
    # prints 'Hello Anne. Do you like Pizza?'

Challenge
---------

Haz un programa que imprima 'Talk is cheap. Show me the code.' usando la función format.
