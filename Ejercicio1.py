#Extracción de Información de una Receta
#Al extraer texto de un sitio web de recetas, obtuviste una cadena de texto corrupta y al revés. Parece contener el nombre de una receta y la cantidad de calorías. Formatea la cadena para conseguir una estructura como la siguiente:
#La receta de [Nombre de la receta] contiene [Número] calorías. 

def formatear_receta(cadena_corrupta):
    # Invertir la cadena
    cadena_corregida = cadena_corrupta[::-1]

    # Dividir la cadena en nombre de la receta y calorías
    partes = cadena_corregida.split(' ', 1)
    nombre_receta = partes[1][::-1]  # Invertir el nombre de la receta
    calorias = partes[0][::-1]  # Invertir las calorías

    # Formatear la cadena resultante
    cadena_formateada = f"La receta de {nombre_receta} contiene {calorias} calorías."

    return cadena_formateada

# Ejemplo de uso
cadena_corrupta = "atellam elehsarfóitnerdnocsezerp eziloaC8210"
cadena_formateada = formatear_receta(cadena_corrupta)
print(cadena_formateada)
