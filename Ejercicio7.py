#Añadir Ítems a un Inventario
#Crea una función llamada agregar_item(inventario, item) que reciba una lista de ítems de un inventario y un nuevo ítem a añadir. La función debe añadir el nuevo ítem siempre y cuando no se repita. Si el ítem ya está en el inventario, debe lanzar un error de tipo ValueError.

def agregar_item(inventario, item):
    if item in inventario:
        raise ValueError("El ítem ya está en el inventario.")
    inventario.append(item)
    return inventario

# Ejemplo de uso
inventario = ["espada", "escudo", "poción"]
try:
    agregar_item(inventario, "arco")
    print(inventario)
    agregar_item(inventario, "espada")
except ValueError as e:
    print(e)