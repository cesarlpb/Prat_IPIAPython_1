
# El algoritmo KMP (Knuth-Morris-Pratt) es un método eficiente para buscar un patrón dentro de un texto. Fue diseñado por Donald Knuth, Vaughan Pratt y James H. Morris en 1977. Su ventaja principal sobre otros métodos de búsqueda es que evita retrocesos innecesarios en el texto al encontrar desajustes entre el patrón y el texto.


from django.shortcuts import render
from .algoritmo_kmp import kmp_search
import time
import matplotlib.pyplot as plt
import os 
from django.conf import settings




def search_pattern(request): # Esta función maneja la lógica para buscar patrones en un texto usando el algoritmo KMP.
    context = {}  # Inicializa un diccionario para pasar datos a la plantilla.
    if request.method == 'POST':  # Verifica si la solicitud es de tipo POST.
        text = request.POST.get('text')  # Obtiene el texto del formulario enviado.
        pattern = request.POST.get('pattern')  # Obtiene el patrón del formulario enviado.
        
        # Multiplicar el texto por 1000 para aumentar el tiempo de procesamiento.
        large_text = text * 1000
        
        # Calcular posiciones y recuento en el texto original usando el algoritmo KMP.
        positions = kmp_search(text, pattern)  # Llama a la función kmp_search para encontrar las posiciones del patrón en el texto.
        count = len(positions)  # Calcula cuántas veces se encontró el patrón.

        # Bucle de 10 veces con texto multiplicado para medir el tiempo de ejecución.
        start_time_10 = time.time()  # Inicia el temporizador.
        for _ in range(10):  # Ejecuta la búsqueda 10 veces.
            kmp_search(large_text, pattern)  # Realiza la búsqueda en el texto ampliado.
        end_time_10 = time.time()  # Termina el temporizador.
        duration_10 = end_time_10 - start_time_10  # Calcula la duración total.

        # Bucle de 100 veces 
        start_time_100 = time.time()  
        for _ in range(100):  
            kmp_search(large_text, pattern)  
        end_time_100 = time.time()  
        duration_100 = end_time_100 - start_time_100  

        # Bucle de 500 veces 
        start_time_500 = time.time()  
        for _ in range(500):  
            kmp_search(large_text, pattern)  
        end_time_500 = time.time()  
        duration_500 = end_time_500 - start_time_500  

        # Bucle de 1000 veces 
        start_time_1000 = time.time()  
        for _ in range(1000):  
            kmp_search(large_text, pattern) 
        end_time_1000 = time.time()  
        duration_1000 = end_time_1000 - start_time_1000  

        # Gráfico.
        x = [10, 100, 500, 1000]  # Eje X representa el número de repeticiones.
        y = [duration_10, duration_100, duration_500, duration_1000]  # Eje Y representa el tiempo de ejecución.
        plt.plot(x, y, marker='o')  # Crea un gráfico de líneas con marcadores.
        plt.title('Tiempo de Ejecución del Algoritmo KMP')  # Título del gráfico.
        plt.xlabel('Número de Repeticiones')  # Etiqueta del eje X.
        plt.ylabel('Tiempo (segundos)')  # Etiqueta del eje Y.
        plt.grid(True)  # Activa la cuadrícula en el gráfico.

        # Crear un directorio para almacenar los gráficos, si no existe.
        static_dir = os.path.join(settings.BASE_DIR, 'static', 'proyecto_7_app')  # Ruta al directorio estático.
        if not os.path.exists(static_dir):  # Verifica si el directorio no existe.
            os.makedirs(static_dir)  # Crea el directorio.

        # Guardar el gráfico en un archivo PNG.
        graph_path = os.path.join(static_dir, 'kmp_timing_graph.png')  # Ruta para guardar el gráfico.
        plt.savefig(graph_path)  # Guarda el gráfico en el archivo.
        plt.close()  # Cierra la figura del gráfico.

        # Preparar el contexto para la plantilla.
        context = {
            'text': text,  # El texto original.
            'pattern': pattern,  # El patrón de búsqueda.
            'positions': positions,  # Las posiciones del patrón en el texto.
            'count': count,  # Número de coincidencias encontradas.
            'duration_10': duration_10,  # Duración para 10 repeticiones.
            'duration_100': duration_100,  # Duración para 100 repeticiones.
            'duration_500': duration_500,  # Duración para 500 repeticiones.
            'duration_1000': duration_1000,  # Duración para 1000 repeticiones.
            'graph_url': '/static/proyecto_7_app/kmp_timing_graph.png',  # URL del gráfico generado.
        }

    return render(request, 'algoritmo.html', context)  # Renderiza la plantilla con el contexto.


def compute_prefix_array(pattern):# Esta función preprocesa el patrón para construir la tabla de prefijos necesaria para el algoritmo KMP.

    m = len(pattern)  # Longitud del patrón.
    prefix_array = [0] * m  # Inicializa la tabla de prefijos con ceros.
    j = 0  # Longitud del prefijo más largo que también es sufijo.

    for i in range(1, m):  # Recorre el patrón desde el segundo carácter.
        while (j > 0 and pattern[i] != pattern[j]):  # Si hay un desajuste, retrocede en el patrón.
            j = prefix_array[j - 1]  # Usa la tabla de prefijos para encontrar el nuevo j.

        if pattern[i] == pattern[j]:  # Si los caracteres coinciden, avanza en el patrón.
            j += 1  # Incrementa j para la siguiente posición.

        prefix_array[i] = j  # Asigna la longitud del prefijo más largo al índice i.

    return prefix_array  # Devuelve la tabla de prefijos.
  

def kmp_search(text, pattern): #Esta función realiza la búsqueda del patrón en el texto utilizando la tabla de prefijos.
    n = len(text)  # Longitud del texto.
    m = len(pattern)  # Longitud del patrón.
    prefix_array = compute_prefix_array(pattern)  # Calcula la tabla de prefijos para el patrón.
    result = []  # Lista para almacenar las posiciones donde se encuentra el patrón.
    j = 0  # Índice para el patrón.

    for i in range(n):  # Recorre el texto.
        while (j > 0 and text[i] != pattern[j]):  # Si hay un desajuste, retrocede en el patrón usando la tabla de prefijos.
            j = prefix_array[j - 1]  # Usa la tabla de prefijos para determinar el nuevo j.

        if text[i] == pattern[j]:  # Si los caracteres coinciden, avanza en el patrón.
            j += 1  # Incrementa j para la siguiente posición del patrón.

        if j == m:  # Si se encontró una coincidencia completa.
            result.append(i - m + 1)  # Almacena la posición de inicio de la coincidencia.
            j = prefix_array[j - 1]  # Reinicia j usando la tabla de prefijos para buscar más coincidencias.

    return result  # Devuelve la lista de posiciones donde se encuentra el patrón.
def home(request):
    return render(request,"home.html")




