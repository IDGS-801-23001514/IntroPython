'''
operacion de multiplicacion de a * b utilizando sumas
salida 3+3+3+3=12
'''
a=3
b=4

resultado = 0
tem = ""
x = 0

while x < b:
    resultado += a
    tem += str(a) + "+"
    x += 1

tem = tem[:-1]

print(tem + "=" + str(resultado))