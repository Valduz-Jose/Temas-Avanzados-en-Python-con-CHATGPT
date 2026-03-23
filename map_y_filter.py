# Map permite mapear una función a cada elemento de un iterable, como una lista o una tupla.
# La función map toma dos argumentos: la función que se desea aplicar y el iterable al que se le aplicará la función

numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))#el primer parametro es la funcion lambda que eleva al cuadrado cada elemento de la lista numeros, y el segundo parametro es la lista numeros
print(cuadrados) # Output: [1, 4, 9, 16, 25]

# Filter permite filtrar elementos de un iterable en función de una función que devuelve un valor booleano.
# La función filter toma dos argumentos: la función que se desea aplicar y el iterable 

pares = list(filter(lambda x: x % 2 == 0, numeros)) #el primer parametro es la funcion lambda que devuelve True si el numero es par, y el segundo parametro es la lista numeros
print(pares) # Output: [2, 4]

#reduce permite reducir un iterable a un solo valor aplicando una función acumulativa a los elementos del iterable.
from functools import reduce
suma = reduce(lambda x, y: x + y, numeros) #el primer parametro es la funcion lambda que suma dos elementos, y el segundo parametro es la lista numeros
print(suma) # Output: 15