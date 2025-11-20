import acceso_archivos

def alertas_recomendaciones(cantidad_horas_pantalla):
    if cantidad_horas_pantalla > 6:
        print("Alerta: Uso excesivo de pantallas. Se recomienda limitar el tiempo digital y descansar la vista.")
    if cantidad_horas_pantalla >= 0 and cantidad_horas_pantalla <= 3 :
        print("Recomendación: Se sugiere dormir al menos 7 o 8 horas para compensar el esfuerzo visual y mental.")
    elif cantidad_horas_pantalla >= 4 and cantidad_horas_pantalla <= 6 :
        print("Recomendación: Se sugiere dormir al menos 8 o 9 horas para compensar el esfuerzo visual y mental.")
    elif cantidad_horas_pantalla >= 7 and cantidad_horas_pantalla <= 9 :
        print("Recomendación: Se sugiere dormir al menos 9 horas o más para compensar el esfuerzo visual y mental.")
    elif cantidad_horas_pantalla <= 10 :
        print("Recomendación: Se recomienda descanso digital y pausas activas.")

def agregar_pantalla():
    nombre_archivo = 'pantallas.txt'
    cantidad_horas_pantalla = ""

    nombre = input("Ingrese el nombre de la persona: ")
    existe_nombre = acceso_archivos.validar_nombre(nombre_archivo, nombre)

    if existe_nombre:
        print(f"\nEsta persona ya se encuentra registrada en {nombre_archivo}")
        print("Si desea modificar su información, utilice la opción de 'Editar registro existe_nombrente'.")
        return

    while True:
        try:
            cantidad_horas_pantalla = int(input("Ingrese la cantidad de horas frente a la pantalla: "))
            break
        except ValueError:
            print(f"{cantidad_horas_pantalla} no es una cantidad de horas. Ingrese una cantidad horas correcta: ")

    lista_datos = [nombre, cantidad_horas_pantalla]

    if cantidad_horas_pantalla < 0 or cantidad_horas_pantalla > 10:
        print("Valor fuera del rango aceptado")
        return

    acceso_archivos.guardar_datos(lista_datos, nombre_archivo)

    alertas_recomendaciones(cantidad_horas_pantalla)


def editar_pantalla():
    nombre_archivo = 'pantallas.txt'
    existen_datos = acceso_archivos.obtener_datos(nombre_archivo)

    if not existen_datos or len(existen_datos) == 0:
        print(f"\nNo hay datos registrados.")
        return

    cantidad_horas_pantalla = ""
    nombre = input("Ingrese el nombre de la persona: ")
    existe_nombre = acceso_archivos.validar_nombre(nombre_archivo, nombre)

    if not existe_nombre:
        print(f"No se encontró ninguna persona con el nombre {nombre}.")
        return
    
    while True:
        try:
            cantidad_horas_pantalla = int(input("Ingrese la cantidad de horas frente a la pantalla: "))
            break
        except ValueError:
            print(f"{cantidad_horas_pantalla} no es una cantidad de horas. Ingrese una cantidad horas correcta: ")

    lista_datos = nombre, cantidad_horas_pantalla

    if cantidad_horas_pantalla < 0 or cantidad_horas_pantalla > 10:
        print("Valor fuera del rango aceptado")
        return
    
    acceso_archivos.editar_datos(lista_datos, nombre_archivo)

    alertas_recomendaciones(cantidad_horas_pantalla)

def mostrar_datos():
    nombre_archivo = 'pantallas.txt'

    lista_datos = acceso_archivos.obtener_datos(nombre_archivo)

    if not lista_datos or len(lista_datos) == 0:
        return

    print("\n--- Horas Frente a Pantallas ---")
    for dato in lista_datos:
        print(f"{dato[0]}: {dato[1]}")

def obtener_nombres():
    nombre_archivo = 'pantallas.txt'

    lista_datos = acceso_archivos.obtener_datos(nombre_archivo)
    nombres = []

    for dato in lista_datos:
        nombre = dato[0]
        nombres.append(nombre)
        
    return nombres

def sueno_suficiente(nombre, cantidad_horas_pantalla):
    nombre_archivo = 'sueno.txt'
    lista_datos = acceso_archivos.obtener_datos(nombre_archivo)

    for dato in lista_datos:
        if nombre == dato[0]:
            cantidad_horas_sueno = int(dato[1])

    if cantidad_horas_pantalla >= 0 and cantidad_horas_pantalla <= 3 and cantidad_horas_sueno < 7 :
        return False
    elif cantidad_horas_pantalla >= 4 and cantidad_horas_pantalla <= 6 and cantidad_horas_sueno < 8:
        return False
    elif cantidad_horas_pantalla >= 7 and cantidad_horas_pantalla <= 9 and cantidad_horas_sueno < 9:
        return False
    elif cantidad_horas_pantalla >= 10 :
        return False
    
    return True

def obtener_cantidad_horas_pantalla(nombre):
    nombre_archivo = 'pantallas.txt'
    lista_datos = acceso_archivos.obtener_datos(nombre_archivo)

    for dato in lista_datos:
        if nombre == dato[0]:
            cantidad_horas_pantalla = dato[1]
    
    return cantidad_horas_pantalla