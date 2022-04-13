def divisors(numero):
    try:
        if(numero<0 or numero==0):
            #  raise nos permite generar errores, es decir crear nuestros propios errores
            raise ValueError("El número no puede igual o menor a 0")

        divisors=[]
        
        for i in range(1,numero+1):
            if numero%i==0:
                divisors.append(i)

        return divisors
    except ValueError as e:
        print(e)
        return False
       

def run():
    while True:
        try:
            num=int(input("Ingrese un número: "))
            
            if(divisors(num)):
                print(divisors(num))
                print("Fin del programa")
                break
            
        except ValueError:
            print("El valor ingresado no es un número")


# Punto de entrada
if __name__ == "__main__":
    run()