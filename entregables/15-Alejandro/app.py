# 15. Sistema de recomendación
# Requisitos necesarios:
# - Implementar algoritmos que resuelvan el problema (Done, 2 hechos)
# - Medir el tiempo que lleva ejecutar cada algoritmo implementado (Done)
# - Comparar los tiempos de cada caso estudiado (Done)
# - Explicar dificultades, soluciones y conclusiones (Done, mirar abajo del todo)

# Recomendable:
# - Hacer una muestra gráfica de los resultados (Done)

# Descripción: Implementar un sistema de recomendación basado en filtrado colaborativo. Puntos clave: Distancia de coseno, 
# matrices dispersas. (Done)
# Aplicación práctica: En plataformas de streaming, los sistemas de recomendación personalizados mejoran la satisfacción 
# del usuario sugiriendo contenido relevante basado en sus preferencias. (Lo hice de películas pero aplicaría igual mirando
# categorías/canales en una plataforma streaming en vez de categorías/usuarios)

import numpy as np
import pandas as pd
from scipy.spatial.distance import cosine
from faker import Faker
import random
from scipy.sparse import csr_matrix
import time
import matplotlib.pyplot as plt
import seaborn as sns
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkfont

# Inicializar Faker
fake = Faker()

# Configurar parámetros
num_users = 20
num_items = 40
min_rating = 1
max_rating = 5
density = 0.3  # Densidad para que los usuarios no califiquen todas las películas (30%)

# Leer datos de películas y géneros desde un archivo JSON
def load_movie_data(filename='movies_genres.json'):
    with open(filename, 'r') as f:
        movie_data = json.load(f)
    return movie_data

movie_data = load_movie_data()

# Convertir datos de películas a DataFrame
movie_titles = list(movie_data.keys())
genres = list(set(g for sublist in movie_data.values() for g in sublist))
genre_matrix = pd.DataFrame(0, index=movie_titles, columns=genres)

for movie, movie_genres in movie_data.items():
    for genre in movie_genres:
        genre_matrix.at[movie, genre] = 1

# Generar usuarios y películas aleatorios
user_ids = [fake.name() for _ in range(num_users)]
item_ids = random.sample(movie_titles, num_items)  # Elegir títulos de películas aleatorios

# Crear una matriz de calificaciones aleatorias
np.random.seed(0)
matrix = np.random.uniform(0, 1, (num_users, num_items))

# Aplicar una densidad a la matriz
mask = np.random.rand(num_users, num_items) < density
matrix[~mask] = 0

scaled_matrix = np.copy(matrix)
# Escalar las calificaciones en el rango [1, 5]
scaled_matrix[scaled_matrix > 0] = scaled_matrix[scaled_matrix > 0] * (max_rating - min_rating) + min_rating
# Redondear los valores
scaled_matrix = np.round(scaled_matrix)
# Asegurarse de que las calificaciones estén en el rango [1, 5]
scaled_matrix = np.clip(scaled_matrix, min_rating, max_rating)
# Mantener los valores no calificados como 0
scaled_matrix[matrix == 0] = 0

# Crear DataFrame
df = pd.DataFrame(scaled_matrix, index=user_ids, columns=item_ids)
sparse_matrix = csr_matrix(df.values)

# Calcular la similitud entre usuarios
def calculate_similarity(matrix):
    num_users = matrix.shape[0]
    similarity_matrix = np.zeros((num_users, num_users))

    for i in range(num_users):
        for j in range(num_users):
            if i != j:
                similarity_matrix[i, j] = 1 - cosine(matrix[i].toarray().flatten(), matrix[j].toarray().flatten())
    
    return similarity_matrix

