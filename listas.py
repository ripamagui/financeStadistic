#Los array son listas de variables o datos separadas por , y entre [] 
#Incluso puedo tener otras listas dentro de este
# listas/array/trupa/diccionario/matrices/arreglos 
[1,"hello",1.23,True,[1,2,3]]

#puedo ponerle un nombre de vatiable 
color =["red","green","blue"]
print (color)

#las ruplas con listas entre () en vez de [] 
#lo que permiten las tuplas es introducir una funcion 
numList =list((1,2,3))

#1,2,3 es la tupla y list() la funcion
print(numList)

#Range es la funcion para crear una lista con un rango
range(1,10)
r =list(range(1,10)) #list me da la creacion de lista
print(r)
#SUPER IMPORTANTE!
#no va a tomar el ultimo elemento, range hace la lista desde el primer valor hasta el segundo-1

#Diccionarios 
#Van estar definidas por {} cada elemento lo voy a separar con , 

diccionario  = {"Benecio","Rodrigo","Estefani","Sandra"}
print(diccionario)

#Comandos utiles para usar en listas 
#para saber la longitud de una lista
len(r)
print(len(r))

#Cuando quiero traer un valor especifico que esta en la lista voy a usar el nombre y [] voy a poner la posicion 
#OJO! que cuenta desde cero 
color[2]
print(color[2])
#puedo poner posiciones en positivo o negativo. Cuando pongo en neg empieza a contar desde la izquierda
print(color[-1])

#Para saber si un valor esta dentro de esta lista. vos a usar IN 
#Esto es un booliano, me va a responder "True" o "false"
print("green" in color)

#Cabiar valores en las listas - para eso voy a poner el nombre de la lista con la posicion en [] = al nuevo valor
color[1] = "yellow"
print(color)

#Para agregar un nuevo valor uso la funcion append 
color.append("violet")
print(color)

#Cuando quiero poner mas de un elemento en las lista uso extend con una lista []
color.extend (["orange","purple"])
print(color)

#Para incorporarlo en una posicion determinada uso insert (posicion,elemento)
color.insert(2,"pink")
#lo puedo agregar al final puedo poner len() para la posicion
color.insert(len(color),"black")
print(color)

#para quitar el ultimo elementos uso pop
color.pop()
print(color)
#si quiero quitar un valor en un indice lo pongo entre ()
color.pop(1)
print(color)

#cuando quiero quitar un valor segun como se llama uso 
color.remove("red")
print(color)


#Para ordenrar alfabeticamente SORT 
color.sort()
print(color)
color.sort(reverse=True) #Para hacerlo de Z a A
print(color)

#para conocer un indice/posicion
color.index("pink")
print(color.index("pink"))

#Cuantas veces existe un elemento
color.count("pink")
print(color.count("pink"))

#Cuando quiero basiar la lista uso clear
color.clear()
print(color)