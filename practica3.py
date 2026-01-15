"""
Imprimir la tabla de multiplicar del x utilizando un ciclo for
dame =x
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
.
.
7 x 10 = 70
fin
"""
x = int(input("Dame un numero: "))

for i in range(1, 11):
    multi = i * x
    print("{} x {} = {}".format(x,i,multi))
print("fin")
