##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
datos=open('data.csv','r').readlines()
datos=[ line.replace('\t', ';') for line in datos]
datos=[ line[:-1] for line in datos]
datos=[ line.split(';')[2] for line in datos]
datos=[ line.split('-')[1] for line in datos]
conjunto=list(set(datos))
conjunto.sort()
nuevo=[[line, str(datos.count(line))] for line in conjunto]
registro=[ ','.join(line) for line in nuevo]
registro='\n'.join(registro)
print(registro)