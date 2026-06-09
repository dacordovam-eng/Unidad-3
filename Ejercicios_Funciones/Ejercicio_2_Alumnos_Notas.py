'''alumnos = {
"Ana": [5.5, 6.0, 4.8],
"Luis": [3.9, 4.1, 5.0],
"Pedro": [6.5, 6.8, 7.0]
}'''
import statistics

alumnos = {}

def agregar_alumno(alumnos):
    print("Agregando nuevo alumno")
    Nombre_alumno = input("Agrege nombre de alumno: ").strip().title()
    if Nombre_alumno == "":
        print("Nombre vacio, ingrese nombre correcto")
        return
    if Nombre_alumno.replace(" ", "").isdigit():
        print("Error! El nombre no puede ser solo numeros")
        return
    if Nombre_alumno in alumnos:
        print("Alumno ya existe! Intente de nuevo")
        return

    while True:
        try:
            Cantidad_notas = int(input("Ingrese cantidad de notas a agregar: "))
            break
        except ValueError:
            print("Ingrese numero entero valido")
    
    Notas = []
    for i in range(Cantidad_notas):
        while True:
            try:
                while True:
                    Nota_alumno = float(input(f"Ingrese nota a registrar {i+1}/{Cantidad_notas}: "))
                    if Nota_alumno > 7.0 or Nota_alumno < 1.0 
                Notas.append(Nota_alumno)
                break
            except ValueError:
                print("Ingrese solo numeros para notas")
        
    alumnos[Nombre_alumno] = Notas

    print(f"El registro se ha agregado exitosamente: {Nombre_alumno} - Notas: {Notas}")

def mostrar_alumnos(alumnos):
    if not alumnos:
        print("No existen registros, agrege alumnos y notas")
        return
    for Nombre_alumno, Notas in alumnos.items():
        print(f"Nombre: {Nombre_alumno} | Notas: {Notas}")

def ver_promedios(alumnos):
    for Nombre_alumno, Notas in alumnos.items():
        promedio = statistics.mean(Notas)
        print(f"Alumno: {Nombre_alumno} | Promedo: {round(promedio, 2)}")

def mejor_alumno(alumnos):
    for Nombre_alumno, promedio in alumnos.items():
        if promedio > promedio:
            Mejor_alumno = statistics.mean(promedio)
            print(f"El Alumno: {Nombre_alumno} | Es el mejor Promedo con: {round(Mejor_alumno, 2)}")


while True:
    print('''
    ======== MENU =========
    1. Agregar alumno
    2. Mostrar alumnos
    3. Ver promedios
    4. Mejor alumno
    5. Cantidad de aprobados
    6. Salir
    ========================

    ''')

    while True:
        try:
            Opcion = int(input("\nSeleccione su opcion segun Menú: "))
            if 1 <= Opcion <= 6:
                break
            print("\n\u274CIngrese una opcion valida en el menu")
        except ValueError:
            print("\nIngrese un numero valido del menu") 

    if Opcion == 1:
        agregar_alumno(alumnos)
    elif Opcion == 2:
        mostrar_alumnos(alumnos)
    elif Opcion == 3:
        print("")
    elif Opcion == 4:
        print("")
    elif Opcion == 5:
        print("")
    elif Opcion == 6:
        print("Saliendo del sistema...")
        break
    else:
        print("Seleccione una opcion valida en el Menú")


