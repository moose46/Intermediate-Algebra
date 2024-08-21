import numpy as np
from contourpy import LineType
from matplotlib import pyplot as plt
from matplotlib.lines import lineStyles

t = np.arange(0.0, 3.0, 0.2)
for x in t:
    print(x)
A = -4, 3
B = 3, 2, -5 / 2
plt.plot(-4, 3, "or")
plt.plot([-4, -4, -4, 0], [3, 0, 3, 3], "b--")
plt.plot([3, 0, 3, 3], [2, 2, 2, 0], "g--")
plt.text(-4, 3, "(-4,3)")
plt.plot(3, 2, "or")
plt.plot(3, 2, "ob")
plt.text(3, 2, "(3,2)")
plt.plot(0, -5 / 2, "og")
plt.text(0, -5 / 2, "(0,-5/2)")
plt.text(0, 0, "(0,0)")
plt.plot([0, 0], [0, -5], color="red")
plt.plot([0, 0], [0, 5], color="red")
plt.plot([0, -5], [0, 0], color="red")
plt.plot([0, 5], [0, 0], color="red")
plt.grid()
plt.show()
