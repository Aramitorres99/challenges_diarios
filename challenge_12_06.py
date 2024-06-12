
# DIA 2
# Tabla de Multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.


#funcion multiplicadora
def multiply_number():
    
    print(f"Esta es la tabla de multiplicar del numero {number_user}")
    #itera el numero entre el 1 y el 10 xq hasta ese rango quiero multiplicar 
    for i in range (1,11):
        #en la variable result se guarda la multiplicacion del numero del usuario por el iterador
        result = number_user * i
        #se imprime el numero del usuario por el iterador y el resultado guardado en la variable result
        print(f"{number_user} * {i} = {result}")
        
#pedir al usuario que ingrese el numero que quiere multiplicar
number_user = int(input("ingrese un numero: "))
#llamamos a la funcion
multiply_number()