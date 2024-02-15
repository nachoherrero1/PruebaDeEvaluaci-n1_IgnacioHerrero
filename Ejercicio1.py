#Extracción de Información de una Receta
#Al extraer texto de un sitio web de recetas, obtuviste una cadena de texto corrupta y al revés. Parece contener el nombre de una receta y la cantidad de calorías. Formatea la cadena para conseguir una estructura como la siguiente:
#La receta de [Nombre de la receta] contiene [Número] calorías. 

def formatear_receta(cadena_corrupta):
    # Invertir la cadena completa para corregir el orden
    cadena_corregida = cadena_corrupta[::-1]

    # Encontrar el índice del primer espacio para separar las calorías del nombre de la receta
    indice_espacio = cadena_corregida.find(' ')
    
    # Las calorías están al inicio de la cadena corregida, seguido por el nombre de la receta
    calorias = cadena_corregida[:indice_espacio]
    nombre_receta = cadena_corregida[indice_espacio + 1:]

    # Formatear la cadena resultante correctamente
    cadena_formateada = f"La receta de {nombre_receta} contiene {calorias} calorías."

    return cadena_formateada

# Solicitar datos al usuario
cadena_corrupta = input("Ingrese la cadena corrupta: ")

# Formatear la receta
cadena_formateada = formatear_receta(cadena_corrupta)

# Mostrar el resultado
print(cadena_formateada)
