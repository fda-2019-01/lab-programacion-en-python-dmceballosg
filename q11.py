##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
datos=open('data.csv','r').readlines()
datos=[ line.replace('\t', ';') for line in datos]
datos=[ line[:-1] for line in datos]
datos=[ line.split(';') for line in datos]
datos=[[line[0], line[3].split(','), line[4].split(',')] for line in datos]
datos=[[lista[0], str(len(lista[1])), str(len(lista[2]))]for lista in datos]
registro=[ ','.join(line) for line in datos]
registro='\n'.join(registro)
        
with open("punto11.csv", "w") as f:
    f.write(registro)

print(registro)
