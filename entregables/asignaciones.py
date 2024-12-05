import json
import os

# Archivo JSON para almacenar las asignaciones
archivo_asignaciones = 'asignaciones.json'

# Diccionario para almacenar las asignaciones
asignaciones = {}

def asignar_ejercicio(alumno, ejercicio):
    if alumno not in asignaciones:
        asignaciones[alumno] = []
    if len(asignaciones[alumno]) < 3 and ejercicio not in asignaciones[alumno]:
        asignaciones[alumno].append(ejercicio)
        print(f"Ejercicio {ejercicio} asignado a {alumno}.")
    elif len(asignaciones[alumno]) >= 3:
        print(f"{alumno} ya tiene 3 ejercicios asignados.")
    else:
        print(f"Ejercicio {ejercicio} ya está asignado a {alumno}.")
    guardar_asignaciones()

def desistir_ejercicio(alumno, ejercicio):
    if alumno in asignaciones and ejercicio in asignaciones[alumno]:
        asignaciones[alumno].remove(ejercicio)
        print(f"{alumno} ha desistido del ejercicio {ejercicio}.")
    else:
        print(f"{alumno} no tiene asignado el ejercicio {ejercicio}.")
    guardar_asignaciones()

def mostrar_asignaciones():
    print("\nAsignaciones actuales:")
    for alumno, ejercicios in asignaciones.items():
        print(f"{alumno}: {', '.join(map(str, ejercicios))}")

def calcular_ejercicios():
    ejercicios_alumnos = {}
    for alumno, ejercicios in asignaciones.items():
        for ejercicio in ejercicios:
            if ejercicio not in ejercicios_alumnos:
                ejercicios_alumnos[ejercicio] = []
            ejercicios_alumnos[ejercicio].append(alumno)
    print("\nEjercicios y alumnos asignados:")
    for ejercicio, alumnos in ejercicios_alumnos.items():
        print(f"Ejercicio {ejercicio}: {', '.join(alumnos)}")

def guardar_asignaciones():
    with open(archivo_asignaciones, 'w') as f:
        json.dump(asignaciones, f)

def cargar_asignaciones():
    global asignaciones
    if os.path.exists(archivo_asignaciones):
        with open(archivo_asignaciones, 'r') as f:
            asignaciones = json.load(f)

def mostrar_asignaciones_finales():
    ejercicios_alumnos = {}
    
    # Recopilación de todas las asignaciones
    for alumno, ejercicios in asignaciones.items():
        for ejercicio in ejercicios:
            if ejercicio not in ejercicios_alumnos:
                ejercicios_alumnos[ejercicio] = []
            ejercicios_alumnos[ejercicio].append(alumno)

    # Resolución de conflictos: un solo alumno por ejercicio
    asignados_finales = {}
    for ejercicio, alumnos in ejercicios_alumnos.items():
        if alumnos:  # Si hay alumnos en la lista
            asignados_finales[ejercicio] = alumnos[0]  # Asignar el primer alumno de la lista

    print("\nAsignaciones finales (un solo alumno por ejercicio):")
    for ejercicio, alumno in sorted(asignados_finales.items()):
        print(f"Ejercicio {ejercicio}: {alumno}")

if __name__ == '__main__':

    # Cargar las asignaciones al inicio del programa
    cargar_asignaciones()

    # Ejemplos de uso
    # asignar_ejercicio("Juan", 1)
    # asignar_ejercicio("Juan", 2)
    # asignar_ejercicio("Juan", 3)
    # asignar_ejercicio("Juan", 4)  # No debería asignar porque ya tiene 3
    # asignar_ejercicio("Maria", 1)
    # asignar_ejercicio("Maria", 2)
    # desistir_ejercicio("Maria", 1)
    # asignar_ejercicio("Maria", 3)
    # asignar_ejercicio("Pepe", 3)

    asignar_ejercicio("Erik", 7)
    asignar_ejercicio("Erik", 4)
    asignar_ejercicio("Erik", 1)
    asignar_ejercicio("Cristian", 16)
    asignar_ejercicio("Sergio", 1)
    asignar_ejercicio("Sergio", 3)
    asignar_ejercicio("Cristian", 4)
    asignar_ejercicio("Irene", 14)
    asignar_ejercicio("Irene", 18)
    asignar_ejercicio("J", 5)
    asignar_ejercicio("Gerard", 9)
    asignar_ejercicio("Gerard", 13)
    asignar_ejercicio("Fran", 10)
    asignar_ejercicio("Solomon", 1)
    asignar_ejercicio("Solomon", 2)
    asignar_ejercicio("Marina", 6)
    asignar_ejercicio("Marina", 11)
    asignar_ejercicio("Adan", 6)
    asignar_ejercicio("Adan", 13)
    asignar_ejercicio("Adan", 9)
    asignar_ejercicio("Alejandro", 15)
    asignar_ejercicio("Alejandro", 20)
    desistir_ejercicio("Sergio", 1)
    asignar_ejercicio("Josep", 7)
    asignar_ejercicio("Josep", 9)
    asignar_ejercicio("Josep", 14)
    desistir_ejercicio("Marina", 6)
    asignar_ejercicio("Josias", 12)
    asignar_ejercicio("Glenn", 17)
    desistir_ejercicio("Irene", 18)
    desistir_ejercicio("Erik", 1)
    desistir_ejercicio("Erik", 4)
    desistir_ejercicio("Alejandro", 20)
    desistir_ejercicio("Solomon", 2)
    desistir_ejercicio("Gerard", 13)
    desistir_ejercicio("Josep", 14)
    asignar_ejercicio("Josep", 2)
    asignar_ejercicio("Yago", 18)
    desistir_ejercicio("Cristian", 4)

    mostrar_asignaciones()
    calcular_ejercicios()
    mostrar_asignaciones_finales()
