# %%
import time
from mi_aplicacion.views import longest_unique_substring  # Ajusta la importación según tu estructura

# Función para medir tiempo de ejecución
def medir_tiempo(func, arg):
    start_time = time.time()
    result = func(arg)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Casos de prueba
casos_de_prueba = [
    "abcde",            # Caso corto y simple
    "a1b2c3!",          # Caso corto y complejo
    "abcdefgh",         # Caso medio y simple
    "a1b2c3d4e5f6!",    # Caso medio y complejo
    "abcdefghijklmnopqrstuvwxyz",  # Caso largo y simple
    "a1b2c3d4e5f6g7h8i9j0k!l@m#",  # Caso largo y complejo
]

# Evaluación de los casos de prueba
resultados = []
for caso in casos_de_prueba:
    resultado, tiempo = medir_tiempo(longest_unique_substring, caso)
    resultados.append((caso, resultado, tiempo))

# Mostrar resultados
for caso, longitud, tiempo in resultados:
    print(f"Entrada: {caso}")
    print(f"Longitud de la cadena más larga sin caracteres repetidos: {longitud}")
    print(f"Tiempo de ejecución: {tiempo:.5f} segundos\n")

# Opcional: Guardar los resultados en un archivo para análisis posterior
with open("resultados_comparacion.txt", "w") as file:
    for caso, longitud, tiempo in resultados:
        file.write(f"Entrada: {caso}\n")
        file.write(f"Longitud de la cadena más larga sin caracteres repetidos: {longitud}\n")
        file.write(f"Tiempo de ejecución: {tiempo:.5f} segundos\n\n")
# %%