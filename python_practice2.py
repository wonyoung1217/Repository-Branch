import numpy as np
import matplotlib.pyplot as plt

def sinusoid(A, f0, phi, fs, t):
	# 1/fs 간격으로
	t=np.arange(0, t, 1.0/fs)
	
	# 위 아래 둘중 아무거나 사용하면 됨
	# 점 갯수를 fs개로
	# t=np.linspace(0, t, int(fs)) 
	x=A*np.cos(2*np.pi*f0*t*+phi)
	return x
    
# 지속시간 t를 짧게 해야 구불구불이 보인다
sin_A=sinusoid(A=0.8, f0=440, phi=np.pi/2, fs=44100, t=0.005)

plt.plot(sin_A)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()