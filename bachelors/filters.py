import numpy as np 



def low_ring_filt1(f,start,stop):
	filt=np.ones(len(f))
	slope = 1./abs((stop-start))
	for i in range(len(f)):
		if stop>=i>=start:
			filt[i]=filt[i-1]-slope
		if i >= stop:
			filt[i]=0
	filt[len(fx)/2:]=np.flip(filt[:len(fx)/2],0)
	print(len(fx))
	return filt

def standard_square_pulse(n,width,c=1.,tweek=0):
	filt=np.zeros(n)
	filt[n/2-(width/2)],filt[n/2+(width/2+1)]=c/2,c/2
	filt[n/2-(width/2+1):n/2+(width/2+1)]=c
	return filt

def tapering_filt(n,dx,width,c=1.,tweek=0):
	filt=np.zeros(n)
	filt[n/2-(width/2+tweek):n/2+(width/2+1+tweek)]=c
	for i in range(dx):
		filt[n/2-(width/2+tweek+i)],filt[n/2+(width/2+tweek+i)]=(dx-i)*(c/dx),(dx-i)*(c/dx)
	return filt

def sin_filt(n,dx,width,c=1.,tweek=0):
	filt=np.zeros(n)
	filt[n/2-(width/2+tweek):n/2+(width/2+1+tweek)]=c
	for i in range(dx):
		filt[n/2-(width/2+tweek+i)],filt[n/2+(width/2+tweek+i)]=c*np.sin(pi*(dx-i)/(2*dx)),c*np.sin(pi*(dx-i)/(2*dx))
	return filt

