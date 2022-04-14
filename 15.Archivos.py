# Existen varias extensiones de archivos con los que podemos interactuar con python 
# (js,csv,py,css,json,xml) Para abrir un archivo seguimos las siguiente estructura.

# with open(<ruta>, <modo_apertura>, encoding) as <nombre>

# • with Es un manejador contextual, nos ayuda a controlar el flujo del archivo 
#   (sirve para que el archivo no se dañe cuando existe algún cierre inesperado)
# • open(ruta,modo_apertura): es una función que necesita de dos parámetros
#   * ruta: es donde se encuentra nuestro archivo en nuestro equipo
#   * modo_de_apertura: como vamos a abrir el archivo, los modificadores son:
#     r -> Solo lectura
#     r+ -> Lectura y escritura
#     w -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
#     w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
#     a -> Añadido (agregar contenido). Crea el archivo si éste no existe
#     a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.
#   * encoding: es el tipo de codificación que usaremos para leer el archivo (opcional)

# Función para leer un archivo 
def read():
    numbers=[]
    # Abrimos el archivo en modo lectura
    with open("./archivos/numbers.txt", 'r', encoding="utf-8") as file: 
        # Leemos el archivo linea por linea
        for line in file:
            # Eliminamos los espacios en blanco
            line=line.strip()
            # Convertimos la linea a un número y lo agregamos a la lista de números
            numbers.append(int(line))
    print(numbers)
    file.close()


# Función para escribir un archivo
def write():
    names=["Juan", "Pedro", "Luis", "Carlos", "Jorge", "Rocío"]
    # Abrimos el archivo en modo escritura
    with open("./archivos/names.txt", 'w', encoding="utf-8") as file:
        # Escribimos cada nombre en el archivo
        for name in names:
            file.write(name + "\n")
    file.close()

# Función para escribir en el archivo sin sobreescribir el contenido
def append():
    moreNames=["Manuel", "Valencia", "Londoño"]
    # Abrimos el archivo en modo añadido y lectura
    with open("./archivos/names.txt", 'a', encoding="utf-8") as file:
        # Escribimos cada nombre en el archivo
        for name in moreNames:
            file.write(name + "\n")
    file.close()


def run():
    read()
    write()
    append()

# Punto de partida programa Python
if __name__ == "__main__":
    run()

