#Priorización de Tareas en un Videojuego
#Durante la planificación de un videojuego, se han acordado una serie de misiones con niveles de dificultad. Crea una estructura de cola con todas las misiones ordenadas por dificultad pero sin mostrar los números de dificultad.

from queue import PriorityQueue

def organizar_misiones(misiones):
    cola_prioridad = PriorityQueue()
    for dificultad, mision in misiones:
        cola_prioridad.put((dificultad, mision))
    
    misiones_ordenadas = []
    while not cola_prioridad.empty():
        misiones_ordenadas.append(cola_prioridad.get()[1])
    return misiones_ordenadas

# Ejemplo de uso
misiones = [(3, "Misión 1"), (1, "Misión 2"), (2, "Misión 3")]
print(organizar_misiones(misiones))