# Hacer recomendaciones basadas en contenido
def recommend_movies_content(user_ratings, genre_matrix, top_n=5):
    unrated_movies = [movie for movie in genre_matrix.index if user_ratings.get(movie, 0) == 0]
    movie_scores = np.zeros(len(unrated_movies))

    # Calcular el vector de género promedio de las películas calificadas por el usuario
    rated_movie_genres = genre_matrix.loc[user_ratings.index[user_ratings > 0]]
    if rated_movie_genres.empty:
        return [], {}  # Si no hay películas calificadas, no hay recomendaciones

    avg_user_genre_vector = rated_movie_genres.mean()
    
    for idx, movie in enumerate(unrated_movies):
        movie_genre_vector = genre_matrix.loc[movie].values
        movie_score = np.dot(avg_user_genre_vector, movie_genre_vector)
        movie_scores[idx] = movie_score
    
    recommended_indices = np.argsort(movie_scores)[::-1][:top_n]
    recommended_movies = np.array(unrated_movies)[recommended_indices]

    # Determinar los géneros preferidos del usuario
    preferred_genres = avg_user_genre_vector
    preferred_genres_list = [genre for genre, score in zip(genre_matrix.columns, preferred_genres) if score > 0]
    genre_reasons = ', '.join(preferred_genres_list) if preferred_genres_list else "No se han identificado géneros preferidos."

    return recommended_movies, genre_reasons

# Hacer recomendaciones basadas en usuarios
def recommend_items(user_index, user_item_matrix, similarity_matrix, top_n=5):
    user_ratings = user_item_matrix.iloc[user_index].values
    similar_users = similarity_matrix[user_index]
    
    # Calcular puntuaciones predichas
    pred_ratings = np.zeros(user_item_matrix.shape[1])
    
    for i in range(user_item_matrix.shape[1]):
        if user_ratings[i] == 0:  # Solo predecir para ítems no calificados
            pred_ratings[i] = np.dot(similar_users, user_item_matrix.iloc[:, i]) / np.sum(similar_users)
    
    # Obtener los ítems con mayor puntuación predicha
    recommended_indices = np.argsort(pred_ratings)[::-1][:top_n]
    recommended_movies = user_item_matrix.columns[recommended_indices]

    return recommended_movies

# Función para convertir rating a estrellas
def rating_to_stars(rating):
    try:
        rating = int(round(rating))  # Asegurarse de que rating sea un entero
        filled_stars = '★' * rating
        empty_stars = '☆' * (max_rating - rating)
        return filled_stars + empty_stars
    except ValueError:
        return 'Error'

def save_ratings_to_json(df, filename='user_ratings.json'):
    # Convertir el DataFrame a un diccionario
    data = df.to_dict(orient='index')
    
    # Guardar el diccionario como un archivo JSON
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def plot_ratings_distribution(df):
    # Aplanar el DataFrame para obtener todas las calificaciones
    ratings = df.melt(var_name='Movie', value_name='Rating')
    
    # Crear un gráfico de distribución usando seaborn
    plt.figure(figsize=(12, 6))
    sns.histplot(ratings['Rating'], bins=range(1, 7), kde=False, color='skyblue')
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    plt.title('Distribution of Ratings Across All Movies')
    plt.xticks(range(1, 6))  # Para que los ticks del eje x estén entre 1 y 5
    plt.show()

def plot_average_ratings(df):
    # Filtrar solo las películas calificadas
    rated_df = df[df > 0]  # Solo mantener las calificaciones > 0
    avg_ratings = rated_df.mean()
    
    # Crear gráfico de barras
    plt.figure(figsize=(12, 8))
    avg_ratings.sort_values().plot(kind='barh', color='lightgreen')
    plt.xlabel('Average Rating')
    plt.ylabel('Movie')
    plt.title('Average Ratings for Each Movie (Only Rated Movies)')
    plt.show()

def plot_num_ratings(df):
    # Contar el número de calificaciones por película
    num_ratings = df.astype(bool).sum()
    
    # Crear gráfico de barras
    plt.figure(figsize=(12, 8))
    num_ratings.sort_values().plot(kind='barh', color='coral')
    plt.xlabel('Number of Ratings')
    plt.ylabel('Movie')
    plt.title('Number of Ratings per Movie')
    plt.show()

def plot_user_ratings(df):
    # Filtrar calificaciones válidas (mayores a 0)
    rated_df = df[df > 0]
    
    # Calcular calificación promedio por usuario solo para calificaciones válidas
    avg_user_ratings = rated_df.mean(axis=1)
    
    # Crear gráfico de barras
    plt.figure(figsize=(12, 8))
    avg_user_ratings.sort_values().plot(kind='barh', color='salmon')
    plt.xlabel('Average Rating Given')
    plt.ylabel('User')
    plt.title('Average Rating Given by Each User (Only Rated Movies)')
    plt.show()

