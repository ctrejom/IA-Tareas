# 📘 Ejercicio 4: Escriba un programa que solicite ingresar el nombre de varios
#  estudiantes y su nota, y lo almacene en un diccionario. Al final, muestra los
#  datos almacenados.


veces = int(input("\n Ingrese el numero de estudiantes que desea agregar: "))

estudiantes = {}

i = 1 
while i <= veces :
    try:
        nombre = str(input(f"Ingrese el nombre del estudiante {i}: "))
        nota = float(input(f"Ingrese la nota de {nombre}: "))   
        
        #Almacenamos los datos en el diccionario
        estudiantes[nombre] = nota
        i += 1
    except ValueError:
        print("Debe de ingresar los datos en el formato correcto")

print("\n Datos de los estudiantes")
print(estudiantes)
