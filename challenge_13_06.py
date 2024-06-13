#Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.

def count_vowels(word_user):
    #creo una lista con las vocales
    vowels = ['a', 'e', 'i', 'o', 'u']
    #cree un contador para las vocales
    c_vowels = 0
    #recorro la palabra que ingresa el usuario
    for leter in word_user:
        #Verifico letra por letra y veo si alguna de ellas es una vocal
        if leter.lower() in vowels:
            #si eso ocurre, le sumo el contador de vocales
            c_vowels +=1
    #retorno la cantidad de vocales que se encuentra
    return c_vowels

#pido al usuario que ingrese una palabra
word_user = input("Ingrese una palabra: ")
#guardo lo retornado de la funcion en una variable 
result = count_vowels(word_user)
#imprimo la palabra ingresada con la cantidad de vocales existentes en la misma
print(f"la palabra {word_user} tiene {result} vocales")