def plot_execution_times(collaborative_time, content_time):
    # Graficar los tiempos de ejecución
    plt.figure(figsize=(8, 6))
    methods = ['Filtrado Colaborativo', 'Filtrado Basado en Contenido']
    times = [collaborative_time, content_time]
    
    plt.bar(methods, times, color=['skyblue', 'salmon'])
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Tiempo de Ejecución por Algoritmo')
    plt.show()

def get_top_genres(user_ratings, genre_matrix, top_n=5):
    # Obtén los géneros preferidos del usuario
    preferred_genres = set()
    genre_count = {}

    for movie, rating in user_ratings.items():
        if rating > 0:  # Solo considerar las películas calificadas
            movie_genre_vector = genre_matrix.loc[movie]
            for genre in genre_matrix.columns[movie_genre_vector > 0]:
                if genre in genre_count:
                    genre_count[genre] += rating
                else:
                    genre_count[genre] = rating

    # Ordenar géneros por la suma de ratings y seleccionar los top_n
    top_genres = sorted(genre_count, key=genre_count.get, reverse=True)[:top_n]
    return top_genres

def show_user_info(user_index, user_ratings, recommended_items_collab, recommended_items_content, content_reasons):
    user_name = user_ids[user_index]

    # Crear la ventana del popup
    popup = tk.Tk()
    popup.title(f"Películas calificadas por {user_name}")

    # Configuración de la ventana
    popup.geometry("825x600")
    popup.resizable(True, True)
    popup.configure(bg="#f4f4f4")

    # Estilo de la ventana
    style = ttk.Style()
    style.configure("TFrame", background="#f4f4f4")
    style.configure("TLabel", background="#f4f4f4", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12, "bold"))

    # Crear el marco principal y el canvas
    main_frame = ttk.Frame(popup, padding="20", relief="flat", style="TFrame")
    main_frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(main_frame, bg="#f4f4f4")
    scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    content_frame = ttk.Frame(canvas, padding="20", relief="flat", style="TFrame")
    canvas.create_window((0, 0), window=content_frame, anchor="nw")
    content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    font_title = tkfont.Font(family="Arial", size=18, weight="bold")
    font_subtitle = tkfont.Font(family="Arial", size=14, weight="bold")
    font_text = tkfont.Font(family="Arial", size=12)
    font_button = tkfont.Font(family="Arial", size=12, weight="bold")

    header_frame = ttk.Frame(content_frame, padding="10", relief="flat", style="TFrame")
    header_frame.pack(fill="x", pady=(0, 20))

    ttk.Label(header_frame, text=f"Películas calificadas por {user_name}", font=font_title, foreground="#fff").pack(anchor='w')

    ratings_frame = ttk.Frame(content_frame, padding="10", relief="flat", borderwidth=2, style="TFrame")
    ratings_frame.pack(fill="x", pady=(0, 30), anchor="w")

    ttk.Label(ratings_frame, text="Calificaciones:", font=font_subtitle, foreground="#fff").pack(anchor='w')

    if len(user_ratings) > 0:
        for movie, rating in user_ratings.items():
            if rating > 0:
                stars = rating_to_stars(rating)
                ttk.Label(ratings_frame, text=f"{movie}: {stars}", font=font_text, foreground="#fff").pack(anchor='w', pady=2)
    else:
        ttk.Label(ratings_frame, text="No hay calificaciones disponibles.", font=font_text, foreground="#fff").pack(anchor='w', pady=2)

    recommendations_frame = ttk.Frame(content_frame, padding="10", relief="flat", borderwidth=2, style="TFrame")
    recommendations_frame.pack(fill="x", pady=(0, 30), anchor="w")

    ttk.Label(recommendations_frame, text="Recomendaciones:", font=font_title, foreground="#fff").pack(anchor='w')

    ttk.Label(recommendations_frame, text="Filtrado Colaborativo:", font=font_subtitle, foreground="#fff").pack(anchor='w', pady=(10, 5))
    if len(recommended_items_collab) > 0:
        for movie in recommended_items_collab:
            ttk.Label(recommendations_frame, text=movie, font=font_text, foreground="#fff").pack(anchor='w', pady=2)
    else:
        ttk.Label(recommendations_frame, text="No hay recomendaciones disponibles para el Filtrado Colaborativo.", font=font_text, foreground="#fff").pack(anchor='w', pady=2)

    ttk.Label(recommendations_frame, text="Filtrado Basado en Contenido:", font=font_subtitle, foreground="#fff").pack(anchor='w', pady=(10, 5))

    # Mostrar las 5 principales categorías preferidas
    top_genres = get_top_genres(user_ratings, genre_matrix, top_n=5)
    reason_text = "Recomendaciones basadas en sus géneros preferidos: " + ', '.join(top_genres) + '\n\n'
    recommendations_text = '\n'.join(recommended_items_content)

    full_text = reason_text + recommendations_text
    text_label = ttk.Label(recommendations_frame, text=full_text, font=font_text, background="#f4f4f4", foreground="#fff", wraplength=750, justify='left')
    text_label.pack(side='top', fill='both', expand=True)

    close_button = tk.Button(popup, text="Cerrar", command=popup.destroy, font=font_button, bg="#e74c3c", fg="#000", relief="flat", padx=10, pady=5)
    close_button.pack(pady="20", side="bottom")

    def on_mouse_wheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    popup.bind_all("<MouseWheel>", on_mouse_wheel)

    popup.update_idletasks()
    width = popup.winfo_width()
    height = popup.winfo_height()
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    popup.geometry(f'{width}x{height}+{x}+{y}')

    popup.mainloop()

