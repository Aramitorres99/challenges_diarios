# Piloto de eventos (Priority Queue): Implementa una cola de prioridad 
# utilizando una lista para insertar y eliminar 5 elementos.

class ColaDePrioridad:
    def __init__(self):
        self.cola = []
        
    def insert(self, element):
        self.cola.append(element)
        self.cola.sort()
        
    def delete(self):
        if not self.is_empty():
            return self.cola.pop(0)
        else:
            return "La cola esta vacia"
        
    def is_empty(self):
        return len(self.cola) == 0
    
    def display(self):
        return self.cola
    
#ejemplo
colaproridad = ColaDePrioridad()
elements = [4, 1, 2, 3, 5]

#Insertar elementos
for element in elements:
    colaproridad.insert(element)
    print(f'Lo insertado fue {element}, en la cola: {colaproridad.display()}')
    

#eliminar elementos 
for _ in range(len(elements)):
    removed = colaproridad.delete()
    print(f'Elimnado {removed} de la cola: {colaproridad.display()}')