'''alumnos = {
"Ana": [5.5, 6.0, 4.8],
"Luis": [3.9, 4.1, 5.0],
"Pedro": [6.5, 6.8, 7.0]
}'''

alumnos = {}

def agregar_alumno(alumnos):
    print("Agregando nuevo alumno")
    Nombre_alumno = input("Agrege nombre de alumno: ").strip()
    if Nombre_alumno == "":
        print("Nombre vacio, ingrese nombre correcto")
        return
    if Nombre_alumno.isdigit():
        print("Error! El nombre no puede ser solo numeros")
        return
    if Nombre_alumno in alumnos:
        print("Alumno ya existe! Intente de nuevo") 
    
    Cantidad_notas = int(input("Ingrese cantidad de notas a agregar: "))
    
    Notas = []
    for i in range(Cantidad_notas):
        Nota_alumno = float(input(f"Ingrese nota a registrar {i+1}/{Cantidad_notas}: "))
        Notas.append(Nota_alumno)
        
    alumnos[Nombre_alumno] = Notas
    print(f"El registro se ha agregado exitosamente: {Nombre_alumno} - Notas: {Notas}")

    
        
        
     




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


    Opcion = int(input("Seleccione su opcion segun Menú: "))

    if Opcion == 1:
         agregar_alumno(alumnos)
    elif Opcion == 2:
        print("")
    elif Opcion == 3:
        print("")
    elif Opcion == 4:
        print("")
    elif Opcion == 5:
        print("")
    elif Opcion == 6:
        print("")
    else:
        print("Seleccione una opcion valida en el Menú")


