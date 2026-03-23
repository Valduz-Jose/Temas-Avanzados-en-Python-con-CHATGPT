# sorted() crea una nueva lista con los valores ordenados, sin modificar la lista original

print("Ordenamiento en Python")
empleado = ["Juan", "Ana", "Pedro", "María", "Luis"]
# Ordenar la lista
empleado_ordenado = sorted(empleado)
empleado_ordenado_invertido = sorted(empleado, reverse=True)
print("-"*50)
print("Lista original:", empleado)
print("-"*50)
print("Lista ordenada:", empleado_ordenado)
print("-"*50)
print("Lista ordenada (invertido):", empleado_ordenado_invertido)
print("-"*50)

empleados_dict = [
    {"nombre":"Juan", "salario": 3000},
    {"nombre":"Ana", "salario": 3500},
    {"nombre":"Pedro", "salario": 2500},
    {"nombre":"María", "salario": 4000},
    {"nombre":"Luis", "salario": 2800}
]

empleados_ordenados_por_salario = sorted(empleados_dict, key=lambda x: x["salario"])
print("Empleados ordenados por salario:")
for empleado in empleados_ordenados_por_salario:
    print(f"{empleado['nombre']}: {empleado['salario']}")