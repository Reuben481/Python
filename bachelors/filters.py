import numpy as np 
from matplotlib import pyplot as plt
from myplot import myplot

omega1=10
omega2=100
pi=np.pi
e=np.e
xx=np.linspace(0,2*pi,128)
fx=np.ones(128)
fx[:64]=-1
"""
fx=(np.sin(2*xx)+2*np.cos(4*xx)+0.4*np.sin(xx)*np.sin(10*xx))*e**(-(xx**2)/10)
plt.plot(xx,fx)
plt.show()
myplot(xx,np.fft.fft(fx).real)
"""
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
"""
filt=low_ring_filt1(fx,10,15)
lpfx=np.fft.fft(fx)*filt
plt.plot(xx,np.fft.ifft(lpfx))
plt.plot(xx,fx)
plt.show()
"""

