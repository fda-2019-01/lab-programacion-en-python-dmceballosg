##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas) de la primera 
## columna que aparecen asociadas a dicho valor de la segunda 
## columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'A', 'B', 'D', 'E', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E', 'E'])
## ('9', ['A', 'B', 'C', 'E'])
##
##
datos=open('data.csv','r').readlines()
datos=[ line.replace('\t', ';') for line in datos]
datos=[ line[0:3] for line in datos]

datos=[ line.split(';') for line in datos]
conjunto=list(set([line[1] for line in datos]))
conjunto.sort()
datos=[[line[0], line[1]] for line in datos]
datos.sort()
datos1=[ str((elem, [ line[0]  for line in datos if elem== line[1] ])) for elem in conjunto]
unirtuplas='\n'.join(datos1)
print(unirtuplas)