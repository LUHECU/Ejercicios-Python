import acceso_archivos

def agregar_ejercicio():
    nombre_archivo = 'ejercicio.txt'
    cantidad_minutos = ""

    nombre = input("Ingrese el nombre de la persona: ")
    existe_nombre = acceso_archivos.validar_nombre(nombre_archivo, nombre)

    if existe_nombre:
        print(f"Esta persona ya se encuentra registrada en {nombre_archivo}")
        print("Si desea modificar su información, utilice la opción de 'Editar registro existe_nombrente'.")
        return

    while True:
        try:
            cantidad_minutos = int(input("Ingrese la cantidad de minutos de ejercicios :"))
            break
        except ValueError:
            print(f"{cantidad_minutos} no es una cantidad de minutos. Ingrese una cantidad_minutos de minutos correcta: ")

    lista_datos = [nombre, cantidad_minutos]
    
    if cantidad_minutos < 0 or cantidad_minutos > 180:
        print("Valor fuera del rango aceptado")
        return

    acceso_archivos.guardar_datos(lista_datos, nombre_archivo)

    if cantidad_minutos < 30:
        print("Alerta: Poca actividad física. Intente al menos 30 minutos diarios.")


def editar_ejercicio():
    nombre_archivo = 'ejercicio.txt'
    existen_datos = acceso_archivos.obtener_datos(nombre_archivo)

    if not existen_datos or len(existen_datos) == 0:
        print(f"\nNo hay datos registrados.")
        return

    cantidad_minutos = ""
    nombre = input("Ingrese el nombre de la persona: ")
    existe_nombre = acceso_archivos.validar_nombre(nombre_archivo, nombre)

    if not existe_nombre:
        print(f"No se encontró ninguna persona con el nombre {nombre}.")
        return
    
    while True:
        try:
            cantidad_minutos = int(input("Ingrese la cantidad de minutos de ejercicios :"))
            break
        except ValueError:
            print(f"{cantidad_minutos} no es una cantidad de minutos. Ingrese una cantidad_minutos de minutos correcta: ")

    lista_datos = nombre, cantidad_minutos

    if cantidad_minutos < 0 or cantidad_minutos > 180:
        print("Valor fuera del rango aceptado")
        return
    
    acceso_archivos.editar_datos(lista_datos, nombre_archivo)

    if cantidad_minutos < 30:
        print("Alerta: Poca actividad física. Intente al menos 30 minutos diarios.")


def mostrar_datos():
    nombre_archivo = 'ejercicio.txt'

    lista_datos = acceso_archivos.obtener_datos(nombre_archivo)

    if not lista_datos or len(lista_datos) == 0:
        return

    print("\n--- Minutos de ejercicio ---")
    for dato in lista_datos:
        print(f"{dato[0]}: {dato[1]}")

def obtener_nombres():
    nombre_archivo = 'ejercicio.txt'

    lista_datos = acceso_archivos.obtener_datos(nombre_archivo)
    nombres = []

    for dato in lista_datos:
        nombre = dato[0]
        nombres.append(nombre)
        
    return nombres
