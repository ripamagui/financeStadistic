import numpy as np 

#array 1D
a = np.array([1,2,3]) #Para crear un array de una dimencion

print(a)

#array 2D
b =np.array([(1,2,3),(4,5,6)]) #Pongo cada dimension entre ()
print(b)

#Matrices Vacias 
vacia = np.empty((3,2))
print(vacia)

#1 Matrices que sean iguales a 1. entre () pongo las filas y columnas que necesito
unos = np.ones((3,4))
print(unos)

#0 Para todos los valores igual cero
ceros = np.zeros((3,4))
print (ceros)

#random para que los valores sean aleatorios
aleatorios = np.random.random((2,2))
print(aleatorios)

#un mismo valor  Para que la matriz tenga el mismo numero en todas las posiciones (dimensiones),num
full = np.full((2,2),8)
print(full)

#Para matrices espaciadas con cantidad igual
#Cuando doy el valor del espacio
espacio = np.arange(0,30,5) #desde 0 a 30 cada 5
print(espacio)

#cuando le doy la cantidad de valores que quiero
espacio2 = np.linspace(0,2,5) #desde 0 a 2 quiero 5 valores
print(espacio2)

#Dimension de la matriz NDIM
b.ndim
print(b.ndim)

#Tipo de datos 
b.dtype
print(b.dtype)

#tamaño SIZE y forma de la matriz SHAPE
print (a.size)
print (b.shape)

#RESHAPE Cambio de tamaño y dorma (para que las filas pasen a ser columnas)
c = np. array([(3,4,5),(6,7,8)])
print (c)
c = c.reshape(3,2) #(n de filas, n de colum)
print(c)

#Seleccion de un elemento
#variables[fila,columna] puedo poner : despues del num para que me tome todos los valores
print(c[0,1])
print(c[0:,1])

#OPERACIONES MATEMATICAS
#puedo operar entre las matrices 
g =np.array([2,5,8])
#Minimo
print(g.min())

#Maximo
print(g.max())

#Sumar 
print(g.sum())

h=np.array([(1,2,3),(3,4,5)])
#raiz cuadrada
print(np.sqrt(h))  #me da la raiz de cada numero de la matriz

#desviacion estandar
print(np.std(h))  #sobre todos los numeros de la matriz


#Operaciones entre matrices - hago mas operaciones simples de python 
x = np.array([(1,2,3),(3,4,5)])
y = np.array([(1,2,3),(3,4,5)])
print(x+y)
print(x-y)
print(x*y)
print(x/y)
