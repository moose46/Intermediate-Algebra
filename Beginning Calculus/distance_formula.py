from cProfile import label
from math import sqrt
from turtle import color

# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from contourpy import LineType
from matplotlib.lines import lineStyles

# 2.2 the distance formula Beginning Calculus Shaum's

p1 = (3.0, 8.0)
p2 = (7.0, 11.0)
X = 0
Y = 1
ax = [3, 7]
ay = [8, 11]


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def distance2(p1, p2, printyn: bool = False):
    dist = sqrt(((p1[X] - p2[X]) ** 2) + ((p1[Y] - p2[Y]) ** 2))
    if printyn:
        print(
            f"the distance between ({p1[0]}, {p1[1]}) and ({p2[0]}, {p2[1]}) is {dist}"
        )

    return dist


def midpoint(x, y, printyn: bool = False):
    """Passed two lists, one x and one y coordinates,returns the midpoint between two points"""
    midx = (x[0] + x[1]) / 2
    midy = (y[0] + y[1]) / 2
    if printyn:
        print(
            f"The midpoint of the segment connecting ({x[0]},{y[0]}) and ({x[1]},{y[1]}) is ({midx}, {midy})"
        )

    return midx, midy


def drawAxis(limit: int = 5):
    """Draw a red x and y axis 5 points each way"""
    plt.plot([0, 0], [0, -limit], color="red")
    plt.plot([0, 0], [0, limit], color="red")
    plt.plot([0, -limit], [0, 0], color="red")
    plt.plot([0, limit], [0, 0], color="red")


midpoint(ax, ay, True)
distance2(p1, p2, printyn=True)
plt.plot(ax, ay)
# for xi, yi in zip(ax, ay):
#     print(f"x={xi}, y={yi}")

# One-liner annotation using list comprehension.
[
    plt.annotate(
        f"({xi}, {yi})",
        (xi, yi),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
    )
    for xi, yi in zip(ax, ay)
]
plt.text(
    (p1[X] + p2[X]) / 2,
    (p1[Y] + p2[Y]) / 2,
    f"len={distance2(p1, p2)} midx={(p1[X] + p2[X]) / 2} midy={(p1[Y] + p2[Y]) / 2}",
)
plt.plot((p1[X] + p2[X]) / 2, (p1[Y] + p2[Y]) / 2, "or")

p3x = [1, 3]
p3y = [7, 5]
midpoint(p3x, p3y, True)
p4x = [-2, 3]
p4y = [5, 3]
midpoint(p4x, p4y, True)
plt.grid()
plt.show()

x = [1, 4, -2, 3, 0, 2, -4]
y = [-1, 4, -2, -3, 2, 0, 1]
l = ["A", "B", "C", "D", "E", "F", "G"]
for xi, yi, li in zip(x, y, l):
    plt.plot(xi + 0.5, yi, "or")
    plt.text(xi, yi, li)
plt.grid()
drawAxis()
plt.show()

# x=y**2 parabola
x = [3, 2, 1, 0, -1, -2, -3]
for xi in x:
    plt.plot(xi, xi * xi, "ro")

plt.grid()
plt.title("parabola")
drawAxis()
plt.show()


# hyperbola
x = [3, 2, 1, 1 / 2, 1 / 3, 1 / 4, -1 / 4, -1 / 3, -1 / 2, -1, -2, -3]
for xi in x:
    plt.plot(xi, xi if xi == 0 else 1 / xi, "bo")
plt.grid()
plt.title("hyperbola")
drawAxis()
plt.show()

c = plt.Circle((0.2, 0.2), 0.2, fill=False, color="r")
fig, ax = plt.subplots()
ax.set_aspect(1)
ax.add_artist(c)
plt.title("My First Circle")
plt.show()
