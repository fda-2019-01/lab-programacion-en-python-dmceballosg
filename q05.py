##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
datos=open('data.csv','r').readlines()
datos=[ line.replace('\t', ';') for line in datos]
datos=[ line[0:3] for line in datos]

datos=[ line.split(';') for line in datos]
datos=[[line[0], int(line[1])] for line in datos]
col1=list(set([line[0] for line in datos]))
col1.sort()
min=10000000
max=-1
vector=[]
for letra in col1:
    for elem in datos:
        if elem[0]==letra:
            #Encontrar el minimo
            if elem[1]<min:
                min=elem[1]
            #Encontrar el maximo
            if elem[1]>max:
                max=elem[1]
    vector.append([letra, max, min])
    min=10000000
    max=-1
nuevo=[[line[0], str(line[1]), str(line[2])] for line in vector]   
registro=[ ','.join(line) for line in nuevo]
registro='\n'.join(registro)
print(registro)

