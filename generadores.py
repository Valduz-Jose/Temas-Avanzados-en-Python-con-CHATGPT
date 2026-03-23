# Generadores -> Son funciones que permiten generar una secuencia de valores, 
# en lugar de devolver un solo valor. 
# Se utilizan para crear iteradores personalizados y pueden ser más eficientes 
# en términos de memoria, ya que no almacenan toda la secuencia en memoria 
# a la vez.

# yield -> Es una palabra clave que se utiliza para definir un generador.

print("Generadores en Python")

def generador(maximo):
    contador=0
    while contador < maximo:
        yield contador
        contador += 1

# Crear un generador
var_generador = generador(5000)
# iteramos sobre el generador

for valor in var_generador:
    print(valor)
