import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(0, 1, 0.001)

y1 =  3 + 2*np.cos(2 * np.pi * x * 4)
y2 =  0 + 1*np.cos(2 * np.pi * x * 5 + np.pi/6)
y3 = -1 + 5*np.cos(2 * np.pi * x * 7 - np.pi/4)

y = y1+y2+y3

plt.plot(x ,y)
plt.grid()
plt.show()
