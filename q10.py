##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
datos=open('data.csv','r').readlines()
datos=[ line.replace('\t', ';') for line in datos]
datos=[ line[:-1] for line in datos]

datos=[ line.split(';') for line in datos]
datos=[ line[-1] for line in datos]
datos=[ line.split(',') for line in datos]
datos=[ elem[:-2] for fila in datos for elem in fila ]

conjunto=set(datos)
nuevo=[[elem, str(datos.count(elem))] for elem in conjunto]
nuevo.sort()
registro=[ ','.join(line) for line in nuevo]
registro='\n'.join(registro)
    
with open("resumen.csv", "w") as f:
    f.write(registro)

print(registro)
