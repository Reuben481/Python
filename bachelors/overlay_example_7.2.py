import numpy as np 
from matplotlib import pyplot as plt
from myplot import myplot

pi=np.pi
numSamples=128
dt=1./numSamples

xx=np.linspace(-11./24,12./24,numSamples)
#xx=np.linspace()
xxp=np.linspace(-0.5,0.5,numSamples)
fx=np.cos(2*pi*xx) + 0.5*np.cos(10*pi*xx) + (1./3)*np.cos(12*pi*xx)
fx1=np.cos(2*pi*xx)

def standard_square_pulse(n,width,c=1.,tweek=0):
	filt=np.zeros(n)
	filt[n/2-(width/2+tweek+1)],filt[n/2+(width/2+tweek+1)]=c/2,c/2
	filt[n/2-(width/2+tweek):n/2+(width/2+1+tweek)]=c
	return filt
#hn=np.fft.fftshift([0,0,0,0,0,0,0,0,0,0,1./8,1./4,1./4,1./4,1./8,0,0,0,0,0,0,0,0,0])
hn=np.fft.fftshift(standard_square_pulse(numSamples,int(0.125*numSamples),c=1./(numSamples/6)))

fx2=np.fft.ifft(np.fft.fft(fx)*np.fft.fft(hn))

def fft_plot_and_sublpot(xx,fx,dt=1):
	n=len(xx)
	
	plt.subplot(211)
	plt.plot(xx,fx, label="time domain")
	plt.legend()
	
	plt.subplot(212)
	myplot(len(xx)*np.fft.fftfreq(len(xx)),abs(1./n*np.fft.fft(fx).real),label="frequency domain")
	plt.legend()
	plt.xlabel('X')

#fft_plot_and_sublpot(xxp,np.fft.fft(hn).real)
#plt.show()

#plt.figure()


plt.subplot(211)
plt.plot(xx,fx,label='unthresholded function f(x)')
plt.legend()

plt.subplot(212)
plt.plot(xx,fx1,'b',label='original function')
plt.plot(xx,fx2,'r--',label='thresholded function')
plt.xlabel('X')
plt.legend()

print(np.linalg.norm(abs(fx1-fx2),2))
"""
plt.figure()
plt.plot(xx,abs(fx1-fx2))
plt.xlabel('X')
plt.title('absolute difference')
"""
plt.show()

