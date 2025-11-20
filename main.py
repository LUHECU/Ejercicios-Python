import pantalla
import ejercicio
import sueno
import calculos

#Menú para editar datos existentes
def editar_datos_existentes():
    while True:
        print("\n============================")
        print("¿Qué desea editar?")
        print("============================")
        print("1. Horas de pantalla")
        print("2. Minutos de ejercicio")
        print("3. Horas de sueño")
        print("4. Regresar")
        print("----------------------------")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            pantalla.editar_pantalla()
            break
        elif opcion == '2':
            ejercicio.editar_ejercicio()
            break
        elif opcion == '3':
            sueno.editar_sueno()
            break
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

#Menú para registrar datos nuevos
def registrar_datos_nuevos():
    while True:
        print("\n============================")
        print("¿Qué desea registrar?")
        print("============================")
        print("1. Horas de pantalla")
        print("2. Minutos de ejercicio")
        print("3. Horas de sueño")
        print("4. Regresar")
        print("----------------------------")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            pantalla.agregar_pantalla()
            break
        elif opcion == '2':
            ejercicio.agregar_ejercicio()
            break
        elif opcion == '3':
            sueno.agregar_sueno()
            break
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

#Menú general
def main():
    while True:
        print("\n============================")
        print("Menú:")
        print("============================")
        print("1. Agregar nuevo registro")
        print("2. Editar un registro existente")
        print("3. Ver datos de un archivo")
        print("4. Analizar bienestar (instersecciones y diferencias)")
        print("5. Calcular promedio recursivo")
        print("6. Generar reporte de resultados")
        print("7. Salir")
        print("----------------------------")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_datos_nuevos()
        elif opcion == '2':
            editar_datos_existentes()
        elif opcion == '3':
            pantalla.mostrar_datos()
            ejercicio.mostrar_datos()
            sueno.mostrar_datos()
        elif opcion == '4':
            calculos.calculo_interseccion()
            calculos.calculo_diferencia()
        elif opcion == '5':
            calculos.promedio_bienestar()
        elif opcion == '6':
            calculos.reporte()
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
