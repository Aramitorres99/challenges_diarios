#Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente

def order_list():
    #pedirle la lista al usuario
    list_user = input("Introduce una lista de numeros separados por espacios: ")
    #para cambiar a numeros
    list_number = list(map(int, list_user.split()))
    #para ordenar de forma ascendente
    list_order = sorted(list_number)
    #para imprimir la lista ordenada
    print(f"Lista ordenada: {list_order}")

#llamando a la funcion    
order_list()