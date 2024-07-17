# Pilas y colas: Implementa las operaciones básicas de una pila y/o una cola para 5 elementos.


class Stack:
    def __init__(self):
        self.stack = []
        
        #insertar elemento en la parte superior de la pila
    def push(self, element):
        self.stack.append(element)
        
        
        
        #eliminar y devolver el elemento en la parte superior de la pila
    def pop(self):
        if self.is_empty():
            return 'La pila esta vacia'
        return self.stack.pop()
    
    
        #devolver el elemento en la parte superior de la pila sin eliminarlo
    def peek(self):
        if self.is_empty():
            return 'La pila esta vacia'
        return self.stack[-1]
    
    
    
        #Comprobar si la pila esta vacia
    def is_empty(self):
        return len(self.stack)== 0

        
        
        #Devolver el numero de elementos en la pila
    def size(self):
        return len(self.stack)
    
    
    
#ejemplos de uso

pila = Stack()
pila.push(2)
pila.push(4)
pila.push(6)
print(f"Elemento en la cima: {pila.peek()}")  # Elemento en la cima: 3
print(f"Eliminar elemento: {pila.pop()}")     #Eliminar elemento: 3
print(f"Tamaño de la pila: {pila.size()}")    # Tamaño de la pila: 2
print(f"¿La pila está vacía?: {pila.is_empty()}") #pregunta si la pila esta vacia, en caso de que si, retorna false