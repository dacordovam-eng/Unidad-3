'''alumnos = {
"Ana": [5.5, 6.0, 4.8],
"Luis": [3.9, 4.1, 5.0],
"Pedro": [6.5, 6.8, 7.0]
}'''

def agregar_alumno(alumnos):
    Nombre_alumno = input("Ingrese nombre de alumno: ").strip().capitalize()
    if Nombre_alumno == "":
        print("El nombre de almno no puede estar vacio, intenete nuevamente")
        return
    if Nombre_alumno in alumnos:
        print("Nombre ya existe, intenta agregando segundo nombre o apellido ó alias")
        return

def mostrar_alumnos(alumnos):
    if alumnos is None:
        print("No existen alumnos registrados")
        return
    else:
        print(f"Los alumnos con notas registradas son {[alumnos][0]}")

def ver_promedios(alumnos):

def mejor_alumno(alumnos):

def cantidad_aprobados(alumnos):

alumnos = {}