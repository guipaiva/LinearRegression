from read import *
from regression import *
from plot import *


print('Theta inicial: ',theta)								#Mostra o vetor theta inicial
print('Custo inicial: {:.2f}'.format(cost(x,y,theta))) 		#Mostra o custo incial 
theta = gradient(x, y, theta, max_iter, alpha,l_cost) 		#Atualiza o theta com o algoritmo do gradiente
print('Theta final: ',theta) 								#Mostra o theta após as atualizações
print('Custo final: {:.2f}'.format(cost(x,y,theta))) 		#Mostra o custo com o theta final

# Lê a entrada do usuário, calcula e mostra o tamanho do peixe de acordo com os valores encontrados de theta
i = int(input("Insira a idade do peixe: "))
t = int(input("Insira a temperatura do tanque: "))
size = theta[0] + theta[1]*i + theta[2]*t 
print("O tamanho esperado do peixe é: {:.2f}".format(size))

plota(l_cost) #Comentar esta linha caso não queria ver o gráfico