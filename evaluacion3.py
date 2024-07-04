##codigo
import csv


lista_reserva = []




##Aqui estan las funciones...
def reservar_habitacion(num_hab, nombre, apellido , rut, fecha_ent, fecha_sal):
    lista_reserva.append([num_hab, nombre, apellido, rut, fecha_ent, fecha_sal])
    return print(lista_reserva)

def buscar_habitacion(num_hab):
    lista_reserva(num_hab)
    if num_hab == False:
        print("La habitacion no está ocupada.")
    return lista_reserva()

def ver_estado():
    for elemento in lista_reserva:
        print(elemento)
    return lista_reserva

##Aqui esta el codigo

print("Bienvenido, seleccione una opcion: \n")

while True:
    try:
        opcion = int(input("1-. Reservar\n 2.- Buscar\n 3.- Estado\n 4.- Ventas diarias\n 5.- Guardar la informacion\n"))
        if opcion == 1:
            try:
                num_hab = int(input("Ingrese el numero de habitacion: "))
            except ValueError:
                print("Ingrese valores numericos")
            nombre = input("Ingresa el nombre de quien reserva: ")
            apellido = input("Ingresa el apellido: ")
            rut = input("Ingresa el Rut de quien reserva: ")
            fecha_ent = input("Ingresa fecha de entrada (DD-MM-AA): ")
            fecha_sal = input("Ingrese la fecha de salida: ")
            lista_reserva = reservar_habitacion([num_hab, nombre, apellido, rut, fecha_ent, fecha_sal])

        if opcion == 2:
            try:
                piso_hab = int(input("Ingrese el numero de piso seguido del numero de habitacion (piso 3, habitacion 4 = 34)"))
            except ValueError:
                print("Ingrese solo valores numericos.")
            lista_reserva = buscar_habitacion(num_hab)

        if opcion == 3:
            print("Se mostraran las habitaciones")
            
       
        elif opcion == 6:
            print("Ha elegido salir del programa. Adios :(")
            break

    except ValueError:
        print("Ingrese un valor numerico")


