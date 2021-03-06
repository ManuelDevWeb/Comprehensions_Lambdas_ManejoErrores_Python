# Errores en el código

# Cuando python nos avisa que tenemos un error en el código nos avienta un mensaje que conocemos 
# como traceback, puesde ser debido a:

# • Errores de Sintaxis (SyntaxError) → escribimos mal alguna palabra clave (typo), el programa 
#   no se ejecuta.
# • Excepciones (Exeption) → Producen un colapso o interrupción de la lógica del programa en alguna 
#   línea en específico por ejemplo (todas las líneas anteriores se ejecutan), pueden ser de varios 
#   tipos, generalmente aparecen cuando no existe un componente clave en la ejecución o hay alguna 
#   imposibilidad lógica (matemática) para efectuar la instrucción, tambipen pueden generarse dentro 
#   del código o fuera de el (elevar una excepción)


# Lectura de un traceback

# • La manera correcta de leer un traceback es iniciar por el final, en el caso de un error de 
#   sintaxis nos indicará en qué línea se encuentra dicho error.
# • En el caso de excepciones la última línea nos indicará el tipo de exepcion que se generó 
#   (generalmente son autoexplicativas pero si no entienedes que paso puedes buscar este error)
# • La penúltima línea nos indicará dende se encuentra el error (archivo y línea)
# • La antepenúltima línea nos muestra “most recent call last” lo que significa que la llamada más 
#   reciente es la última (el programa se cerró después de esa llamada, se genero un error)


# Elevar una excepción

# Cuando tenemos una excepción en python lo que sucede es que se crea un objeto de tipo exception que 
# se va moviendo a través de los bloques de código hasta llegar al bloque principal si es que no se 
# maneja dicha excepción en algún bloque intermedio el programa se interrumpe y genera el traceback