#📘 Ejercicio 1: Calcular el número mayor de una lista sin usar max()
 
def mayor_lista(lista):

    mayor = None
    
    # Manera Tradicional
    for i in range(len(lista)):
        if i == 0 or mayor < lista[i]:
            mayor = lista[i]
    print("El mayor de la lista es:", mayor)

    mayor = None

    #Manera mas moderna a mi parecer
    for numero in lista:
        if mayor is None or numero > mayor:
            mayor = numero

    print("El mayor de la lista es:", mayor)
    

lista = [4,8,3,5,7,9,6,4]
print(mayor_lista(lista))