# Decoradores -> @ -> Son funciones que envuelven a otra función para extender su comportamiento sin modificarla.

print("Decoradores en Python")

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Antes de la función")
        resultado = funcion(*args, **kwargs)
        print("Después de la función")
        return resultado
    return wrapper


@decorador
def saludar (nombre):
    print(f"Hola {nombre}")

saludar("Juan")