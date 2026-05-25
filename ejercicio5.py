print("=" * 50)
print("Ejercicio 5: Mini Sistema de Gestión de Inventario - \nTienda Joyeria ")
print("=" * 50)

inventario = []
# esta lista/Funciona como variable global para almacenar los productos del inventario,pues es accesible desde cualquier parte del codigo. (las funciones pueden leerla y modificarla).

def agregar_producto(nombre, precio, cantidad):
    producto = {
        "nombre": nombre .strip() .capitalize() , 
        #strip() elimina espacios al inicio y al final, capitalize() pone la primera letra en mayuscula
        "precio": float (precio),
        "cantidad": int (cantidad)
    }
    inventario.append(producto)
    print(f"💍 Joya '{producto['nombre']}' registrada en el inventario con éxito.")
    #Una vez que el diccionario producto está ensamblado en memoria, se inyecta al final de nuestra lista global mediante .append().

# =====================================================================
# 2. Funcion de realizar venta para buscar el producto, validar stock,
#  aplicar descuentos y actualizar inventario
# =====================================================================
def realizar_venta():
    
    print("\n" + "=" * 50)
    print("--- 👩🏽‍💻 NUEVA VENTA DE JOYERÍA ---")
    print("=" * 50)
    
    #Busca la joya, pregunta detalles, aplica descuentos y descuenta el stock.
    busqueda = input("🔍 Ingresa el nombre del anillo a vender: ").strip().capitalize()

    # Recorremos la lista de diccionarios buscando coincidencias
    for producto in inventario:
        if producto["nombre"] == busqueda:
            cantidad_a_vender = int(input(f"¿Cuántas unidades de '{busqueda}' vas a facturar?: "))
        #if - verifica si el nombre del diccionario actual coincide con lo que el usuario escribió.

            # VALIDACION DE STOCK 
            if producto["cantidad"] >= cantidad_a_vender:
                
                # --- Seleccion de ocasion de uso/ venta para usuario ---
                print("\n¿Para qué ocasión es el anillo?")
                print("1. Compromiso (10% Descuento)")
                print("2. Regalo (Mensaje especial)")
                print("3. Uso personal")
                ocasion = input("Elige una opción (1-3): ").strip()
                
                descuento = 0.10 if ocasion == "1" else 0.0
                mensaje = "🎁 Incluye empaque y mensaje de regalo." if ocasion == "2" else ""
                
                # ACTUALIZACIÓN DE STOCK 
                producto["cantidad"] -= cantidad_a_vender
            #con asignacion de resta que provoca una accion matematica modificando el valor del diccionario, si la cantidad a vender es menor o igual al stock disponible, se procede a la venta, de lo contrario se muestra un mensaje de error.
            
            #esta se usò con el operador de asignacion compuesto -= que es una forma abreviada de escribir producto["cantidad"] = producto["cantidad"] - cantidad_a_vender, lo que actualiza el stock del producto restando la cantidad vendida.
                
                # Cálculos matemáticos
                subtotal = producto["precio"] * cantidad_a_vender
                valor_descuento = subtotal * descuento
                total_final = subtotal - valor_descuento
                
                # --- RESUMEN DE COMPRA ---
                print("\n========== 🧾 RESUMEN DE COMPRA ==========")
                print(f"Joya vendida : {busqueda}")
                print(f"Unidades     : {cantidad_a_vender}")
                print(f"Subtotal     : ${subtotal:,.2f}")
                if descuento > 0:
                    print(f"Descuento    : -${valor_descuento:,.2f} 💖 (Compromiso)")
                if mensaje:
                    print(f"Nota         : {mensaje}")
                print(f"TOTAL A PAGAR: ${total_final:,.2f}")
                print("==========================================")
                print("🙏 Gracias por confiar en nosotros.🤗")
                return True
                
            else:
                print(f"⚠️ Stock insuficiente. Solo nos quedan {producto['cantidad']} unidades de '{busqueda}'.")
                return False
                
    # Si el ciclo for termina y no encontró nada, llega aquí
    print(f"❌ Error: La joya '{busqueda}' no existe en nuestro inventario.")
    return False

def mostrar_inventario():
    #Imprime el estado actual de la bóveda de forma tabular.
    print("\n" + "=" * 55)
    print(f" {'💎 INVENTARIO: JOYERÍA ORO DEL SOL 💎':^53}")
    print("=" * 55)
    print(f"{'TIPO DE JOYA':<25} | {'PRECIO':<12} | {'STOCK':<10}")
    print("-" * 55)
    
    if not inventario:
        print(f"{'( La bóveda está vacía )':^55}")
    else:
        for p in inventario:
            print(f"{p['nombre']:<25} | ${p['precio']:>10,.2f} | {p['cantidad']:^10}")
            
    print("=" * 55)

# =====================================================================
# INICIALIZACIÓN Y MENÚ INTERACTIVO (Requisito del Taller)
# =====================================================================

# Agregamos datos de prueba para que el usuario no tenga que escribir todo de cero
agregar_producto("Anillo de 18k", 450000, 10)
agregar_producto("Anillo Compromiso", 930000, 15)
agregar_producto("Anillo de 15", 500000, 5)

def iniciar_sistema():
    """Bucle infinito que controla el flujo principal del programa."""
    while True:
        print("\n" + "=" * 50)
        print("--- 🏪 PANEL DE CONTROL - ORO DEL SOL 🏪 ---")
        print("=" * 50)
        print("   [1] 💍 Agregar nueva joya al inventario")
        print("   [2] 🤝 Realizar una venta")
        print("   [3] 📋 Mostrar inventario completo")
        print("   [4] 🚪 Salir del sistema")
        
        opcion = input("\n👉 Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            print("\n--- 📦 INGRESO DE MERCANCÍA ---")
            nom = input("Nombre de la joya: ")
            prec = input("Precio unitario base: ")
            cant = input("Cantidad a ingresar: ")
            agregar_producto(nom, prec, cant)
            
        elif opcion == "2":
            realizar_venta()
            
        elif opcion == "3":
            mostrar_inventario()
            
        elif opcion == "4":
            print("\n🚪 Cerrando el sistema de la joyería. ¡Hasta pronto!")
            print("=" * 45)
            break
            
        else:
            print("❌ Opción inválida. Intente de nuevo con un número del 1 al 4.")

# Punto de entrada del programa
if __name__ == "__main__":
    iniciar_sistema()
