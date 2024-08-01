#%%
import pandas as pd
import tkinter as tk
from tkinter import ttk
import time

# Leer el archivo CSV
data = pd.read_csv('data.csv')

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, [value])
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value.append(value)
                    return
                if current.next is None:
                    break
                current = current.next
            new_node = Node(key, [value])
            current.next = new_node
            self.size += 1

    def search(self, key):
        Pelis = []
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                Pelis.extend(current.value)
            current = current.next

        if Pelis:
            return Pelis
        else:
            raise KeyError(key)

    def remove(self, key):
        index = self._hash(key)
        previous = None
        current = self.table[index]

        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

        raise KeyError(key)

    def __len__(self):
        return self.size

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

# Crear y llenar la tabla hash
ht = HashTable(2000000)
df = pd.DataFrame(data)

for index, row in df.iterrows():
    ht.insert(row["title"], row)
# interfaz de programa
class MovieSearcher:
    def __init__(self, root, hashtable):
        self.root = root
        self.ht = hashtable
        self.results = []
        self.current_index = 0

        self.search_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.counter_var = tk.StringVar()

        self.search_label = ttk.Label(root, text="Buscar Película:")
        self.search_label.pack(pady=10)

        self.search_entry = ttk.Entry(root, textvariable=self.search_var, width=50)
        self.search_entry.pack(pady=10)

        self.search_button = ttk.Button(root, text="Buscar", command=self.search_movie)
        self.search_button.pack(pady=10)

        self.counter_label = ttk.Label(root, textvariable=self.counter_var)
        self.counter_label.pack(pady=10)

        self.result_label = ttk.Label(root, textvariable=self.result_var, wraplength=400)
        self.result_label.pack(pady=20)

        self.prev_button = ttk.Button(root, text="Anterior", command=self.show_previous_result)
        self.prev_button.pack(pady=10)
        self.prev_button.config(state=tk.DISABLED)

        self.next_button = ttk.Button(root, text="Siguiente", command=self.show_next_result)
        self.next_button.pack(pady=10)
        self.next_button.config(state=tk.DISABLED)

    def search_movie(self):
        query = self.search_var.get().strip()
        try:
            inicio = time.time()
            self.results = self.ht.search(query)
            self.current_index = 0
            if self.results:
                self.show_result()
                self.update_navigation_buttons()
                final= time.time()
                tiempo = final - inicio
                print(tiempo)

            else:
                self.result_var.set("No se encontró la película.")
                self.next_button.config(state=tk.DISABLED)
                self.prev_button.config(state=tk.DISABLED)
        except KeyError:
            self.result_var.set("No se encontró la película.")
            self.next_button.config(state=tk.DISABLED)
            self.prev_button.config(state=tk.DISABLED)

    def show_result(self):
        if self.results:
            result = self.results[self.current_index]
            self.result_var.set(result.to_string())
            self.counter_var.set(f"Resultado {self.current_index + 1} de {len(self.results)}")

    def show_next_result(self):
        if self.results:
            self.current_index = (self.current_index + 1) % len(self.results)
            self.show_result()
            self.update_navigation_buttons()

    def show_previous_result(self):
        if self.results:
            self.current_index = (self.current_index - 1) % len(self.results)
            self.show_result()
            self.update_navigation_buttons()

    def update_navigation_buttons(self):
        if len(self.results) > 1:
            self.next_button.config(state=tk.NORMAL)
        else:
            self.next_button.config(state=tk.DISABLED)

        if self.current_index > 0:
            self.prev_button.config(state=tk.NORMAL)
        else:
            self.prev_button.config(state=tk.DISABLED)

# Crear la ventana principal
root = tk.Tk()
root.title("Buscador de Películas")

movie_searcher = MovieSearcher(root, ht)

root.mainloop()

# El proyecto ya está bastante bien, para tenerlo listo para que destaque en portafolio
# Algunas cosas para ponerlo en portafolio
# TODO: 
# [ ] opcional - Ocultar botón anterior si el índice es 0
# [ ] opcional - Mostrar Siguiente solo si hay más de un resultado
# [ ] recomendable - Ponerle un logo y nombre al proyecto
# [ ] recomendable para facilitar pruebas de la app - Revisar cómo se puede hacer un ejecutable que cualquiera pueda usar indicándole el CSV a leer
# [ ] recomendable para aprovechar el tiempo dedicado - Subir al portafolio como app descargable + algún CSV de prueba
#   [ ] recomendable - escribir un post que explique tu experiencia y lo que aprendiste con este proyecto para que muestres tu conocimiento // si subes el código también considera colocar un poco de comentarios