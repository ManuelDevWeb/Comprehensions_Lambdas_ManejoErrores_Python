# Comprensión de Diccionarios (Generar diccionarios sin ciclos)

# Estructura Diccionario Comprehension: {key:value for value in iterable if condition}
# key:value -> Representa el elemento que se va a guardar en el diccionario
# for value in iterable -> Ciclo a partir del cual se extraeran elementos de otra lista
# if condition -> Condición opcional para filtrar los elementos del ciclo

# Ejemplo: my_dictComprehension={i:i**3 for i in range(1,101) if i%3!=0}

import math

def run():
    ### Sin Comprehension

    # Diccionario
    my_dict={}

    for i in range(1,101):
        if(i%3!=0):
            my_dict[i]=i**3
    print(my_dict)

    ### Con Comprehension

    # Diccionario
    my_dictComprehension={i:i**3 for i in range(1,101) if i%3!=0}
    print(my_dictComprehension)

    my_dict_sqrt={i:math.sqrt(i) for i in range(1,1000)}
    print(my_dict_sqrt)

# Punto de entrada del programa Python
if __name__=='__main__':
    run()