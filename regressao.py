from ler_txt import *
from random import randrange
import numpy as np

def hipotesis(i):
	hip = 0
	nvar = 3
	for j in range(nvar):
		hip+= x[i][j]*theta[j]
	return hip

def cost():
	j = 0
	m = len(x)
	for i in range(m):
		j+= pow((hipotesis(i)-y[i]),2)
	j*= (1/2*m)
	return j

def main():
	print("custo = ",cost())
main()