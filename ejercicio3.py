# Ejercicio 3: Agenda de Contactos con Diccionario
#creamos un diccionario vacio paa que el usuario agregue contactos
agenda_contactos = {}
#funcion 1: agregar contacto
#la funcion crea la entrada, si maria ya existe, se actualiza el numero de telefono
def agregar_contacto(nombre, telefono):
    """Agrega un contacto a la agenda."""
    agenda_contactos[nombre] = telefono  #crea la entrada
    print(f"Contacto '{nombre}' guardado.")



#funcion 2: buscar contacto
def buscar_contacto(nombre):
    if nombre in agenda_contactos:   #in verifica si el nombre existe en el diccionario
        print(f"El teléfono de '{nombre}' es: {agenda_contactos[nombre]}")
    else: 
        print(f"'{nombre}' no está en la agenda.")

#funcion 3: mostrar todos los contactos
def mostrar_contactos():
    if len(agenda_contactos) == 0:
        print("La agenda está vacía.")
    else:
        print("\n-----Todos los Contactos-----")
        for nombre, telefono in agenda_contactos.items(): # recorre los pares clave, valor
            print(f"{nombre}: {telefono}")  # el bucle for los muestra en dos variables nombre y telefono, para poder usar ambos.
# ----------PROGRAMA PRINCIPAL----------
while True:
    print("\n======AGENDA DE CONTACTOS======")
    print("1. Agregar Contacto")
    print("2. Buscar Contacto")
    print("3. Mostrar Todos los Contactos")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")
    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Telefono: ")
        agregar_contacto(nombre, telefono)
    elif opcion == "2":
        nombre = input("Nombre del contacto a buscar: ")
        buscar_contacto(nombre)
    elif opcion == "3":
        mostrar_contactos()
    elif opcion == "4":
        print("Saliste de la agenda. ¡Hasta luego!")
        break
    else: 
        print("Esta opcion no es valida.")



