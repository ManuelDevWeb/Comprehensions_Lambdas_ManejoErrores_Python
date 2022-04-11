# Funciones de orden superior 

# Es una función que recibe como parámetro otra función, los mas comunes son 
# map, filter, reduce.

from functools import reduce

my_list=range(1,21)
my_list2=[2,2,2,2,2]

# 1. Filter 

# Lista de números impares utilizando list comprehension

odd_comprehension=[i for i in my_list if i%2!=0]
print(odd_comprehension)

# Lista de números impares utilizando filter
odd_filter=list(filter(lambda num: num%2!=0, my_list))
print(odd_filter)

# 2. Map

# Lista de números evelados a su cuadrado utilizando list comprehension
squeares_comprehension=[i**2 for i in my_list]
print(squeares_comprehension)

# Lista de números evelados a su cuadrado utilizando map
squeares_map=list(map(lambda num: num**2, my_list))
print(squeares_map)

# 3. Reduce 

# Retornar la multiplicación de los elementos de la lista utilizando list comprehension 
allMult=1
for i in my_list2:
    allMult=allMult*i
print(allMult)

# Retornar la multiplicación de los elementos de la lista utilizando reduce
# a y b son los 2 primeros elementos de la lista, a pasa a ser a*b osea 4 y b seria el siguiente 2
allMult_reduce=reduce(lambda a, b: a * b, my_list2)
print(allMult_reduce)
