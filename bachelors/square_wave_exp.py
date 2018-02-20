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
def sym_sin_taper_filt(n,dx,width,c=1.,tweek=0):
	filt=np.zeros(n)
	filt[n/2-(width/2+tweek):n/2+(width/2)]=c
	for i in range(dx):
		filt[n/2-(width/2+tweek+i)],filt[n/2+(width/2-1+i)]=c*np.sin(pi*(dx-i)/(2*dx)),c*np.sin(pi*(dx-i)/(2*dx))
	return filt

fx2= fx + 0.5*np.cos(10*pi*xx) + (1./3)*np.cos(12*pi*xx)
taper = 6
hn=sym_tapering_filt(numSamples,((numSamples/4)-taper)/2,taper)
fx1=np.fft.ifft(np.fft.fft(fx2)*np.fft.fftshift(hn))

plt.subplot(211)
plt.plot(xx,fx1,'b',label='thresholded function')
plt.plot(xx,fx,'r--',label='approximating function')
plt.xlabel('X')
plt.legend()
plt.title('symetric tapering low pass filter on square wave')


plt.subplot(223)
myplot(np.fft.fftshift(np.arange(numSamples)), np.fft.fftshift(hn),label='frequency domain')
plt.text(0,-0.3,'Filter in Frequency domain')

plt.subplot(224)
plt.plot(xx,np.fft.fftshift(np.fft.ifft(hn)),label='time domain')
plt.text(-pi,-0.22,'Filter in time domain')

print('tapering filt')
print('l2 norm',np.linalg.norm(abs(fx1-fx),2))
print('inf norm',np.linalg.norm(abs(fx1-fx),np.inf))



plt.figure()

hn=sym_square(numSamples,numSamples/4)
fx1=np.fft.ifft(np.fft.fft(fx2)*np.fft.fftshift(hn))

plt.subplot(211)
plt.plot(xx,fx1,'b',label='thresholded function')
plt.plot(xx,fx,'r--',label='approximation function')
plt.xlabel('X')
plt.legend()
plt.title('symmetric square low pass filter')

plt.subplot(223)
myplot(np.arange(numSamples), hn,label='frequency domain')
plt.text(0,-0.3,'Filter in Frequency domain')

plt.subplot(224)
plt.plot(xx,np.fft.fftshift(np.fft.ifft(hn)),label='time domain')
plt.text(-pi,-0.22,'Filter in time domain')

print('square filt')
print('l2 norm',np.linalg.norm(abs(fx1-fx),2))
print('inf norm',np.linalg.norm(abs(fx1-fx),np.inf))


plt.figure()
taper = 2
hn=sym_sin_taper_filt(numSamples,((numSamples/4)-taper)/2,taper)
fx1=np.fft.ifft(np.fft.fft(fx2)*np.fft.fftshift(hn))

plt.subplot(211)
plt.plot(xx,fx1,'b',label='thresholded function')
plt.plot(xx,fx,'r--',label='approximating function')
plt.xlabel('X')
plt.legend()
plt.title('symetric sin-taper low pass filter on square wave')


plt.subplot(223)
myplot(np.fft.fftshift(np.arange(numSamples)), np.fft.fftshift(hn),label='frequency domain')
plt.text(0,-0.3,'Filter in Frequency domain')

plt.subplot(224)
plt.plot(xx,np.fft.fftshift(np.fft.ifft(hn)),label='time domain')
plt.text(-pi,-0.22,'Filter in time domain')

print('sin-taper filt')
print('l2 norm',np.linalg.norm(abs(fx1-fx),2))
print('inf norm',np.linalg.norm(abs(fx1-fx),np.inf))



plt.figure()
plt.subplot(211)
plt.plot(xx,fx2,'b',label='unthresholded function')
plt.plot(xx,fx,'r--',label='approximation function')
plt.legend()
plt.title('no filter')
plt.subplot(223)
myplot(np.arange(numSamples),1./numSamples*np.fft.fftshift(np.fft.fft(fx2).imag))
plt.text(0,-1,'Function in phase space')
plt.subplot(224)
myplot(np.arange(numSamples),1./numSamples*np.fft.fft(fx2).real)
plt.text(0,-0.175,'Function in freq space')
print('no filter')
print('l2 norm',np.linalg.norm(abs(fx2-fx),2))
print('inf norm',np.linalg.norm(abs(fx2-fx),np.inf))

plt.show()
