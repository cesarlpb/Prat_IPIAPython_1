from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
import networkx as nx
import matplotlib
matplotlib.use('Agg')  # Usar un backend no interactivo para Matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from .forms import TSPForm
import time
from .models import RouteResult

def plot_graph(G, tour, current_node, pos):
    """Genera una imagen del gráfico en formato base64."""
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    path_edges = list(zip(tour, tour[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='green', node_size=500)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_data = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()
    return image_data

def nearest_neighbor_tsp(G, start_node):
    """Resuelve el problema del vendedor viajero usando el algoritmo del vecino más cercano."""
    pos = nx.spring_layout(G)
    unvisited = set(G.nodes)
    unvisited.remove(start_node)
    tour = [start_node]
    current_node = start_node
    image_uris = [plot_graph(G, tour, current_node, pos)]

    while unvisited:
        next_node = min(unvisited, key=lambda node: G[current_node][node]['weight'])
        unvisited.remove(next_node)
        tour.append(next_node)
        current_node = next_node
        image_uris.append(plot_graph(G, tour, current_node, pos))

    tour.append(tour[0])
    image_uris.append(plot_graph(G, tour, current_node, pos))
    tour_cost = sum(G[tour[i]][tour[i + 1]]['weight'] for i in range(len(tour) - 1))

    return tour, tour_cost, image_uris

def tsp_view(request):
    """Maneja el formulario para generar y mostrar el resultado del TSP."""
    if request.method == 'POST':
        form = TSPForm(request.POST)
        if form.is_valid():
            num_nodes = form.cleaned_data['num_nodes']
            min_weight = form.cleaned_data['min_weight']
            max_weight = form.cleaned_data['max_weight']
            start_node = form.cleaned_data['start_node']

            G = nx.complete_graph(num_nodes)
            for u, v in G.edges():
                G.edges[u, v]['weight'] = random.randint(min_weight, max_weight)

            start_time = time.time()
            tour, tour_cost, image_uris = nearest_neighbor_tsp(G, start_node)
            end_time = time.time()

            execution_time = end_time - start_time

            # Guardar los resultados en la sesión
            request.session['results'] = request.session.get('results', [])
            request.session['results'].append({
                'tour': tour,
                'tour_cost': tour_cost,
                'execution_time': execution_time,
                'images': image_uris
            })

            return render(request, 'tsp_app/results.html', {
                'tour': tour,
                'tour_cost': tour_cost,
                'images': image_uris
            })
    else:
        form = TSPForm()
    return render(request, 'tsp_app/form.html', {'form': form})

def compare_results(request):
    """Muestra y compara los resultados almacenados en la sesión."""
    results = request.session.get('results', [])
    return render(request, 'tsp_app/compare_results.html', {'results': results})

def delete_all_results(request):
    """Borra todos los resultados almacenados en la sesión."""
    request.session['results'] = []
    return redirect('compare_results')
