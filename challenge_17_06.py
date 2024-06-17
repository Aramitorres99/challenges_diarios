#Crear un Diccionario: Escribe un programa que crea un diccionario a partir de dos listas dadas: una de claves y otra de valores.

def dictionary():
    my_dictionary = {
        'Nombre': 'Abril',
        'Edad': 23,
        'Ciudad' : 'Luque'
    }
    return my_dictionary
dictionary_user = dictionary()
print(dictionary_user)