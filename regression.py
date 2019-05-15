from read import *

def hipotesis(x,theta):			#Hipótese
	hip = np.dot(theta.T,x)		#Faz a multiplicação entre theta transposto e a matriz x
	return hip

def cost(x,y,theta):		#Função Custo
	m = len(x[1])			#Número de linhas da matriz X
	j = sum((hipotesis(x,theta)-y)**2) 		#Calcula a hipótese, subtrai de y e eleva ao quadrado
	j = j/(2*m)		#Faz a normalização dividindo pelo tamanho
	return j


def gradient(x,y,theta,max_iter,alpha,l_cost):	
	m = len(x[1])		
	for i in range(max_iter): 		#Itera até o limite
		for j in range(len(theta)):	#Para cada posição do vetor theta
			theta[j] = theta[j] - alpha/m *(sum((hipotesis(x,theta)-y)*x[j]))  #Atualiza o elemento da posição 
		l_cost.append(cost(x,y,theta))  	#Adiciona à lista o custo com o vetor theta atual
	return theta
