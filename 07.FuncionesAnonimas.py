# Funciones anónimas o lambda (Funciones que no tienen nombre) y una sola linea de código

# Sin lambda
def palindrome(string):
    return string == string[::-1]

print(palindrome("ana"))

# Con lambda
palindromeLambda = lambda string: string == string[::-1]

print(palindromeLambda("ana"))