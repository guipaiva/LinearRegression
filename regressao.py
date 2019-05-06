from ler_txt import *
import numpy as np
np.random.seed(0)

def hipotesis(x,theta):			#Hipótese
	hip = np.dot(theta.T,x)
	return hip

def cost(x,y,theta):		#Função Custo
	m = len(x)
	j = ((hipotesis(x,theta)-y)**2).sum()
	return j/2*m


def gradient(x,y,theta,max_iter,alpha):	
	m = len(x)
	for i in range(max_iter):
		for j in range(len(theta)):
			theta[j] = theta[j] - alpha/m *(((hipotesis(x,theta)-y)*x[j]).sum())
	return theta



print('Theta inicial: ',theta)
print('Custo inicial: ',cost(x,y,theta))
theta = gradient(x, y, theta, 4000, 1e-5)
print('Theta final: ',theta)
print('Custo final: ',cost(x,y,theta))
