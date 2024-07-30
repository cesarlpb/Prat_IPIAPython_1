import random
import pickle
import json
import numpy as np
from collections import deque
import time
from django.shortcuts import render
from django.http import JsonResponse
import matplotlib.pyplot as plt
import matplotlib
import io
import base64

#1. CREAMOS UNA FUNCION PARA GENERAR LABERINTOS AL AZAR
def generar_laberinto(width, height, camino_extra=8):
    laberinto = np.ones((height, width), dtype=int)
    
    #punto de inicio aleatorio en la primera columna
    start_y = random.randrange(1, height, 2)
    start_x = 0
    laberinto[start_y, start_x] = 0
    laberinto[start_y, start_x + 1] = 0
    
    #Punto de salida aleatorio en la última columna
    end_y = random.randrange(1, height, 2)
    end_x = width - 1
    laberinto[end_y, end_x] = 0
    
    paredes = [(start_x+1, start_y, nx, ny) for nx, ny in celdas_vecinas(start_x+1, start_y, width, height)]
    random.shuffle(paredes)

    #Generamos los caminos borrando las paredes
    while paredes:
        x, y, nx, ny = paredes.pop()
        if laberinto[ny, nx] == 1:
            laberinto[ny, nx] = 0
            laberinto[(y + ny) // 2, (x + nx) // 2] = 0
            for nnx, nny in celdas_vecinas(nx, ny, width, height):
                if laberinto[nny, nnx] == 1:
                    paredes.append((nx, ny, nnx, nny))
            random.shuffle(paredes)

    # Añadimos caminos extras borrando bloques aleatorios de paredes
    for _ in range(camino_extra):
        añadir_camino_extra(laberinto)
    
    return laberinto, (start_x, start_y), (end_x, end_y)

#Devuelve las 4 direcciones a 2 casillas para el while anterior
def celdas_vecinas(x, y, width, height):
    vecinos=[]
    if x > 1: vecinos.append((x - 2, y))
    if x < width - 2: vecinos.append((x + 2, y))
    if y > 1: vecinos.append((x, y - 2))
    if y < height - 2: vecinos.append((x, y + 2))
    return vecinos    

#Para que exista más de una solución correcta
def añadir_camino_extra(laberinto):
    height, width = laberinto.shape
    while True:
        x, y = random.randrange(1, width, 2), random.randrange(1, height, 2)
        if laberinto[y, x] == 0:
            vecinos = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            random.shuffle(vecinos)
            for nx, ny in vecinos:
                if 0 < nx < width-1 and 0 < ny < height-1:
                    if laberinto[ny, nx] == 1:
                        laberinto[ny, nx] = 0
                        return


#2. CREAMOS UNA FUNCION PARA DETERMINAR QUE CAMINO ES EL MÁS CORTO EN EL LABERITNO
def bfs(laberinto, start, end):
    height, width = laberinto.shape
    queue = deque([start]) #cola de los que se estan analizando
    visited = set([start]) #lista de los visitados
    parent = {start: None} #padre del current

    while queue:
        current = queue.popleft()
        if current == end: #cuando current llega al end, crea la lista añadiendo las coordenades del padre cada vez
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1] #invertimos esa lista para tener el orden correcto del path 

        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #direcciones posibles (izq, dxa, arriba, abajo)
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and laberinto[ny, nx] == 0 and (nx, ny) not in visited:
                #si el siguiente es un camino no visitado previamente, se añade a la cola y a la lista de visitados, guardando las coordenada del padre
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)

    return None

def index(request):
    return render(request, 'index.html')

#Visualizamos el laberinto
def dibuja_laberinto(laberinto, path = None):
    matplotlib.use('agg')
    fig, ax = plt.subplots()
    ax.imshow(laberinto, cmap='binary')
    if path:
        path_x, path_y = zip(*path)
        ax.plot(path_x, path_y, color='red')  
    plt.xticks([]), plt.yticks([])

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi= 110, bbox_inches='tight', transparent="True", pad_inches=0.2)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()
    return image_base64


#Se genera una vez el usuario introduce las medidas y le da al botón
def generate_maze(request):
    width = int(request.GET.get('width', 50))
    if width % 2 == 0:
        width += 1
    height = int(request.GET.get('height', 50))
    if height % 2 == 0:
        height += 1

    start_time_laberinto= time.time_ns()
    laberinto, start, end = generar_laberinto(width, height, 8)
    end_time_laberinto = time.time_ns()

    image_base64 = dibuja_laberinto(laberinto)

    return JsonResponse({
        'image': image_base64,
        'laberinto_time': (end_time_laberinto - start_time_laberinto) / 1000000,
        'laberinto': json.dumps(pickle.dumps(laberinto).decode('latin-1')),
        'start_y': start[1],
        'end_y': end[1]
    })


#Generamos la solución mediante el BFS cuando el usuario le da al botón
def solve_maze(request):
    laberinto = pickle.loads(json.loads(request.POST.get('laberinto')).encode('latin-1'))
    start_y = int(request.POST.get('start_y', 25))
    end_y = int(request.POST.get('end_y', 25))
    
    height, width = laberinto.shape
    start = (0, start_y)
    end = (width-1, end_y)
    start_time_bfs = time.time_ns()
    path = bfs(laberinto, start, end)
    end_time_bfs = time.time_ns()

    image_base64 = dibuja_laberinto(laberinto, path)

    return JsonResponse({
        'image': image_base64,
        'bfs_time': (end_time_bfs - start_time_bfs) / 1000000
    })


