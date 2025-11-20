import pantalla
import ejercicio
import sueno

def calculo_interseccion():
    personas = []

    nombres_pantallas = pantalla.obtener_nombres()
    nombres_ejercicio = ejercicio.obtener_nombres()
    nombres_sueno = sueno.obtener_nombres()

    if not nombres_pantallas:
        print("\nNo hay usuarios equilibrados (presentes en los 3 conjuntos)")
        return

    for nombre in nombres_pantallas:
        if nombre in nombres_ejercicio and nombre in nombres_sueno:
            personas.append(nombre)

    if not personas or len(personas) == 0:
        print("\nNo hay usuarios equilibrados (presentes en los 3 conjuntos)")
        return

    print("\nUsuarios equilibrados (presentes en los 3 conjuntos):")
    for nombre in personas:
        print(nombre)

def calculo_diferencia():
    personas = []

    nombres_pantallas = pantalla.obtener_nombres()
    nombres_ejercicio = ejercicio.obtener_nombres()
    nombres_sueno = sueno.obtener_nombres()

    if not nombres_pantallas:
        print("\nNo hay registros de pantalla")
        return

    for nombre in nombres_pantallas:

        if nombre not in nombres_ejercicio:
            personas.append(nombre)

        if nombre in nombres_ejercicio and nombre not in nombres_sueno:
            personas.append(nombre)

        if nombre in nombres_ejercicio and nombre in nombres_sueno:
            horas_pantalla = int(pantalla.obtener_cantidad_horas(nombre))
            duerme_sufiente = pantalla.sueno_suficiente(nombre, horas_pantalla)
            if not duerme_sufiente:
                personas.append(nombre)

    if not personas or len(personas) == 0:
        print("\nNo hay usuarios con exceso de pantallas (no hacen ejercicio o duermen poco)")
        return

    print("\nUsuarios con exceso de pantallas (no hacen ejercicio o duermen poco):")
    for nombre in personas:
        print(nombre)

def calculo_diferencia_simetrica():
    personas = []
    nombres_pantallas = pantalla.obtener_nombres()
    nombres_ejercicio = ejercicio.obtener_nombres()
    nombres_sueno = sueno.obtener_nombres()

    if not nombres_ejercicio and not nombres_sueno and not nombres_pantallas:
        print("\nNo hay registros de ejercicio, sueño y pantallas")
        return

    if nombres_pantallas:
        for nombre in nombres_pantallas:
            if nombre not in nombres_ejercicio or nombre not in nombres_sueno:
                personas.append(nombre)

    if nombres_ejercicio:
        for nombre in nombres_ejercicio:
            if nombre not in nombres_pantallas or nombre not in nombres_sueno:
                personas.append(nombre)

    if nombres_sueno:
        for nombre in nombres_sueno:
            if nombre not in nombres_ejercicio or nombre not in nombres_pantallas:
                personas.append(nombre)

    if not personas or len(personas) == 0:
        print("\nNo hay usuarios con hábitos irregulares (solo en uno o dos conjutos)")
        return

    print("\nUsuarios con hábitos irregulares (solo en uno o dos conjutos):")
    for nombre in personas:
        print(nombre)

def promedio_recursivo(lista_horas):
    if len(lista_horas) == 0:
        return 0
    
    return (lista_horas[0] + promedio_recursivo(lista_horas[1:]))

def promedio_bienestar():
    horas_sueno = sueno.obtener_horas_sueno()
    if not horas_sueno or len(horas_sueno) == 0 :
        print("\nNo hay datos registrados sobre el sueño para generar el promedio de bienestar")
        return

    suma_hora = promedio_recursivo(horas_sueno)
    promedio_sueno = suma_hora / len(horas_sueno)

    print(f"\nPromedio de sueño (recursivo): {promedio_sueno}")

def reporte():
    print("\nREPORTE DE BIENESTAR DIGITAL")
    print("------------------------------")

    calculo_interseccion()

    calculo_diferencia()

    calculo_diferencia_simetrica()

    promedio_bienestar()



    