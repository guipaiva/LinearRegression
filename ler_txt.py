import csv
import numpy as np

# inicializa os vetores/matrizes
x = [[] for i in range(3)]
theta = np.random.rand(3) #define o vetor de tamanho 3 com numeros aleatorios entre 0 e 1
y = []


#lendo txt e construindo a matriz X
f = open('data.txt','r')  
leitor_csv = csv.reader(f, delimiter=',')
for row in leitor_csv:
	x[0].append(1) #vetor x0 = 1
	x[1].append(int(row[1])) #idade do peixe 
	x[2].append(int(row[2])) #temperatura da água
	y.append(int(row[3]))	#Comprimento do peixe

x = np.array(x)
y = np.array(y)
theta = np.array(theta)


