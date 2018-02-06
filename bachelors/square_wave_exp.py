import numpy as np 
from matplotlib import pyplot as plt
from myplot import myplot
pi=np.pi
numSamples=128
xx=np.linspace(-pi,pi,numSamples)
fx=np.ones(numSamples)
fx[:numSamples/2]=-1

def sym_square(n,width,c=1.,tweek=0):
	filt=np.zeros(n)
	if n % 2 == 0:
		filt[n/2-(width/2+1)],filt[(n/2+(width/2))]=c/2,c/2
		filt[n/2-(width/2):n/2+(width/2)]=c	
	elif n% 2 != 0:
		filt[n/2+1]=c
		filt[n/2-(width/2+1)],filt[(n/2+(width/2))+1]=c/2,c/2
		filt[n/2-(width/2):n/2+(width/2)+1]=c	
	return filt

def sym_tapering_filt(n,dx,width,c=1.,tweek=0):
	filt=np.zeros(n)
	if n % 2 == 0:
		filt[n/2-(width/2+tweek):n/2+(width/2)]=c
		for i in range(dx):
			filt[n/2-(width/2+tweek+i)],filt[n/2+(width/2-1+i)]=(dx-i)*(c/dx),(dx-i)*(c/dx)
	elif n % 2 != 2:
		filt[n/2+1]=c
		filt[n/2-(width/2):n/2+(width/2)+1]=c
		for i in range(dx):
			filt[n/2-(width/2+tweek+i)],filt[n/2+(width/2+i)]=(dx-i)*(c/dx),(dx-i)*(c/dx)
	return filt


#myplot(np.arange(1,numSamples+1),hn)
#plt.show()

fx2= fx + 0.5*np.cos(10*pi*xx) + (1./3)*np.cos(12*pi*xx)
hn=sym_tapering_filt(numSamples,numSamples/4,2)
fx1=np.fft.ifft(np.fft.fft(fx2)*np.fft.fftshift(hn))

plt.plot(xx,fx1,'b',label='thresholded function')
plt.plot(xx,fx,'r--',label='approximating function')
plt.xlabel('X')
plt.legend()
plt.title('symetric tapering low pass filter on square wave')
print('l2 norm',np.linalg.norm(abs(fx1-fx),2))

print('inf norm',np.linalg.norm(abs(fx1-fx),np.inf))

plt.figure()

hn=sym_square(numSamples,numSamples/4)
fx1=np.fft.ifft(np.fft.fft(fx2)*np.fft.fftshift(hn))

plt.plot(xx,fx1,'b',label='thresholded function')
plt.plot(xx,fx,'r--',label='approximation function')
plt.xlabel('X')
plt.legend()
plt.title('symmetric square low pass filter')
print('l2 norm',np.linalg.norm(abs(fx1-fx),2))

print('inf norm',np.linalg.norm(abs(fx1-fx),np.inf))


plt.figure()
plt.plot(xx,fx2,'b',label='unthresholded function')
plt.plot(xx,fx,'r--',label='approximation function')
plt.xlabel('X')
plt.legend()
plt.title('no filter')
print('l2 norm',np.linalg.norm(abs(fx1-fx),2))

print('inf norm',np.linalg.norm(abs(fx1-fx),np.inf))

plt.show()