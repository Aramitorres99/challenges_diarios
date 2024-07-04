#Recorrido en amplitud (BFS): Implementa un recorrido BFS para un gráfico simple con 5 nodos.
from collections import deque

#mi grafo representado con una lista de adyacencia

grafo = {
    1: [2, 3], 
    2: [1, 4],
    3: [4, 5],
    4: [2, 3],
    5: [3]
}


def bfs_grafo(grafo, node_initial):
    visited = set()
    
    cola = deque([node_initial])
    
    while cola:
        node = cola.popleft()
        if node not in visited:
            visited.add(node)
            print(node)
        
        for neighbor in grafo[node]:
            if neighbor not in visited:
                cola.append(neighbor)
    

bfs_grafo(grafo, 1)