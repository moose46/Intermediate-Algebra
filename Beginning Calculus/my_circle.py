# Program to plot a Circle
# using Parametric equation of a Circle

import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi, 150)
print(type(theta))
print(theta)
radius = 0.4

a = radius * np.c
os(theta)
b = radius * np.sin(theta)

figure, axes = plt.subplots(1)

axes.plot(a, b)
axes.set_aspect(1)

plt.title("Parametric Equation Circle")
plt.show()
