Toma de decisiones
------------------

En programación, la toma de decisiones es la anticipación a las condiciones que pueden ocurrir durante la ejecución del programa, así como la espcecificación de las acciones tomadas de acuerdo a las condiciones. El programa determina que acción tomar y que sentencias ejecutar dependiendo del valor de las expresiones. El siguiente es un ejemplo de toma de decisiones encontrado en la mayoría de los lenguajes de programación:

.. sourcecode:: python

    edad = 45

    if edad > 18:
        print('Eres muy viejo')

Python provee las sentencias "if", que consisten de una expressión booleana (True o False) seguida de uno o más sentencias, como la mostrada arriba. Las sentencias if pueden ser sucedidas por sentencias "else" que son ejecutadas si la condición del "if" no se cumple.

.. sourcecode:: python

    x = 32
    y = 2

    if y == 0:
        print('El divisor no debe ser 0')
    else:
        print('El resultado es {{}}'.format(x/y))

Las sentencias if pueden ser anidadas, permitiendo ejecutar código más complejo.

.. sourcecode:: python

    age = 23
    if age < 18:
        if age < 0:
            print('Age no es válido')
        print('Eres muy pequeño para manejar')
    else:
        print('Puedes manejar')



Desafío
-------

Usando el siguiente programa, modifica las variables para que el programa imprima las líneas "1", "2" y "3".

.. sourcecode:: python

    # Cambia este código
    first_number = 0
    second_number = 0

    # No cambies este código
    if first_number > 15:
        print("1")
        if second_number > 15:
            print("2")

    if first_number < second_number:
        print("3")
    else:
        print("Error")

