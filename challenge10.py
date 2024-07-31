#Implementa una función que elimina los elementos duplicados de una lista de 10 enteros.


def eliminar_duplicados(lista_numeros):
    # Convertir la lista a un conjunto para eliminar duplicados y luego convertirlo de nuevo a una lista
    return list(set(lista_numeros))

# Probando la función con la lista dada
lista_sin_duplicados = [1, 2, 3, 4, 5, 6, 6, 7, 7, 1]
print(eliminar_duplicados(lista_sin_duplicados))  # imprime una lista sin duplicados, por ejemplo [1, 2, 3, 4, 5, 6, 7]
