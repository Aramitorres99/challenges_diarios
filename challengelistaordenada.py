def lista_ordenada():
    list_order = (10,9,8,7,6,5,4,3,2,1)
    number_user = int(input("ingrese un numero para buscar: "))
    if number_user in list_order:
        print(f"el numero {number_user} esta en la lista {list_order}")
    else:
        print("El numero no esta en la lista")
    return number_user
        
lista_ordenada()