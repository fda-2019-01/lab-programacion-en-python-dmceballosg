##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras (ordenadas y sin repetir letra) 
## de la primera  columna que aparecen asociadas a dicho valor de la 
## segunda columna. Esto es:
##
## ('0', ['C'])
## ('1', ['A', 'B', 'D', 'E'])
## ('2', ['A', 'D', 'E'])
## ('3', ['A', 'B', 'D', 'E'])
## ('4', ['B', 'E'])
## ('5', ['B', 'C', 'D', 'E'])
## ('6', ['A', 'B', 'C', 'E'])
## ('7', ['A', 'C', 'D', 'E'])
## ('8', ['A', 'B', 'E'])
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
datos1=[ (elem, list(set([ line[0]  for line in datos if elem== line[1]] ))) for elem in conjunto]
nuevo=[]
for x,y in datos1:
    y.sort()
    nuevo.append((x,y))

datos2=[ str(tupla) for tupla in nuevo]
unirtuplas='\n'.join(datos2)
print(unirtuplas)