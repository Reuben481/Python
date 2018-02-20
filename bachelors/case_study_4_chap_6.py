import numpy as np
import numpy.fft as fft
from myplot import myplot
from matplotlib import pyplot as plt
pi=np.pi

#A*omega=N
#domega*dx=1/N

N=128
A=8
omega=N/A

#domega=1/A
#dx=A/N

xax=np.linspace(-A/2,A/2,N)
omegax=np.linspace(-omega/2,omega/2,omega*A)

#---------------------------------

hn=np.zeros(len(omegax))
hn[np.argmin(abs(omegax+1)):np.argmin(abs(omegax-1))]=1
hnprime=2*np.sinc(2*xax)



plt.subplot(221)
plt.plot(xax,fft.fftshift(fft.ifft(hn)))

plt.subplot(222)
myplot(omegax,hn)

plt.subplot(223)
plt.plot(xax,hnprime)

plt.subplot(224)
myplot(omegax,float(A)/N*abs(fft.fftshift(fft.fft(hnprime))))

plt.show()
