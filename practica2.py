""" Crear un programa que tenga un menu con las siguientes opciones: 
1. suma
2. resta
3. multiplicacion
4. division
5. salir
Cada opcion debe ser una funcion diferente
"""
import os

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a // b

def main():
    opcion = 0

    while opcion != 5:
        os.system("cls")
        print("----- MENÚ -----")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion >= 1 and opcion <= 4:
            a = int(input("Ingresa el primer número: "))
            b = int(input("Ingresa el segundo número: "))

        if opcion == 1:
            print("Resultado:", sumar(a, b))
        elif opcion == 2:
            print("Resultado:", restar(a, b))
        elif opcion == 3:
            print("Resultado:", multiplicar(a, b))
        elif opcion == 4:
            print("Resultado:", dividir(a, b))
        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opción no válida")

        os.system("pause")

if __name__ == "__main__":
    main()
