# Debugging:

# • O depuración es una herramienta que traen varios editores de código con el objetivo de solucionar 
#   nuestros errores de lógica. Revisemos la herramienta debugging de VSCode
# • En este entorno podemos acceder a funcionalidades como:
#   pause → permite pausar la ejecución del programa
#   step over → permite avanazr un solo paso en el programa
#   step in → igresamos a un bloque secundario del programa (funciones)
#   step out → salimos del bloque secundario
#   restart → reinicia el programa
#   stop → detiene el programa
# • Además podemos generar breakpoints, que son puntos en los que el programa se detendrá para ayudarnos 
#   a depurar el código

# Nota: Existen herramientas de debugging propias de python como el módulo pdb o los breakpoints 
#       (a partir de python 3.7)

# Función que retorna los divisores de un número
def divisors(numero):
    divisors=[]
    # Vamos a debugear la aplicación
    # 1. Ir al icono de Run and Debug VSCode
    # 2. Seleccionar python file
    # 3. Pausar el debuger cuando antes de ingresar el número, a través del boton Pause
    # 4. Ingresar a la función divisors, a través del boton Step into
    # 5. La pestaña lateral nos va mostrando el cambio de variables
    # 6. Breakpoints (Al lado del número que especifica la línea de código actual
    #    damos click en el boton rojo) permite pausar el programa en ciertas partes del 
    #    código

    # List comprehension
    divisors = [i for i in range(1,numero+1) if numero % i == 0]

    return divisors

def run():
    num=int(input("Ingrese un número: "))
    print(divisors(num))
    print("Fin del programa")


# Punto de entrada
if __name__ == "__main__":
    run()