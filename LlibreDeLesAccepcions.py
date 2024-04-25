import time,os
diccionari = {}
def cls():#Limpiamos la pantalla
    os.system('cls' if os.name=='nt' else 'clear')
def pedirNumero(mensaje, NUMIN, NUMAX): #Funcion para pedir un numero
    while True:
        try:
            num = int(input(mensaje))
            if num >= NUMIN and num <= NUMAX:
                break
            else:
                print(f"No existe esa opcion solo existen de la opcion {NUMIN} hasta la {NUMAX}")
        except ValueError:
            print("Has de dar un numero valido")
    return num
#!Funciones Opciones
def afegir(): #Añadir al diccionario
    paraula = input("Dona la paraula a afegir: ")
    entrada = input("Dona la definició de la paraula: ")
    diccionari[paraula] = entrada
    print("Paraula afegida correctament!\n")
    input("Pulsa una tecla per continuar...")

def llistar(): #Listar opciones del diccionario
    if diccionari != {}:
        for paraula in diccionari:
            print(f"{paraula}: {diccionari[paraula]}")
    else:
        print("No hi ha cap paraula afegida")
    input("Pulsa una tecla per continuar...")

def modificar(): #Modificar palabras del diccionario
    paraules = [paraula for paraula in diccionari]
    if len(paraules) == 0:
        print("No hi ha cap paraula per modificar")
        input("Pulsa una tecla per continuar...")
    else:
        print(f"Les paraules que pots modificar son: {', '.join(paraules)}")
        paraula = input("Dona la paraula a modificar: ")
        if paraula in diccionari:
            entrada = input("Dona la nova definició de la paraula: ")
            diccionari[paraula] = entrada
            print("Paraula modificada correctament!\n")
            input("Pulsa una tecla per continuar...")
        else:
            print("Aquesta paraula no existeix")
            input("Pulsa una tecla per continuar...")


def esborrar(): # Eliminar palabra del Diccionario
    if diccionari:
        print("Les paraules que hi ha son:", ", ".join(diccionari))
        paraula = input("Dona la paraula a esborrar: ")
        if paraula in diccionari:
            del diccionari[paraula]
            print("Paraula esborrada correctament!\n")
            input("Pulsa una tecla per continuar...")
        else:
            print("Aquesta paraula no existeix. Les paraules que hi ha son:", ", ".join(diccionari))
            input("Pulsa una tecla per continuar...")
    else:
        print("No hi ha cap paraula per esborrar")
        input("Pulsa una tecla per continuar...")

def sortir(): # Salir del Codigo
    print("Hasta la próxima!")
    exit()

#!CODIGO
while True: #Bucle Preguntar
    cls()
    print ("-"*30)
    print ("   Llibre de les Accepcions")
    print ("       Creat per Sergi")
    print ("-"*30)
    print ("1) Afegir")
    print ("2) Llistar")
    print ("3) Modificar")
    print ("4) Esborrar")
    print ("5) Sortir\n")
    numero = pedirNumero("Selecciona una opcion: ", 1, 5) #Pedir Accion

    if numero == 1: # Que hacer segun la accion seleccionada
        afegir()
    elif numero == 2:
        llistar()
    elif numero == 3:
        modificar()
    elif numero == 4:
        esborrar()
    elif numero == 5:
        sortir()