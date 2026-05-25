print("=" * 55)
print ("📍✏️ Ejercicio 4: Conversor de Unidades 📱📏")
print("=" * 55)

# 1. Base de Conocimiento (Diccionario de Factores)
# El diccionario mapea conversiones con base en la unidad métrica 'Metros' (m)
factores_conversion = {
    "m_a_pie": 3.28084,
    "m_a_pulgada": 39.3701,
    "m_a_cm": 100.0,
    "cm_a_m": 0.01
}

# 2. Función Principal de Conversión
def convertir_unidades(cantidad, origen, destino):

    """Realiza la conversión de unidades basándose en la composición de llaves del diccionario.
    Maneja con seguridad excepciones lógicas si las unidades solicitadas no existen."""
    #Recibe una cantidad y las unidades. Busca el factor matemático en el diccionario usando una clave construida dinámicamente.

    llave_busqueda = f"{origen}_a_{destino}"

# Manejo de errores lógicos: Validamos si la clave existe en el diccionario antes de intentar la conversión. Si no existe, retornamos None para indicar que la conversión no es posible.   
    if llave_busqueda in factores_conversion:
        factor = factores_conversion[llave_busqueda]
        return cantidad * factor
    else:
        # Retorna None indicando que la relación de conversión no está soportada
        return None

# 3. Pruebas del Sistema (Consola)
# --- EVALUACIÓN DE CASOS EN CONSOLA ---
print("=" * 55)
print(" 📐 SISTEMA DE CONVERSIÓN DE MEDIDAS MÉTRICAS")
print("=" * 55)

pruebas = [
    (5, "m", "pie"),
    (150, "cm", "m"),
    (10, "m", "yarda") # Caso de error controlado
]

for cant, orig, dest in pruebas:
    # Se llama a la función y se guarda lo que nos devuelve
    resultado = convertir_unidades(cant, orig, dest)
    if resultado is not None:
        print(f" ✅ {cant:>3} [{orig}] equivalen a → {resultado:.2f} [{dest}]")
    else:
        print(f" ❌ Error: No se puede convertir de [{orig}] a [{dest}] (No Soportado)")
print("=" * 55)
