import numpy as np
m = np.random.rand(30,10)
n = n.empty(15,5)
def downsize(m):
	for i in range(n.shape()[0]):
		for j in range(n.shape()[1]):
			n[i,j] = (m[2i,2j] + m[2i+1,2j] + m[2i,2j+1] + m[2i+1,2j+1])/4
	return n


