def run():
    # Lista
    my_list=[1,"Hello", True, 4.5]
    # Diccionario
    my_dict={
        "firtname": "Manuel",
        "lastname": "Valencia"
    }

    # Lista con diccionarios anidados
    super_list=[
        {
            "firtname": "Manuel",
            "lastname": "Valencia"
        },
        {
            "firtname": "Juan",
            "lastname": "Perez"
        },
        {
            "firtname": "Pedro",
            "lastname": "Garcia"
        },
        {
            "firtname": "Ana",
            "lastname": "Lopez"
        }
    ]

    # Diccionaro con listas anidadas
    super_dict={
        "naturals":[1,2,3,4,5],
        "integers": [-1,-2,0,1,2],
        "floating": [1.1,2.2,3.3,4.4,5.5],
    }

    # Recorriendo las llaves y valores de un diccionario
    for key, value in super_dict.items():
        # print(key, value)
        print(f"{key} : {value}")

    for i in super_list:
        print(i)

# Punto de entrada del programa Python
if __name__=='__main__':
    run()