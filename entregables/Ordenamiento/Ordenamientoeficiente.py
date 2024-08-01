import numpy as np
import time
import matplotlib.pyplot as plt

# Implementaciones de los algoritmos de ordenamiento

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heapsort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            largest = left
        if right < n and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Función para medir el tiempo de ejecución de un algoritmo de ordenamiento
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    end_time = time.time()
    return end_time - start_time

# Función para graficar los resultados
def plot_results(sizes, times, title):
    plt.figure(figsize=(10, 6))
    for alg, time_data in times.items():
        plt.plot(sizes, time_data, label=alg)
    plt.xlabel('Tamaño de la lista')
    plt.ylabel('Tiempo (segundos)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Tamaños de lista para probar
sizes = [1000, 5000, 10000, 50000, 100000, 500000]

# Diccionarios para almacenar los tiempos de cada algoritmo
times = {
    "Quicksort": [],
    "Mergesort": [],
    "Heapsort": []
}

# Probar cada tamaño de lista
for size in sizes:
    np.random.seed(0)
    large_list = np.random.randint(0, 1000000, size=size)

    times["Quicksort"].append(measure_time(quicksort, large_list))
    times["Mergesort"].append(measure_time(mergesort, large_list))
    times["Heapsort"].append(measure_time(heapsort, large_list))

# Graficar los resultados
plot_results(sizes, times, 'Comparación de Tiempos de Algoritmos de Ordenamiento')

# Explicación de dificultades, soluciones y conclusiones
print("""
Dificultades:
- La implementación de Quicksort puede tener problemas de eficiencia en el peor caso si no se elige bien el pivote.
- La mezcla en Mergesort requiere espacio adicional, lo que puede ser un problema para listas muy grandes.
- Heapsort es menos eficiente en listas casi ordenadas debido a la reestructuración constante del heap.

Soluciones:
- Utilizar una estrategia de pivote aleatorio o mediana de tres en Quicksort para mejorar el rendimiento en el peor caso.
- Optimizar el uso de memoria en Mergesort utilizando técnicas in-place (aunque puede ser complejo).
- Aceptar el costo adicional de reestructuración en Heapsort como parte de su algoritmo.

Conclusiones:
- Todos los algoritmos implementados tienen una complejidad promedio de O(n log n), pero su rendimiento real puede variar según la naturaleza de los datos y los casos específicos.
- Quicksort tiende a ser más rápido en la práctica para listas aleatorias, pero puede ser menos fiable en el peor caso sin optimizaciones.
- Mergesort es estable y garantiza O(n log n) en todos los casos, pero con un costo de espacio adicional.
- Heapsort es robusto con una complejidad constante de O(n log n), pero puede ser más lento en listas casi ordenadas debido a su naturaleza de heap.""")

