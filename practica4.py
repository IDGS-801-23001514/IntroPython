"""
pedir al usuario que ingrese 20 numeros repetidos y sin repetir, 
los almacene en una lista y luego muestre la lista ordenada de menor a mayor,
tambien nos diga cuantos son repetidos y cuantas veces se repitieron,
separarlos entre pares e inmpares
"""
numeros = []
for i in range(20):
    num = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(num)


print("\nLista original:")
print(numeros[:])


numeros.sort()
print("\nLista ordenada de menor a mayor:")
print(numeros[:])

repetidos = []
conteo = []

for n in numeros:
    if n not in repetidos:
        repetidos.append(n)
        conteo.append(numeros.count(n))

print("\nNúmeros repetidos:")
hay_repetidos = False
for i in range(len(repetidos)):
    if conteo[i] > 1:
        print(f"El número {repetidos[i]} se repite {conteo[i]} veces")
        hay_repetidos = True

if not hay_repetidos:
    print("No hay números repetidos")


pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\nNúmeros pares:")
print(pares)

print("\nNúmeros impares:")
print(impares)
