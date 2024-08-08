import random  # Importa la biblioteca random para generar números aleatorios
import networkx as nx  # Importa la biblioteca NetworkX para trabajar con grafos
import matplotlib.pyplot as plt  # Importa la biblioteca matplotlib para visualización
import numpy as np  # Importa la biblioteca numpy para trabajar con matrices
import time  # Importa la biblioteca time para medir tiempos de ejecución

# Generar un grafo dirigido con pesos
def generate_directed_graph(num_nodes, weight_range=(1, 100)):
    G = nx.DiGraph()  # Crear un grafo dirigido
    for i in range(num_nodes):  # Iterar sobre cada nodo i
        for j in range(num_nodes):  # Iterar sobre cada nodo j
            if i != j:  # Evitar lazos (self-loops)
                # Añadir una arista con un peso aleatorio entre los nodos i y j
                G.add_edge(i, j, weight=random.randint(*weight_range))
    return G  # Devolver el grafo generado

# Algoritmo de Floyd-Warshall con predecesores
def floyd_warshall(G):
    n = G.number_of_nodes()  # Obtener el número de nodos del grafo
    dist = np.full((n, n), float('inf'))  # Crear una matriz de distancias inicializada a infinito
    np.fill_diagonal(dist, 0)  # Poner 0 en la diagonal (distancia a sí mismo es 0)
    pred = np.full((n, n), None)  # Crear una matriz de predecesores inicializada a None
    
    for u, v, data in G.edges(data=True):  # Iterar sobre cada arista del grafo
        dist[u][v] = data['weight']  # Inicializar la distancia con el peso de la arista
        pred[u][v] = u  # Inicializar el predecesor
    
    start_time = time.time()  # Registrar el tiempo de inicio del algoritmo
    # Algoritmo de Floyd-Warshall
    for k in range(n):  # Iterar sobre cada nodo k como nodo intermedio
        for i in range(n):  # Iterar sobre cada nodo i como nodo de origen
            for j in range(n):  # Iterar sobre cada nodo j como nodo de destino
                if dist[i][j] > dist[i][k] + dist[k][j]:  # Si se encuentra un camino más corto
                    dist[i][j] = dist[i][k] + dist[k][j]  # Actualizar la distancia
                    pred[i][j] = pred[k][j]  # Actualizar el predecesor
    end_time = time.time()  # Registrar el tiempo de finalización del algoritmo
    tiempo_ejecucion = end_time - start_time  # Calcular el tiempo de ejecución
    
    return dist, pred, tiempo_ejecucion  # Devolver las matrices de distancias y predecesores, y el tiempo de ejecución

# Reconstrucción del camino más corto
def reconstruct_path(pred, start, end):
    if pred[start][end] is None:  # Si no hay camino
        return []  # Retornar una lista vacía
    path = [end]  # Iniciar el camino con el nodo final
    while end != start:  # Mientras no se llegue al nodo inicial
        end = pred[start][end]  # Actualizar el nodo final al predecesor
        path.append(end)  # Añadir el nodo al camino
    path.reverse()  # Invertir el camino para que vaya del inicio al final
    return path  # Devolver el camino reconstruido

# Visualización del grafo y el camino más corto
def plot_shortest_path(G, path):
    pos = nx.spring_layout(G)  # Calcular la disposición de los nodos
    plt.figure()  # Crear una nueva figura
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, arrowsize=20)  # Dibujar el grafo
    
    path_edges = list(zip(path, path[1:]))  # Crear una lista de aristas en el camino más corto
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)  # Dibujar las aristas del camino más corto
    nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='green', node_size=500)  # Dibujar los nodos del camino más corto
    
    edge_labels = nx.get_edge_attributes(G, 'weight')  # Obtener los pesos de las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Dibujar los pesos de las aristas
    
    plt.title('Camino más corto')  # Título de la gráfica
    plt.show()  # Mostrar la gráfica

# Visualización del grafo original
def plot_graph(G, title=''):
    pos = nx.spring_layout(G)  # Calcular la disposición de los nodos
    plt.figure()  # Crear una nueva figura
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, arrowsize=20)  # Dibujar el grafo
    edge_labels = nx.get_edge_attributes(G, 'weight')  # Obtener los pesos de las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Dibujar los pesos de las aristas
    plt.title(title)  # Título de la gráfica
    plt.show()  # Mostrar la gráfica

# Función principal para realizar las pruebas y mediciones
def main():
    num_nodes_list = [5, 10, 15, 20, 25, 30, 35, 40]  # Lista de diferentes tamaños de grafos
    tiempos_fw = []  # Lista para guardar los tiempos de ejecución de Floyd-Warshall
    teoricos_fw = []  # Lista para guardar los tiempos teóricos

    for num_nodes in num_nodes_list:  # Iterar sobre cada tamaño de grafo
        G = generate_directed_graph(num_nodes)  # Generar un grafo dirigido
        
        # Ejecutar Floyd-Warshall
        dist_matrix, pred_matrix, tiempo_fw = floyd_warshall(G)
        tiempos_fw.append(tiempo_fw)  # Guardar el tiempo de ejecución
        
        # Calcular el tiempo teórico Θ(n^3)
        teorico_fw = num_nodes ** 3
        teoricos_fw.append(teorico_fw)  # Guardar el tiempo teórico
        
        print(f'Número de nodos: {num_nodes}')
        print(f'Tiempo de ejecución de Floyd-Warshall: {tiempo_fw:.4f} segundos')
        print("Matriz de distancias:")
        print(dist_matrix)
        
        start_node = 0
        end_node = num_nodes - 1
        path = reconstruct_path(pred_matrix, start_node, end_node)  # Reconstruir el camino más corto
        
        print(f'Camino más corto de {start_node} a {end_node}: {path}')
        
        # Mostrar gráfico del grafo y el camino más corto
        plot_shortest_path(G, path)
        
        # Mostrar gráfico del grafo original
        plot_graph(G, title=f'Grafo dirigido con {num_nodes} nodos')
    
    # Mostrar resultados de comparación de tiempos de ejecución
    plt.figure()  # Crear una nueva figura
    plt.plot(num_nodes_list, tiempos_fw, label='Floyd-Warshall Empírico', marker='o')  # Graficar los tiempos de ejecución empíricos
    plt.plot(num_nodes_list, [t / max(teoricos_fw) * max(tiempos_fw) for t in teoricos_fw], label='Θ(n^3) Teórico', linestyle='--', marker='x')  # Graficar los tiempos teóricos
    plt.xlabel('Número de nodos')  # Etiqueta del eje X
    plt.ylabel('Tiempo de ejecución (segundos)')  # Etiqueta del eje Y
    plt.title('Comparación de tiempos de ejecución de Floyd-Warshall')  # Título de la gráfica
    plt.legend()  # Mostrar la leyenda
    plt.show()  # Mostrar la gráfica

if __name__ == '__main__':
    main()  # Ejecutar la función principal
