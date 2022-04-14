import random
import os


# Función para leer el archivo
def read_data(filepath="./archivos/data.txt"):
    words = []
    # Abrimos el archivo en modo lectura
    with open(filepath, "r", encoding="utf-8") as f:
        # Leemos el archivo linea por linea
        for line in f:
            # Eliminamos los espacios en blanco, lo pasamos a mayúsculas y lo agregamos a la lista de words
            words.append(line.strip().upper())
    return words


def run():
    # Llamamos la función que nos lee el archivo
    data = read_data(filepath="./archivos/data.txt")
    # Seleccionamos una palabra al azar de la lista de palabras
    chosen_word = random.choice(data)
    # Separamos la palabra en una lista de letras ['A','B','C','D','E']
    chosen_word_list = [letter for letter in chosen_word]
    # Creamos una lista de letras vacias (Se multiplica por el length de la palabra)
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    # Llenamos el diccionario con las letras y su posición en la palabra (idx es el indice de la letra, letter es la letra)
    for idx, letter in enumerate(chosen_word):
        # Si no existe la letra en el diccionario, la agregamos y la llave será la letra
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        # Agregamos a la llave letra (letter) el indice de la letra (idx)
        letter_index_dict[letter].append(idx)
    
    while True:
        os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
        print("¡Adivina la palabra!")
        # Imprimimos la palabra con los guiones
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        # Validamos que el valor, ingresada sea una letra
        assert letter.isalpha(), "Solo puedes ingresar letras"

        # Validamos que la letra ingresada este en la lista de letras
        if letter in chosen_word_list:
            # Recorremos el diccionario para saber si hay una llave con la letra ingresada
            for idx in letter_index_dict[letter]:      
                # Si la letra ingresada esta en la lista de letras, la reemplazamos por la letra ingresada          
                chosen_word_list_underscores[idx] = letter
        
        if "_" not in chosen_word_list_underscores:
            os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
            print("¡Ganaste! La palabra era", chosen_word)
            break


if __name__ == '__main__':
    run()
