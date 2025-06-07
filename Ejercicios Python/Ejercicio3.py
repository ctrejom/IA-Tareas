# 📘 Ejercicio 3: Cree un programa que elimine los elementos repetidos de una
# lista y devuelva una nueva lista con elementos únicos ordenados.

lista = [6,3,5,6,3,3,6,8]

listaunica = []

for numero in lista:
    if numero not in listaunica:
        listaunica.append(numero)

listaunica.sort()

print("Lista original: ", lista)
print('Lista Unica: ',listaunica)

#Metodo sin  bucles
listaunica = sorted(set(lista))
print("Lista original: ", lista)
print('Lista Unica: ',listaunica)



