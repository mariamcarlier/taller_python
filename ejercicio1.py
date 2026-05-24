# Ejercicio 1: Análisis de Calificaciones en una Lista


print("Analizando calificaciones...")

#definimos la funcion de calificaciones
def analizar_calificaciones(calificaciones):
    #funcion que analiza una lista de calificaciones recibe notas y retorna la tupla con promedio, mayor y menor
    
    promedio = sum(calificaciones)/len(calificaciones)
    #sum() suma todos los elementos de la lista y len() cuenta cuantos hay
    # luego dividimos para obtener el promedio
    
    mayor = max(calificaciones)
    #max() devuelve el valor máximo de la lista
    
    menor = min(calificaciones)
    #min() devuelve el valor mínimo de la lista
    
    return (promedio, mayor, menor)
    #return devuelve los 3 valores en una tupla, es ordenada e inmutable

notas = [4.8, 3.5, 4.9, 2.8, 5.0, 3.7]
#definimos la lista en []
resultado = analizar_calificaciones(notas)
#llamamos la funcion psandole la lista el valor que retorna es la tupla 
print(f"El Promedio de las notas es: {resultado[0]:.2f}") 
#Accedemos a la tupla por su indice, resultado[0] es el promedio, resultado[1] es el mayor y resultado[2] es el menor
print(f"La nota mayor es: {resultado[1]:.2f}")
print(f"La nota menor es: {resultado[2]:.2f}")