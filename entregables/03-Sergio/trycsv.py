#%%
import pandas as pd
import time
inicio = time.time()
df = pd.read_csv('data.csv')


df = pd.DataFrame(df)

título = "Superman"

resultado = df[df['title'] == título]

print(resultado)
final = time.time()
tiempo_busqueda = final-inicio
print(tiempo_busqueda)
#Anque la búsqueda es más rápido en el archivo con el hash map, usando la biblioteca de pandas, 
# no tenemos que esperar a que el hashmap se forme ni debemos escribir tanto código, además podemos buscar varias películas con el mismo título.
#Al buscar un título nos proporciona todas las películas que tienen este título y no solo la primera que encuentra, por tanto,
# si quisieramos hacer que la hash table fuera competitiva deberíamos hacer aún más mejoras.
