# usando comprension de listas
# sintaxis # [expresion for item in iterable if condicion]
numeros = range(1, 11)
numeros_pares = [numero for numero in numeros if numero % 2 ==0]
print(numeros_pares) # [2, 4, 6, 8, 10]