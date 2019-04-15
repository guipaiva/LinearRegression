import csv
from random import randrange
import numpy as np
#setando as variaveis
x = []
x1 = []
y = []
theta = []

#lendo txt e construindo a matriz, devemos transformar para int pois o leitor reconhece como string
f = open('data.txt','r')  
leitor_csv = csv.reader(f, delimiter=',')
for row in leitor_csv:
	x.append(int(row[0]))
	x1.append(int(row[1]))
	y.append(int(row[2]))

#concatenando os valores de x e x1 para cada coluna de x usando a função zip
#porém essa função retorna tuplas, então devemos transformar todos os elementos para lista
x = [list(x) for x in zip(x,x1)]

#inserindo o vetor x0 = 1 e setando valores aleatórios para teta
for i in range(len(x)):
	x[i].insert(0,1)
	theta.append(randrange(20))
#Transforma as listas para Array
theta = np.array(theta)
x = np.array(x)
y = np.array(y)



