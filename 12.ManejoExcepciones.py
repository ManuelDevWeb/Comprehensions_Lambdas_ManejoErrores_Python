# Manejo de Excepciones

# • try except → Anidamos nuestro programa en dos bloques de código, el primero es el programa 
#   que se ejecuta normalmente sin errores y el segundo representa las instrucciones 
#   a seguir en caso de error. Su sintaxis es:

# try:
# 	<bloque1>
# except <error> as <alias>:
# 	<bloque 2>

# • <error> es un parámetro opcional, permite capturar sólo el tipo de error indicado, si no se 
#   coloca captura todos los errores posibles (es buena práctica capturar cada tipo de error por 
#   separado).
# • as <alias> nos permite crear un alias al error, para trabajar con él.

def palindrome(string):
    try:
        if len(string)==0:
            #  raise nos permite generar errores, es decir crear nuestros propios errores
            raise ValueError("No se puede evaluar una cadena vacía")
        
        return string == string[::-1]
    except ValueError as e:
        print(e)
        return False

try:
    print(palindrome(1)) 
except TypeError:
    print("Solo se pueden ingresar strings")

# • raise → Esta instrucción nos permite generar errores, es decir crear nuestros propios errores 
#   cuando detectemos que nuestro programa no actúa como debería con cierto tipo de datos
#   Su sintaxis es:    

# raise <NombreError>("<descripci[on del error>")

try:
    print(palindrome(""))
except TypeError:
    print("Solo se pueden ingresar strings")

# • fynally → Es una bloque de código que se ejecuta exista un error o no (un tercer bloque después 
#   de try except), no es muy usual pero puede darse para cerrar archivos, conexiones a BBDD o 
#   liberar recursos.
