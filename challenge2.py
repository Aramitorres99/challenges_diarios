#Ordenamiento simple: Escribe una función que ordena una lista de 5 enteros 
# utilizando cualquier método de ordenamiento que prefieras (por ejemplo, burbuja, inserción, selección).

def order_list(list_):
    for i in range (1, len(list_)):
        clue = list_[i]
        j = i-1
        
        while j >=0 and clue < list_[j]:
            list_[j + 1] = list_[j]
            j -=1
            
        list_[j + 1] = clue
        
    return list_

list_ = [54, 43, 50, 68, 23]
print(f"Lista original {list_}")
list_order = order_list(list_)
print(f"Lista ordenada {list_order}")
        
        