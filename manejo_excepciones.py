# Excepciones son eventos que ocurren dentro del programa
# que interrumpen el flujo normal de ejecución del programa.
# Las excepciones pueden ser manejadas utilizando bloques try-except.

print("*** Manejo de Excepciones ***")

def dividir(numerador, denominador):
    try:
        # Revisamos si el denominador es igual a 0
        if denominador == 0:
            raise Exception("El denominador no puede ser cero.")
        resultado = numerador/denominador
        # return resultado
        print(f"El resultado de la división es: {resultado}")
    # except ZeroDivisionError:
    #     print("Error: No se puede dividir por cero.")
    # except TypeError:
    #     print("Error: Tipo de dato no válido para la división.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        
    else:
        print("La división se realizó correctamente.")
        # Se ejecuta si no se produce ninguna excepción

    # Este es mas generico para los errores que no se han manejado especificamente
    finally:
        print("Esta sección se ejecuta siempre, haya o no una excepción.")

dividir(10,2)
dividir(10,0) # Esto genera una excepción de tipo ZeroDivisionError
dividir(10,'0') # Esto genera una excepción de tipo TypeError