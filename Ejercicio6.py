#Separar Personajes de Videojuegos
#Crea una función que tome una lista de personajes de videojuegos y devuelva dos listas ordenadas: la primera con personajes humanos y la segunda con personajes no humanos.

def separar_y_ordenar_personajes(personajes):
    # Filtrar personajes humanos y no humanos, luego ordenar cada lista
    humanos = sorted([personaje for personaje in personajes if personaje['tipo'] == 'humano'], key=lambda x: x['nombre'])
    no_humanos = sorted([personaje for personaje in personajes if personaje['tipo'] != 'humano'], key=lambda x: x['nombre'])

    return humanos, no_humanos

# Ejemplo de uso
personajes = [
    {"nombre": "Link", "tipo": "humano"},
    {"nombre": "Mario", "tipo": "humano"},
    {"nombre": "Samus", "tipo": "humano"},
    {"nombre": "Pikachu", "tipo": "no humano"},
    {"nombre": "Kirby", "tipo": "no humano"}
]

humanos, no_humanos = separar_y_ordenar_personajes(personajes)
print("Personajes Humanos:", humanos)
print("Personajes No Humanos:", no_humanos)