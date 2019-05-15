import csv
import numpy as np
from statistics import mean

# inicializa os vetores/matrizes
x = [[] for i in range(3)] 		#Inicializa a Matriz X com 3 colunas
theta = np.random.rand(3) 		#Vetor Theta com valores aleatórios entre 0 e 1
y = [] 							#Vetor Y com o tamanho dos peixes
l_cost=[]  				  #Lista com o custo após cada atualização de theta, utilizado para plotar o gráfico
max_iter = 100 					#Limite de iterações
alpha = 1e-5 					#Tamanho do passo alpha 1*10^-5

#lendo txt e construindo a matriz X
f = open('data.txt','r')  
leitor_csv = csv.reader(f, delimiter=',')
for row in leitor_csv:
	x[0].append(1) 					#vetor x0 = 1
	x[1].append(float(row[1])) 		#idade do peixe 
	x[2].append(float(row[2])) 		#temperatura da água
	y.append(float(row[3]))			#Comprimento do peixe
f.close() 

'''
Abaixo foi realizada uma normalização dos dados, porém, após normalizar os dados a atualização dos valores 
de theta não se realizou de forma eficiente

avg1 = mean(x[1]) 				#média de x1
avg2 = mean(x[2]) 				#média de x2
s1 = (max(x[1])-min(x[1])) 		#faixa de valores de x1
s2 = (max(x[2])-min(x[2])) 		#faixa de valores de x2

for i in range(len(x[0])):
	x[1][i] = (x[1][i]-avg1)/s1
	x[2][i] = (x[2][i]-avg2)/s2
'''

#Transforma as listas no tipo numpy Array para facilitar os calculos
x = np.array(x)
y = np.array(y)
theta = np.array(theta)


