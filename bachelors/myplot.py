import numpy as np 
from matplotlib import pyplot as plt 

def myplot(xx,fx,label=None,c='k'):
	for i in range(len(xx)):
		plt.plot([xx[i],xx[i]],[fx[i],0],c)
	plt.scatter(xx,fx,s=1,c=c,label=label)

