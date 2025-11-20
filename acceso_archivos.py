def guardar_datos(lista_datos, nombre_archivo):
    datos = obtener_datos(nombre_archivo)
    modo = 'w'
    nombre, cantidad_tiempo = lista_datos

    if datos:
        modo = 'a'

    with open(nombre_archivo, modo) as archivo:
        archivo.write(f'{nombre}, {cantidad_tiempo}\n')

    print("\nRegistro guardado correctamente")

def editar_datos(lista_datos, nombre_archivo):
    datos = obtener_datos(nombre_archivo)
    nombre_editado, cantidad_tiempo_editada = lista_datos

    with open(nombre_archivo, 'w') as archivo:
        for dato in datos:
            nombre, cantidad_tiempo = dato
            if nombre == nombre_editado:
                archivo.write(f'{nombre}, {cantidad_tiempo_editada}\n')
            else:
                archivo.write(f'{nombre}, {cantidad_tiempo}\n')

    print("\nRegistro editado correctamente")

def obtener_datos(nombre_archivo):
    lista_datos = []
    try:
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                lista_datos.append(linea.strip().split(','))
        return lista_datos
    except FileNotFoundError:
        return

def validar_nombre(nombre_archivo, nombre):
    lista_datos = obtener_datos(nombre_archivo)

    for dato in lista_datos:
        if nombre == dato[0]:
            return True
    
    return False
