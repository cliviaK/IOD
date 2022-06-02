import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3

print(f(2))
print(f(5))
print(f(-3))

x = np.arange(-10, 11, 1)
print(x)
y = f(x)
print(y)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

def derivative(x):
    delta = 1.0/1000.0
    rise = (f(x + delta)) - f(x)
    slope = rise / delta
    print(delta, rise, slope)
    return slope

print(derivative(3))
x = np.arange(-10,11,1)
y = f(x)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)', color=color)
ax1.plot(x, y, color=color)
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(which='major', axis='both', linestyle='--')

ax2 = ax1.twinx()

z = derivative(x)
color = 'tab:blue'
ax2.set_xlabel('x')
ax2.set_ylabel('derivative(x)', color=color)
ax2.plot(x, z, color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.grid(which='major', axis='both', linestyle='--')

fig.tight_layout() # othwise the right y-lable is slightly clipped
plt.show()