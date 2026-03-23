# La funcion zip se usa para combinar dos o mas listas en una sola lista de tuplas, donde cada tupla contiene un elemento de cada una de las listas originales. La funcion zip se detiene cuando la lista mas corta se queda sin elementos.
nombres = ["Juan", "Maria", "Pedro"]
edades = [25, 30, 35]
ciudades = ["Madrid", "Barcelona", "Valencia"]
personas = zip(nombres, edades, ciudades)
for persona in personas:
    print(persona) # ('Juan', 25, 'Madrid'), ('Maria', 30, 'Barcelona'), ('Pedro', 35, 'Valencia')
# Toma en cuenta el tamaño de la lista mas corta los demas valores se ignoran
