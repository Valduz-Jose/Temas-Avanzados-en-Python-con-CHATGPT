print("*** Funcion Sum y Next ***")

lista = [1, 2, 3, 4, 5]

resultado =sum(lista)
print(f"Resultao de la suma {resultado}")

# Se le puede dar un valor inicial
resultado = sum(lista, 10)
print(f"Resultao de la suma con valor inicial {resultado}")

# La función next se utiliza para obtener el siguiente elemento de un iterador
iterador = iter(lista)
print(f"Primer elemento: {next(iterador)}")
print(f"Primer elemento: {next(iterador)}")
print(f"Primer elemento: {next(iterador)}")
print(f"Primer elemento: {next(iterador)}")
print(f"Primer elemento: {next(iterador)}")