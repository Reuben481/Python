import numpy as np
import numpy.linalg as LA
from matplotlib import pyplot as plt
from myplot import myplot
from scipy.special import sici
pi=np.pi
numSamples=128
A=10.12
Omega=numSamples/A
xx=np.linspace(-A/2,A/2,numSamples)
omegax=np.linspace(-Omega/2,Omega/2,Omega*A)


g=np.zeros(numSamples)
g[np.argmin(abs(xx+pi)):numSamples/2]=-1
g[numSamples/2:np.argmin(abs(xx-pi))]=1
print(g[numSamples/2])

hn=np.zeros(numSamples)
hn[np.argmin(abs(omegax+1)):np.argmin(abs(omegax-1))]=1
#hn[np.argmin(abs(omegax+1))],hn[np.argmin(abs(omegax-1))]=0.5,0.5


gprime=np.fft.ifft(np.fft.fft(g)*np.fft.fftshift(hn))
gwolf=(sici(2*pi*(pi-xx))[0]+2*sici(2*pi*xx)[0]-sici(2*pi*(pi+xx))[0])/pi


plt.plot(xx,gprime,label='discrete evaluation')
plt.plot(xx,gwolf,'r--',label='analytical evaluation')

plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend()

#Figure plot of square_wave with no aved.



#plt.show()
print(((gwolf-gprime)**2).mean(axis=0))
print(((gprime-g)**2).mean(axis=0))
print(LA.norm(abs(gwolf-gprime),np.inf))
#print(gprime[:numSamples/2],gprime[numSamples/2])


plt.figure()


plt.subplot(221)
plt.plot(xx,abs(np.fft.fftshift(np.fft.ifft(hn))))

plt.subplot(222)
myplot(omegax,hn)

plt.subplot(223)
hnprime=np.sin(2*pi*xx)/(pi*xx)
plt.plot(xx,abs(hnprime))


plt.subplot(224)
myplot(omegax,abs(np.fft.fftshift(np.fft.ifft(hnprime))))

plt.show()