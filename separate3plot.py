import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(0, 1, 0.001)

plt.figure()

plt.subplot(4, 1, 1)
y1 =  3 + 2*np.cos(2 * np.pi * x * 4 + 0)
plt.plot(x ,y1)

plt.subplot(4, 1, 2)
y2 =  0 + 1*np.cos(2 * np.pi * x * 5 + np.pi/6)
plt.plot(x ,y2)

plt.subplot(4, 1, 3)
y3 = -1 + 5*np.cos(2 * np.pi * x * 7 - np.pi/4)
plt.plot(x ,y3)

plt.subplot(4, 1, 4)
y = y1+y2+y3
plt.plot(x,y)
plt.tight_layout()

plt.grid()
plt.show()
