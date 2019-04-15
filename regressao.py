from ler_txt import *

#função Hipotese (a função ".T" retorna o vetor Theta transposto)

def hipotesis(theta,x):
	return x*theta

def cost(x,theta):
	m = len(x)
	soma = 0
	for i in range(m):
		soma+= pow((hipotesis(x[i],theta[i])-y[i]),2)
	j = (1/2*m)*soma
	return j

def main():
	print("custo = ",cost(x,theta))
main()