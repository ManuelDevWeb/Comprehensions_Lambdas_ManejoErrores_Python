# Comprensión de Listas (Generar listas sin ciclos)

# Estructura List Comprehension: [element for element in iterable if condition]
# element -> Representa el elemento que se va a guardar en la lista
# for element in iterable -> Ciclo a partir del cual se extraeran elementos de otra lista
# if condition -> Condición opcional para filtrar los elementos del ciclo

# Ejemplo: squaresComprehension=[i**2 for i in range(1,101) if i%3!=0]

def run():
    ### Sin Comprehension

    # Lista
    squares=[]

    for i in range(1,101):
        # Guardar el cuadrado de los números divisibles entre 3
        if(i%3!=0):
            squares.append(i**2)
    print(squares)

    ### Con Comprehension

    # Lista que guarda los cuadrados de los números divisibles entre 3
    squaresComprehension=[i**2 for i in range(1,101) if i%3!=0]
    print(squaresComprehension)

    # Lista que guarda los numeros pares
    evenComprehension=[i for i in range(1,101) if i%2==0]
    print(evenComprehension)

    squaresMultiples = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(squaresMultiples)


# Punto de entrada del programa Python
if __name__ == '__main__':
    run()