"""
Una lista es una coleccion de datos ordenada modificable y se define con corchetes []
"""

mi_lista = [1,2,3,4,5]
print(type(mi_lista))
print(mi_lista[:])#muestra la lista completa
print(mi_lista[2])#muestra lo que se encuentra en la posicion 2
print(mi_lista[-1])#va de atras hacia adelante asi que muestra el ultimo numero
print(mi_lista[0:3])#recorre desde la posicion 0 a la 3
print(mi_lista[3:])#muestra dela posicion 3 en adelante

#la lista puede tener diferente tipo de dato
#append permite añadir elementos a la lista
#insert añade elementos a la lista pero yo diciendole en que posicion lo añada
#añade a la lista otra lista
#remove quita el primer elemento especificado de la lista
#extrae un elemento de la lista en base al indice
#sort ordena una lista
lista1=["Dario",33,9.5,True,"German",20.8]
lista1.append("Vargas")
print(lista1)

lista1.insert(2,"Nadia")
print(lista1)

lista1.extend(["uno", 1.1,False])
print(lista1)

lista1.remove(33)
print(lista1)

lista1.pop()
print(lista1)

lista2=["tres","cuatro"]
lista3=lista1+lista2
print(lista3)

print(lista2*4)
lista4=[2,1,5,4,3]
print(lista4)
print(lista4.sort())

del lista4[0]
print(lista4)