#  Dado el siguiente diccionario:
#  ventas = {
#  'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
#  'Cantidad': [10, 5, 7, 3, 2, 8]
#  }
#  Agrupa las cantidades por producto y muestra la suma total de ventas por cada uno.
#  # Salida esperada:
#  # {'A': 25, 'B': 7, 'C': 3}

ventas = {
  'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
  'Cantidad': [10, 5, 7, 3, 2, 8]
}

ventas_agrupadas = {}

for producto, cantidad in zip(ventas['Producto'], ventas['Cantidad']):
    if producto in ventas_agrupadas:
        ventas_agrupadas[producto] += cantidad  
    else:
        ventas_agrupadas[producto] = cantidad  

print(ventas_agrupadas)

