#Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al usuario jugar piedra, papel o tijeras contra la computadora.

import random 

def turno_user():
    word = ['piedra', 'papel', 'tijera']
    while True:
       usu_word = input("escribe una palabra: piedra, papel o tijera: ")
       if usu_word in word:
           return usu_word
       else:
           print("palabra no valida, intenta de nuevo")
           
def turno_compu():
    word = ['piedra', 'papel', 'tijera']
    return random.choice(word)

def winner(user, computador):
    if user == computador:
        return "empate"
    
    elif (user == 'piedra' and computador == 'tijera') or \
        (user == 'papel' and computador == 'piedra') or \
        (user == 'tijera' and computador == 'papel'):
            return "ganaste"
        
    else:
        return "te gano la compu xd"
    
def jugar():
    user = turno_user()
    computador = turno_compu()
    
    print(f"elegiste {user}")
    print(f"la compu eligio {computador}")
    
    result = winner(user, computador)
    print(result)
    
jugar()