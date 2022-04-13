# Assert statements

# • Es una manera poco usual de manejar los errores en python
# • Evalúa una condicional, si esta se cumple continuamos con el flujo normal del python, 
#   si no se cumple eleva un error del tipo AssertionError y nos muestra un mensaje.

# Su sintaxis es:

# assert <condicion>, <"mensaje">
# <código>

def divisors(numero):
    divisors=[]
        
    for i in range(1,numero+1):
        if numero%i==0:
            divisors.append(i)

    return divisors
   
       

def run():
    num=(input("Ingrese un número: "))
    # Afirmando que el valor debe ser numérico
    assert num.isnumeric() and int(num) > 0, "El valor ingresado no es un número o es menor o igual a 0"
    print(divisors(int(num)))
    print("Fin del programa")
                   

# Punto de entrada
if __name__ == "__main__":
    run()