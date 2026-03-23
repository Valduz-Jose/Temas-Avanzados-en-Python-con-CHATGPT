print("Expresiones generadoras en Python")

# Expresiones generadoras -> Son una forma concisa de crear generadores
# Se definen utilizando paréntesis en lugar de corchetes

# Crear una expresión generadora
generador = (x**2 for x in range(10) if x % 2 == 0)

# iteramos sobre la expresión generadora
for valor in generador:
    print(valor)