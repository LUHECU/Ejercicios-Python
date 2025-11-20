import acceso_archivos

def agregar_sueno():
    nombre_archivo = 'sueno.txt'
    cantidad_horas = ""

    nombre = input("Ingrese el nombre de la persona: ")
    existe = acceso_archivos.validar_nombre(nombre_archivo, nombre)

    if existe: 
        print(f"Esta persona ya se encuentra registrada en {nombre_archivo}")
        print("Si desea modificar su información, utilice la opción de 'Editar registro existente'.")
        return

    while True:
        try:
            cantidad_horas = int(input("Ingrese la cantidad de horas de sueño :"))
            break
        except:
            print(f"{cantidad_horas} no es una cantidad de horas. Ingrese una cantidad de horas correcta: ")

    lista_datos = [nombre, cantidad_horas]

    if cantidad_horas < 0 or cantidad_horas > 12:
        print("Valor fuera del rango aceptado")
        return

    acceso_archivos.guardar_datos(lista_datos, nombre_archivo)

    if cantidad_horas < 7:
        print("Alerta: Dormir menos de 7 horas puede afectar su bienestar.")

def editar_sueno():
    nombre_archivo = 'sueno.txt'
    cantidad_horas = ""
    nombre = input("Ingrese el nombre de la persona: ")
    existe = acceso_archivos.validar_nombre(nombre_archivo, nombre)

    if not existe:
        print(f"No se encontró ninguna persona con el nombre {nombre}.")
        return
    
    while True:
        try:
            cantidad_horas = int(input("Ingrese la cantidad de horas de sueño :"))
            break
        except:
            print(f"{cantidad_horas} no es una cantidad de horas. Ingrese una cantidad de horas correcta: ")

    lista_datos = nombre, cantidad_horas

    if cantidad_horas < 0 or cantidad_horas > 12:
        print("Valor fuera del rango aceptado")
        return
    
    acceso_archivos.editar_datos(lista_datos, nombre_archivo)

    if cantidad_horas < 7:
        print("Alerta: Dormir menos de 7 horas puede afectar su bienestar.")

def mostrar_datos():
    nombre_archivo = 'sueno.txt'

    lista_datos = acceso_archivos.obtener_datos(nombre_archivo)

    if not lista_datos or len(lista_datos) == 0:
        return

    print("\n--- Horas de sueño ---")
    for dato in lista_datos:
        print(f"{dato[0]}: {dato[1]}")


def obtener_nombres():
    nombre_archivo = 'sueno.txt'

    lista_datos = acceso_archivos.obtener_datos(nombre_archivo)
    nombres = []

    for dato in lista_datos:
        nombre = dato[0]
        nombres.append(nombre)
        
    return nombres

def obtener_horas_sueno():
    nombre_archivo = 'sueno.txt'

    lista_datos = acceso_archivos.obtener_datos(nombre_archivo)
    horas = []

    for dato in lista_datos:
        hora = dato[1]
        horas.append(int(hora))
        
    return horas
