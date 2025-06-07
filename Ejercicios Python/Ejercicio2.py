#  Ejercicio 2: Escriba un programa que solicite un número al usuario y
#  muestre la tabla de multiplicar del 1 al 10 de ese número.

def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")

while True:
    try:
        numero = int(input("Ingrese un numero para ver la tabla de multiplicar del 1 al 10"))
        tabla_multiplicar(numero)
        break
    except ValueError: 
        print("Debe de ingresar un numero")
