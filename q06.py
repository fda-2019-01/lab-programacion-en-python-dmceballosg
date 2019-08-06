# coding=utf-8
##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
##
datos=open('data.csv','r').readlines()
datos=[ line.replace('\t', ';') for line in datos]
datos=[ line[:-1] for line in datos]
datos=[ line.split(';') for line in datos]
datos=[ line[-1] for line in datos]
datos=[ line.split(',') for line in datos]
#datos=' '.join(datos)
#datos=[ line.split(',') for line in datos]
datos=[elem for row in datos for elem in row]
datos=[line.split(':') for line in datos]
datos=[[line[0], int(line[1])] for line in datos]
#print(datos)

col1=list(set([line[0] for line in datos]))
col1.sort()
#print(col1)
min=10000000
max=-1
vector=[]
for letras in col1:
    for elem in datos:
        if elem[0]==letras:
            #Encontrar el minimo
            if elem[1]<min:
                min=elem[1]
            #Encontrar el maximo
            if elem[1]>max:
                max=elem[1]
    vector.append([letras, min, max])
    min=10000000
    max=-1
#print(vector)
nuevo=[[line[0], str(line[1]), str(line[2])] for line in vector]   
registro=[ ','.join(line) for line in nuevo]
registro='\n'.join(registro)
print(registro)