##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
datos=open('data.csv','r').readlines()
datos=[ line.replace('\t', ';') for line in datos]
datos=[ line[:-1] for line in datos]
datos=[ line.split(';') for line in datos]
conjunto=[line[-2].split(',') for line in datos]
conjunto=[elem for line in conjunto for elem in line]
conjunto=set(conjunto)

datos=[ [int(line[1]), line[-2].split(',')] for line in datos]
suma=0
nuevo=[]
for elem in conjunto:
    for fila in datos:
        if elem in fila[1]:
            suma=suma+fila[0]
    nuevo.append([elem, str(suma)])
    suma=0
nuevo.sort()

registro=[ ','.join(line) for line in nuevo]
registro='\n'.join(registro)


print(registro)
