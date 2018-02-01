import numpy as np 
xx=np.linspace(-3./8,0.5,8)
fftfx=np.fft.fft(np.fft.fftshift(xx))
xxav=np.linspace(-3./8,0.5,8)
xxav[7]=0
fftfxav=np.fft.fft(np.hstack((xxav[3:],xxav[:3])))
for i in range(len(xxav)):
	print(xxav[i], np.fft.fftshift(1./8*fftfxav)[i-3])

for i in range(len(xx)):
	print(xx[i],1./8*np.fft.fftshift(fftfx)[i-3])