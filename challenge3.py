#Recorrido en profundidad (DFS): Implementa un recorrido DFS para un gráfico simple con 5 nodos.

#mi grafo representado con una lista de adyacencia
grafo = {
    1: [2, 3], 
    2: [1, 4],
    3: [4, 5],
    4: [2, 3],
    5: [3]
}

def dfs_grafo(grafo, node, visited):
    visited.add(node)
    print(node, end=' ')
    #recorro todos los vecinos del grafo en el nodo actual
    for neighbor in grafo[node]:
        #si el vecino no esta en visitados procede a explorar este nodo
        if neighbor not in visited:
            dfs_grafo(grafo, neighbor, visited)
            
visited = set()

print("Recorrido en amplitud del grafo comenzando desde el nodo 1")
dfs_grafo(grafo, 1, visited)