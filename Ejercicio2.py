# Cálculo de Interés Compuesto
# Crea un programa que calcule el interés compuesto.
# Guarda en una variable capital_inicial el valor 1000.
# Lee por pantalla la tasa de interés anual, que deberá estar entre 1% y 10%.
# Eleva la tasa de interés a sí misma por el número de años (por ejemplo, 5 años).
# Multiplica el capital_inicial por el resultado anterior en sí mismo.
# Muestra el capital final.

def calcular_interes_compuesto():
    capital_inicial = 1000
    
    # Solicitar la tasa de interés
    while True:
        tasa_interes = float(input("Introduce la tasa de interés anual (entre 1% y 10%): "))
        if 1 <= tasa_interes <= 10:
            break
        else:
            print("La tasa de interés debe estar entre 1% y 10%. Intenta de nuevo.")
    
    # Solicitar el número de años
    años = int(input("Introduce el número de años: "))
    
    # Convertir la tasa de interés a decimal
    tasa_interes /= 100
    
    # Calcular el capital final
    capital_final = capital_inicial * (1 + tasa_interes) ** años
    
    print(f"El capital final después de {años} años es: {capital_final:.2f}")

calcular_interes_compuesto()