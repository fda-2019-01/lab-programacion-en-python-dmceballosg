##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##

datos=open('data.csv','r').readlines()
datos=[ line.replace('\t', ';') for line in datos]
datos=[ line[:-1] for line in datos]
datos=[ line.split(';') for line in datos]
datos=[ [line[0], line[-1].split(',')] for line in datos]
numeros=[line[1] for line in datos]
numeros=[[int(elem[-1]) for elem in line] for line in numeros]
suma=0
nuevo=[]
for i, line in enumerate(numeros):
    for elem in line:
        suma=suma+elem
    nuevo.append([datos[i][0],str(suma)])
    suma=0

registro=[ ','.join(line) for line in nuevo]
registro='\n'.join(registro)
print(registro)

