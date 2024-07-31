#Implementa una función recursiva para calcular el factorial de un número pequeño (por ejemplo, 5).


def factorial(numero):
    #caso base 
    
    if numero == 0 or numero == 1:
        return 1
    
    else:
        return numero * factorial(numero -1)
        
       
print(factorial(5))