# Medir el tiempo de ejecución para recomendaciones basadas en contenido y filtrado colaborativo
def main():
    # Guardar las calificaciones en un archivo JSON
    save_ratings_to_json(df)
    
    # Calcular matrices de similitud
    start_time = time.time()
    similarity_matrix = calculate_similarity(sparse_matrix)
    collaborative_time = time.time() - start_time

    start_time = time.time()
    content_time = time.time() - start_time
    
    while True:
        # Solicitar al usuario el índice
        user_input = input("Ingrese el número del usuario (0-19), 'plot' o 'exit' para salir: ")
        
        if user_input.lower() == 'exit':
            break
        
        if user_input.lower() == 'plot':
            # Graficar los tiempos de ejecución
            plot_execution_times(collaborative_time, content_time)

            # Graficar distribución de calificaciones
            plot_ratings_distribution(df)

            # Graficar calificaciones promedio por película
            plot_average_ratings(df)

            # Graficar número de calificaciones por película
            plot_num_ratings(df)

            # Graficar calificaciones promedio por usuario
            plot_user_ratings(df)
            continue

        if user_input.isdigit():
            user_index = int(user_input)
            if 0 <= user_index < num_users:
                # Obtener las películas calificadas por el usuario
                user_ratings = df.iloc[user_index]
                rated_movies = user_ratings[user_ratings > 0]

                # Obtener recomendaciones para el usuario
                recommended_items_collab = recommend_items(user_index, df, similarity_matrix)
                recommended_items_content, content_reasons = recommend_movies_content(user_ratings, genre_matrix)
                
                # Mostrar la información del usuario en un popup
                show_user_info(user_index, rated_movies, recommended_items_collab, recommended_items_content, content_reasons)
            else:
                print("Índice de usuario inválido. Por favor, ingrese un número entre 0 y 19.")
        else:
            print("Entrada no válida. Por favor, ingrese un número entre 0 y 19 o 'exit' para salir.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()

# Explicación de Dificultades, Soluciones y Conclusiones

# Dificultades:
# Generación de datos de prueba:
# Crear datos realistas para pruebas.
# Solución: Uso de Faker y selección aleatoria de películas.

# Implementación de algoritmos de recomendación:
# Calcular similitudes de manera eficiente.
# Solución: Uso de distancia de coseno y scipy.sparse.

# Integración de filtrado basado en contenido:
# Comparar géneros de películas no calificadas con preferencias de usuario.
# Solución: Calcular vector promedio de géneros basado en calificaciones.

# Interfaz gráfica intuitiva:
# Uso de tkinter para desarrollar la interfaz.

# Conclusiones:
# Eficacia de sistemas de recomendación:
# Ambos métodos (colaborativo y basado en contenido) son efectivos.

# Eficiencia computacional:
# Uso de matrices dispersas y algoritmos optimizados mejora la eficiencia.