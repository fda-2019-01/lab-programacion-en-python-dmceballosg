## Imprima la suma de la segunda columna.
##
datos=open('data.csv','r').readlines()
datos=[ line.replace('\t', ';') for line in datos]
datos=[ line[:-1] for line in datos]
datos=[ line.split(';') for line in datos]
col2=[int(line[1]) for line in datos]
suma=0
for line in col2:
    suma=suma+line
print(suma)

