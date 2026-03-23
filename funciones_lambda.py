# FUnciones Lambda 
# Sintaxis lambda argumentos: expresion se usa para codigos compactos

print("Funciones Lambda")

def cuadrado(x):
    return x**2

print(cuadrado(5)) # 25

# Usando Lambda
cuadrado_lambda = lambda x: x**2
print(cuadrado_lambda(5)) # 25
print(cuadrado_lambda(4)) # 16

