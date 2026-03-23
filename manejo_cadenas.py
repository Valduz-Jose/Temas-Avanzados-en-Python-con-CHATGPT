# Manejo de cadenas
# El metodo split se usa para dividir una cadena en una lista de subcadenas, utilizando un separador especificado. Si no se especifica un separador, se utiliza el espacio en blanco como separador por defecto.
cadena = "Hola Mundo"
palabras = cadena.split() #por defecto se usa el espacio en blanco como separador
print(palabras) # ['Hola', 'Mundo']


# find se usa para encontrar la posicion de la primera ocurrencia de una subcadena en una cadena. Si la subcadena no se encuentra, devuelve -1.
posicion = cadena.find("Mundo")#devuleve el indice de la primera letra de la subcadena
print(posicion) # 5

# Replace se usa para reemplazar todas las ocurrencias de una subcadena por otra subcadena en una cadena. Devuelve una nueva cadena con los reemplazos realizados.
nueva_cadena = cadena.replace("Mundo", "Python")
print(nueva_cadena) # Hola Python

# Multiplicacion de cadenas se puede multiplicar una cadena por un numero entero para crear una nueva cadena que repite la cadena original el numero de veces especificado.
cadena = "Hola "
resultado_multiplicacion_cadenas = cadena * 3
print(resultado_multiplicacion_cadenas) # Hola Hola Hola

# Fucncion strip se usa para eliminar los espacios en blanco al principio y al final de una cadena. Devuelve una nueva cadena sin los espacios en blanco.
cadena = "   Hola Mundo   "
cadena_sin_espacios = cadena.strip()
print(cadena_sin_espacios) # Hola Mundo