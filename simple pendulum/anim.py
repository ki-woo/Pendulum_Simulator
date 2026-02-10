import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math as m

def f_p(v):
    return v

def f_v(p):
    return -(g / l) * m.sin(p)

def RK4(p, v):
    k1_p = f_p(v) * h
    k1_v = f_v(p) * h

    k2_p = f_p(v + k1_v / 2) * h
    k2_v = f_v(p + k1_p / 2) * h

    k3_p = f_p(v + k2_v / 2) * h
    k3_v = f_v(p + k2_p / 2) * h

    k4_p = f_p(v + k3_v) * h
    k4_v = f_v(p + k3_p) * h

    return [p + (k1_p + (2 * k2_p) + (2 * k3_p) + k4_p) / 6,
            v + (k1_v + (2 * k2_v) + (2 * k3_v) + k4_v) / 6]

# 초기값
g = 9.8
l = 1
h = 0.01

p_0 = 1/4 * m.pi
v_0 = 0

t = np.arange(0, 10, h)
p = np.array([])

for i in t:
    result = RK4(p_0, v_0)
    p_0 = result[0]
    v_0 = result[1]
    p = np.append(p, p_0)


## 그래프
fig, axis = plt.subplots(1, 2, figsize=(10,4))

axis[0].set_xlim([l * -1 - 0.25, l + 0.25])
axis[0].set_ylim([l * -1 - 0.25, l + 0.25])
axis[0].grid()
axis[0].set_aspect(1)

axis[1].set_xlim([min(t), max(t)])
axis[1].set_ylim([min(p) - 1, max(p) + 1])
axis[1].grid()

animated_string, = axis[0].plot([], [], color = 'blue')
animated_mass, = axis[0].plot([], [], 'o', markersize = 20, color = 'red')
animated_graph, = axis[1].plot([], [])

def update(frame):
    animated_string.set_data([0, l * np.sin(p[frame])], [0, l * -np.cos(p[frame])])
    animated_mass.set_data([l * np.sin(p[frame])], [l * -np.cos(p[frame])])

    animated_graph.set_data(t[:frame], p[:frame])

    return animated_graph, animated_string, animated_mass

animation = FuncAnimation(fig= fig, func=update, frames=len(t), interval = h * 1000)

# animation.save("./python/simple pendulum/animation.mp4")

plt.show()
