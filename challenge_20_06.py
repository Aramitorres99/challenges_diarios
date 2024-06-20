#Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable 
# (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, números y símbolos.

import random  # Importa el módulo random para seleccionar caracteres aleatorios
import string  # Importa el módulo string para acceder a conjuntos de caracteres

# Define una función para generar una contraseña de longitud especificada
def generar_contraseña(longitud):
    # Verifica que la longitud esté entre 8 y 16 caracteres, de lo contrario lanza un error
    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud debe estar entre 8 y 16 caracteres")
    
    # Define el conjunto de caracteres permitidos: letras mayúsculas, minúsculas, dígitos y símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Genera una contraseña seleccionando aleatoriamente caracteres del conjunto permitido
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña  # Devuelve la contraseña generada

# Define una función para obtener la longitud deseada de la contraseña por parte del usuario
def obtener_longitud():
    while True:  # Bucle infinito hasta que se obtenga una longitud válida
        try:
            # Solicita al usuario que introduzca la longitud de la contraseña
            longitud = int(input("Introduce la longitud de la contraseña (entre 8 y 16): "))
            if 8 <= longitud <= 16:
                return longitud  # Si la longitud es válida, la devuelve
            else:
                # Informa al usuario si la longitud no está en el rango permitido
                print("La longitud debe estar entre 8 y 16 caracteres.")
        except ValueError:
            # Informa al usuario si la entrada no es un número válido
            print("Por favor, introduce un número válido.")

# Función principal que orquesta el flujo del programa
def main():
    longitud = obtener_longitud()  # Obtiene la longitud deseada de la contraseña
    contraseña = generar_contraseña(longitud)  # Genera la contraseña con la longitud especificada
    print(f"Tu contraseña segura es: {contraseña}")  # Muestra la contraseña generada al usuario

# Ejecuta la función principal solo si el script se ejecuta directamente
if __name__ == "__main__":
    main()
