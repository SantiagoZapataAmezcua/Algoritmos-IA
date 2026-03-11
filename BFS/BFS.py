
from collections import deque

def bfs(grafo, inicio):
    # Un set para guardar nodos visitados y evitar ciclos infinitos o repetir nodos.
    visitados = set()

    # iniciamos la cola en el inicio 
    cola = deque([inicio])

    # Marcamos el inicio como visitado
    visitados.add(inicio)

    #Imprime desde donde estamos empezando
    print(f"Orden de exploración empezando desde {inicio}:")

    # Este ciclo nos dice que mientras haya cola (La cola no sea vacia)
    # seguiremos explorando
    while cola:
        # Extraemos el nodo que llegó primero
        nodo_actual = cola.popleft()
        print(nodo_actual, end=" ")

        # Revisamos los vecinos del nodo actual
        for vecino in grafo[nodo_actual]:
            #Vemos si ya se visito
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)

# Representación del grafo mediante un diccionario (Lista de adyacencia)
grafo_ejemplo = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Ejecución
bfs(grafo_ejemplo, 2)