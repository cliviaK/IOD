import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

def f(x):
    return x**2

x = np.arange(-10, 11, 1)
y = f(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()

print('f(2) = ', f(2))
print('f(5) = ', f(5))
print('f(-3) = ', f(-3))

def integral(startX, endX, numberOfRectangles):
    width = (float(endX) - float(startX))/ numberOfRectangles
    totalArea = 0
    for i in range(numberOfRectangles):
        height = f(startX + i* width)
        area = width * height
        totalArea += area
    return totalArea

print(integral(2.0,4.0,10))
