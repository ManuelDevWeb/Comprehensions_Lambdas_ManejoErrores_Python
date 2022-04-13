# Funciones anónimas o lambda (Funciones que no tienen nombre) y una sola linea de código

# Sin lambda
def palindrome(string):
    return string == string[::-1]

print(palindrome("oso"))

# Con lambda
palindromeLambda = lambda string, string2: string == string[::-1] and string2 == string2[::-1]

print(palindromeLambda("ana", "oso"))