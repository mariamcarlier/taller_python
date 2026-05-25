print("=" * 55)
print ("📍✏️Ejercicio 4: Conversor de Unidades 📱📏")
print("=" * 55)

# El diccionario mapea conversiones con base en la unidad métrica 'Metros' (m)
factores_conversion = {
    "m_a_pie": 3.28084,
    "m_a_pulgada": 39.3701,
    "m_a_cm": 100.0,
    "cm_a_m": 0.01
}

def convertir_unidades(cantidad, origen, destino):
    """
    Realiza la conversión de unidades basándose en la composición de llaves del diccionario.
    Maneja con seguridad excepciones lógicas si las unidades solicitadas no existen.
    """
    llave_busqueda = f"{origen}_a_{destino}"
    
    if llave_busqueda in factores_conversion:
        factor = factores_conversion[llave_busqueda]
        return cantidad * factor
    else:
        # Retorna None indicando que la relación de conversión no está soportada
        return None

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
    resultado = convertir_unidades(cant, orig, dest)
    if resultado is not None:
        print(f" ✅ {cant:>3} [{orig}] equivalen a → {resultado:.2f} [{dest}]")
    else:
        print(f" ❌ Error: No se puede convertir de [{orig}] a [{dest}] (No Soportado)")
print("=" * 55)
