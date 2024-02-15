#Encontrar Palabras Comunes
#Dadas dos listas de palabras, genera una tercera lista con todas las palabras que se repitan en ambas listas, sin repetición en la nueva lista.

def encontrar_palabras_comunes(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    palabras_comunes = list(set1.intersection(set2))
    return palabras_comunes

lista1 = ["manzana", "zanahoria", "banana", "pizza", "cereza"]
lista2 = ["banana", "kiwi", "queso", "pizza", "cereza"]
print(encontrar_palabras_comunes(lista1, lista2))