import csv
from random import randrange
import numpy as np

#lendo txt
f = open('data.txt','r')  
leitor_csv = csv.reader(f, delimiter=',')
x = list(leitor_csv)
y = []
for row in x:
	y.append(row.pop(2))

#setando as variaveis

theta = []
for i in range(len(x)):
	x[i].insert(0,1)
	theta.append(randrange(20))

x = np.array([[int(i) for i in lst] for lst in x])

theta = np.array([theta])


