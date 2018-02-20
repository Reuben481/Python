import numpy as np 
from matplotlib import pyplot as plt
from myplot import myplot

pi=np.pi
numSamples=32
dt=1./numSamples

xx=np.linspace(-11./24,12./24,numSamples)
#xx=np.linspace()
n=np.random.rand(numSamples)
n=n-np.mean(n)
xxp=np.linspace(-0.5,0.5,numSamples)
fx=np.cos(2*pi*xx) + 0.5*np.cos(10*pi*xx) + (1./3)*np.cos(12*pi*xx)+n
fx1=np.cos(2*pi*xx)

def standard_square_pulse(n,width,c=1.,tweek=0):
	filt=np.zeros(n)
	filt[n/2-(width/2+1)],filt[n/2+(width/2+1)]=c/2,c/2
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
hn=standard_square_pulse(numSamples,4,c=1.)
#hn=tapering_filt(numSamples,2,4,c=1.)
#hn=np.fft.fftshift(sin_filt(numSamples,numSamples/4,int(0.125*numSamples),c=1./(numSamples/4)))
fftfx2=np.fft.fft(fx)*np.fft.fftshift(hn)
fx2=np.fft.ifft(np.fft.fft(fx)*np.fft.fftshift(hn))
#fx2=np.fft.ifft(np.fft.fft(fx)*hn)
def fft_plot_and_sublpot(xx,fx,dt=1):
	n=len(xx)
	
	plt.subplot(211)
	plt.plot(xx,fx, label="time domain")
	plt.legend()
	
	plt.subplot(212)
	myplot(len(xx)*np.fft.fftfreq(len(xx)),abs(1./n*np.fft.fft(fx).real),label="frequency domain")
	plt.legend()
	plt.xlabel('X')

def ifft_plot_and_sublpot(xx,fx,dt=1):
	n=len(xx)
	
	plt.subplot(211)
	plt.plot(xx,np.fft.ifft(fx), label="time domain")
	plt.legend()
	
	plt.subplot(212)
	myplot(len(xx)*np.fft.fftfreq(len(xx)),fx,label="frequency domain")
	plt.legend()
	plt.xlabel('X')
ifft_plot_and_sublpot(xx,hn)
plt.show()
"""
myplot(np.arange(numSamples),np.fft.fftshift(hn))
plt.figure()

myplot(np.arange(numSamples),np.fft.fft(fx))

plt.figure()

myplot(np.arange(numSamples),fftfx2)
plt.figure()
plt.subplot(211)
plt.title('Square low pass filter')
plt.plot(xx,fx,label='unthresholded function f(x)')
plt.legend()

plt.subplot(212)
plt.plot(xx,fx1,'b',label='original function')
plt.plot(xx,fx2,'r--',label='thresholded function')
plt.xlabel('X')
plt.legend()

print('l2 norm',np.linalg.norm(abs(fx1-fx2),2))

print('inf norm',np.linalg.norm(abs(fx1-fx2),np.inf))

plt.show()
"""
