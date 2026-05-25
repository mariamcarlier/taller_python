# Ejercicio 2: Lista de Compras Interactiva 
print("Bienvenido a tu lista de compras interactiva!")

# 1. Crear una lista vacia con [] donde se giararan los items de que el usuario agreggue
lista_compras = []
# 2. creamos el bucle infinito while que mantiene el menu activo
while True:
    print("\nLISTA DE COMPRAS:")
    print("1. Agregar un item")
    print("2. Eliminar un item")
    print("3. Ver la lista completa")
    print("4. Salir")
    #un input para que el usuario seleccione una opcion
    opcion = input("Selecciona una opción (1-4): ")
    # 3. Usamos if para cada opcion del menu, opcion para agregar
    if opcion == "1":
        item = input("¿Qué item desea agregar? ")
        lista_compras.append(item)
        print(f"{item} ha sido agregado a la lista.")
        #opcion para eliminar
    elif opcion == "2":
        item = input("¿Qué item desea eliminar?")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"{item} ha sido eliminado de la lista.")
        else:
            print(f"{item} no se encuentra en la lista.")
    #opcion para ver lista 
    elif opcion == "3":
        if len(lista_compras) == 0:
            print("La lista de compras esta vacia.")
        else: 
            print("Tu lista de compras:")
            for i, item in enumerate(lista_compras, 1): #enumerate() devuelve un objeto enumerado que contiene pares de indice y valor, el segundo argumento (1) indica que el indice comienza en 1 en lugar de 0
                print(f"{i}. {item}")
    #opcion para salir del menu
    elif opcion == "4":
        print("Hasta luego! Gracias por usar la lista de compras.")
    # cualquier otra opcion no valida
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

