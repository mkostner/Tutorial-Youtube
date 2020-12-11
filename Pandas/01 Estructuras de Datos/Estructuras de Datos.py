# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:03:20 2020

@author: mkostner
"""

#importamos las bibliotecas que utilizaremos
import numpy as np
import pandas as pd


#Series
#  s = pd.Series(data, index=index) estructura basica tenemos una fuente de informacion y un indice

#Desde un Numpy Array
data=np.random.randn(5) #array random 
s = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
s
#Podemos Acceder al indice
s.index



#Desde Diccionarios
d = {'b': 1, 'a': 0, 'c': 2}
pd.Series(d)

#si ademas pasamos un indice
d = {'a': 0., 'b': 1., 'c': 2.}
pd.Series(d, index=['b', 'c', 'd', 'a'])


#Desde un valor escalar
pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])

#si necesitamos un np.array podemos utilizar
s.to_numpy()

#Las Series funcionan de manera muy similar a un diccionario
s['a']
s['e'] = 12.
s
'e' in s
'f' in s

#Si eventualmente no existe la etiqueta
s['f'] # nos genera una excepcion

#Si deseamos eliminar esto podemos utilizar el metodo get()
s.get('f')

# O
s.get('f', np.nan)


#Las Series nos permiten ejecutar operaciones vectorizadas para no tener que iterar por cada valor
s+s
s*2
np.exp(s)


#Alineacion de etiquetas, devuelve la union de ambas partes
s[1:] + s[:-1]


#Le asignamos un nombre a la serie 
s = pd.Series(np.random.randn(5), name='something')
s

s.name

#tambien podemos renombrar nuestra serie
s2 = s.rename("different") #importante notar que S2 es distinto a s
s2.name

###########################################################################

#DataFrames
#Generamos un diccionario de Series
d = {'uno': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'dos': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
df

pd.DataFrame(d, index=['d', 'b', 'a'])

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['dos', 'tres']) #en este caso la Columna 'tres' no existe

#Podemos investigar nuestro DataFrame
df.index

df.columns

#ahora vamos a generar un df desde un diccionario de arrays
d = {'uno': [1., 2., 3., 4.],
     'dos': [4., 3., 2., 1.]}

pd.DataFrame(d)

pd.DataFrame(d, index=['a', 'b', 'c', 'd'])


#Los df son muy flexibles tambien se pueden generar por medio de una lista de diccionarios
data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

pd.DataFrame(data2)
pd.DataFrame(data2, index=['uno', 'dos'])

pd.DataFrame(data2, columns=['a', 'b'])

#otra opcion es con un diccionario de tuplas
pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
              ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
              ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
              ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
              ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})


#Selección,adición y eliminación de columnas

df['uno']

df['tres'] = df['uno'] * df['dos']

df['flag'] = df['uno'] > 2 #donde es mayor asignamos una nueva columna con un boolean
df

#las columans tambien se pueden elimina
del df['dos']
#Tambien podemos abrirla como un diccionario
three = df.pop('tres')

#si deseamos insertar un valor escalar, se propagara por toda la columns
df['buu']='baar'

#Tambien podemos insertar una serie que no tenga el mismo indice

df['uno_trucado'] = df['uno'][:2]
df

#y tambien podemos insertar nuevas 
df.insert(1, 'bar', df['uno']) #en la columna 1, bajo el nombre bar y los datos de la columna uno


#############################
#Cargamos un df desde un archivo csv 
iris = pd.read_csv('iris.csv') #si estas en la misma carpeta que el archivo py sino (r'ruta\iris.csv')
#revisamos el encabezado
iris.head(2)
iris.tail()

#assign() nos permite crear nuevas columnas que derivan de columnas existentes
(iris.assign(sepal_ratio=iris['sepal_width'] / iris['sepal_length']).head()) 
#es importante notar que la funcion assign() crea una copia del df 

#otro uso comun para el metodo assign es pasarle una funcion
iris.assign(sepal_ratio=lambda x: (x['sepal_width'] / x['sepal_length'])).head()
#entregando el mismo resultado

#parsar un invocable a diferencia de un valor real, es until cuando tenemos cadenas de operaciones,
#por ejemploi limitamos el df a solo las observaciones cuya longitud de sepalo sea mayor que 5

(iris.query('sepal_length > 5').assign(SepalRatio=lambda x: x.sepal_width / x.sepal_length,
                                      PetalRatio=lambda x: x.petal_width / x.petal_length)
 .plot(kind='scatter', x='SepalRatio', y='PetalRatio'))

#otro ejemplo es para reforzar las cadenas de operaciones
dfa = pd.DataFrame({"A": [1, 2, 3],
                    "B": [4, 5, 6]})

dfa.assign(C=lambda x: x['A'] + x['B'],
           D=lambda x: x['A'] + x['C'])
