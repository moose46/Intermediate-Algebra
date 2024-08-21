import numpy as np
from contourpy import LineType
from matplotlib import pyplot as plt
from matplotlib.lines import lineStyles

# figure 3
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
plt.grid("x")
plt.show()


# Example 1
def point(x: float, y: float):
    """put a point on the grid with a label"""
    plt.plot(x, y, "ob")
    plt.text(x, y, f"({x},{y})")


def drawAxis():
    """Draw a red x and y axis 5 points each way"""
    plt.plot([0, 0], [0, -5], color="red")
    plt.plot([0, 0], [0, 5], color="red")
    plt.plot([0, -5], [0, 0], color="red")
    plt.plot([0, 5], [0, 0], color="red")


plt.plot(4, 1, "ob")
plt.text(4, 1, "(4,1)")
plt.plot(-4, 2, "ob")
plt.text(-4, 2, "(-4,2)")
cx = -2
cy = -3
plt.plot(cx, cy, "ob")
plt.text(cx, cy, f"({cx},{cy})")
dx = 2
dy = -5
plt.plot(dx, dy, "ob")
plt.text(dx, dy, f"({dx},{dy})")
point(2, 0)
point(-3 / 2, 0)
point(0, 5)
point(0, 0)
plt.grid(axis="both", linestyle="--")
drawAxis()
plt.show()
