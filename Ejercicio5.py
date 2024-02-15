#Descomposición de Dirección IP
#Crea un script que tome una dirección IP como argumento y la descomponga en sus cuatro octetos, mostrándolos línea a línea.

def descomponer_ip(ip):
    # Dividir la IP por los puntos para obtener los octetos
    octetos = ip.split('.')
    
    # Verificar que la IP tenga exactamente 4 octetos
    if len(octetos) != 4:
        print("La IP no es válida: debe contener exactamente 4 octetos.")
        return

    # Verificar que cada octeto sea un número entero entre 0 y 255
    for octeto in octetos:
        if not octeto.isdigit() or not 0 <= int(octeto) <= 255:
            print("La IP no es válida: los octetos deben ser números enteros entre 0 y 255.")
            return

    # Si todas las comprobaciones son correctas, imprimir los octetos
    print("La IP es válida. Octetos:")
    for octeto in octetos:
        print(octeto)

# Ejemplo de uso
ip = "192.168.1.1"
descomponer_ip(ip)