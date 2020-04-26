import pandas as pd 
import numpy as np 

#crear los data frame
#voy a crear la matriz desde numpy y voy a crear el frame desde pandas

data = np.array([['','Col1','Col2'], ['Fila1',11,22],['Fila2', 33,44]])
print(pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:]))

df = pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]))
print('DataFrame:')
print (df)

#Creacion de series
#Voy hacerlo desde un diccionario {}
#Mantiene las posiciones entonces ARG es cero y Peru 3
series = pd.Series({'Argentina':'Buenos Aires',
'Chile':'Santiago de Chile',
'Colombia':'Bogota',
'Peru':'Lima'}) #Voy a separar los conceptos de las columnas por :
print(series)

#Explorar el Data Frame

#forma de los datos variable.shape
print(df.shape)

#altura del DF len(varible.index)
print(len(df.index))

#medida de las columnas variable.mean()
print(df.mean)


#Estisticas del DF
#Describe() muestra estadisticas de resumen de columnas
print(df.describe())

#Correlacion de columnas variable. corr()
print(df.corr())

#Cuenta los valores no nulos variables.count()
print(df.count())

#Maximo valor por columna variable.max()
print(df.max())

#Minimo valor por columna variable.min()
print(df.min())

#Mediana de cada columna variable.median()
print(df.median())

#Desviacion estandar de cada columna variable.std()
print(df.std())

#Seleccion de datos en las matrices 
#solo voy a indicar []el indice 
print(df[1])

#tambien se puede hacer con algunas columnas 
print(df[0,1])
