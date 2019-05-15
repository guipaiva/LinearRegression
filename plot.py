from read import *
from regression import *
import matplotlib.pyplot as plt

def plota(l_cost):
	#Cria e plota o gráfico do custo
	fig = plt.figure() 		#cria um objeto figure e atribui a variavel fig
	ax = fig.add_subplot(111) 		#Aloca uma matriz 1x1 de gráficos para a figura
	plt_x1 = np.linspace(0,max_iter,len(l_cost)) 		#Gera o dominio da função indo de 0 até iteração maxima
	l_cost = [i/1e6 for i in l_cost] 		#Divide por 10^6 para o valor ficar apresentável no gráfico
	plt.plot(plt_x1,l_cost) 		#Plota o grafico a partir do dominio e imagem

	#Define títulos e a grade para melhor visualização e entendimento
	ax.set_title("Gráfico do Custo")
	ax.set_yticks(np.arange(0,5,0.5))
	ax.set_xlabel("Iteração")
	ax.set_ylabel(r"Custo x 10$^6$")
	ax.grid(True)
	plt.show()