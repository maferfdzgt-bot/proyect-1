import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 10, 200)

x = np.cos(t)
y = np.sin(t)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

ax.scatter(0, 0)

point, = ax.plot([], [], 'o')

def update(frame):
     point.set_data(x[frame], y[frame])
     return point,

ani = FuncAnimation(fig, update, frames=len(t), interval=50)

plt.title("Órbita animada 🚀")
plt.show()

