##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
datos=open('data.csv','r').readlines()
datos=[ line.replace('\t', ';') for line in datos]
datos=[ line[:-1] for line in datos]
datos=[ line.split(';') for line in datos]
datos=[line[0] for line in datos]
conjunto=list(set(datos))
conjunto.sort()
nuevo=[[line, str(datos.count(line))] for line in conjunto]
registro=[ ','.join(line) for line in nuevo]
registro='\n'.join(registro)
print(registro)