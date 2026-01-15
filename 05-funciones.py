import os

def saludar(nombre):
    """Funcion de saluda a la persona cuyo nombre se paso como argumento"""
    return f"Hola,{nombre}!"
def sumar(a,b):
    """uncion que devuelve la suma de dos numeros"""
    return a+b
os.system("cls")
saludar("Ana")
os.system("pause")

def main():
    os.system("cls")
    saludar("Juan")
    resultado_suma = sumar(5,7)
    print("La suma de 5 y 7 es:", resultado_suma)

if __name__ == "__main__":
    main()