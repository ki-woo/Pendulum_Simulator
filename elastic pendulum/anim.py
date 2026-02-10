import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math as ma

def f_p(v1, v2):
    return [h * v1, h * v2]

def f_v(r, a, rv, av):
    rr = r * av ** 2 - k * (r - r0) / m + g * ma.cos(a)
    pp = -g * ma.sin(a) - 2 * rv * av

    return [rr * h, pp * h]

def RK4(p1, p2, v1, v2):
    k1_p = f_p(v1, v2)
    k1_v = f_v(p1, p2, v1, v2)

    k2_p = f_p(v1 + k1_v[0] / 2, v2 + k1_v[1] / 2)
    k2_v = f_v(p1 + k1_p[0] / 2, p2 + k1_p[1] / 2, v1 + k1_v[0] / 2, v2 + k1_v[1] / 2)

    k3_p = f_p(v1 + k2_v[0] / 2, v2 + k2_v[1] / 2)
    k3_v = f_v(p1 + k2_p[0] / 2, p2 + k2_p[1] / 2, v1 + k2_v[0] / 2, v2 + k2_v[1] / 2)

    k4_p = f_p(v1 + k3_v[0], v2 + k3_v[1])
    k4_v = f_v(p1 + k3_p[0], p2 + k3_p[1], v1 + k3_v[0], v2 + k3_v[1])

    return [p1 + (k1_p[0] + (2 * k2_p[0]) + (2 * k3_p[0]) + k4_p[0]) / 6,
            p2 + (k1_p[1] + (2 * k2_p[1]) + (2 * k3_p[1]) + k4_p[1]) / 6,
            v1 + (k1_v[0] + (2 * k2_v[0]) + (2 * k3_v[0]) + k4_v[0]) / 6,
            v2 + (k1_v[1] + (2 * k2_v[1]) + (2 * k3_v[1]) + k4_v[1]) / 6]

# 초기값
g = 9.8
h = 0.01

m = 1
r0 = 1

k = 50

r = 1
a = 1/2 * ma.pi
rv = 0
av = 0

t = np.arange(0, 10, h)
r_arr = np.array([])
a_arr = np.array([])

for i in t:
    result = RK4(r, a, rv, av)
    r = result[0]
    a = result[1]
    rv = result[2]
    av = result[3]
    r_arr = np.append(r_arr, r)
    a_arr = np.append(a_arr, a)


## 그래프
fig, axes = plt.subplots()

axes.set_xlim([r0 * -2 - 0.25, r0 * 2 + 0.25])
axes.set_ylim([r0 * -2 - 0.25, r0 * 2 + 0.25])
axes.grid()
axes.set_aspect(1)

animated_trajectory, = axes.plot([], [], markersize = 0.5, color = 'cyan')
animated_string, = axes.plot([], [], color = 'blue')
animated_mass, = axes.plot([], [], 'o', markersize = 10, color = 'red')

def update(frame):
    animated_trajectory.set_data([r_arr[:frame] * np.sin(a_arr[:frame])], [r_arr[:frame] * -np.cos(a_arr[:frame])])
    animated_string.set_data([0, r_arr[frame] * np.sin(a_arr[frame])], [0, r_arr[frame] * -np.cos(a_arr[frame])])
    animated_mass.set_data([r_arr[frame] * np.sin(a_arr[frame])], [r_arr[frame] * -np.cos(a_arr[frame])])

    animated_string.set_linewidth(r0 * 2 / r_arr[frame])

    return animated_string, animated_mass, animated_trajectory

animation = FuncAnimation(fig= fig, func=update, frames=len(t), interval = h * 1000)

# animation.save("./python/elastic pendulum/animation2.mp4")

plt.show()
