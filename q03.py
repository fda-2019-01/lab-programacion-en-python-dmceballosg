##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
datos=open('data.csv','r').readlines()
datos=[ line.replace('\t', ';') for line in datos]
datos=[ line[:-1] for line in datos]
datos=[ line.split(';') for line in datos]
col1=list(set([line[0] for line in datos]))
col1.sort()
col12=[[ line[0],int(line[1])] for line in datos]
#col12.sort()
suma=0
nuevo=[]
for letra in col1:
    for elemento in col12:
        if elemento[0]== letra:
            suma=suma+elemento[1]
    nuevo.append([letra,suma])
    suma=0
nuevo=[[line[0], str(line[1])] for line in nuevo]
nuevo=[','.join(line) for line in nuevo]
nuevo='\n'.join(nuevo)
print(nuevo)
