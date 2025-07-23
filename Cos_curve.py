import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-10,10,0.01)
y = np.cos(x)
plt.plot(x,y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Cos Curve.')
plt.grid()
plt.show()