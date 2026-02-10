import numpy as np
import matplotlib.pyplot as plt
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
a = 1/4 * ma.pi
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
    
# 그래프
fig = plt.figure(figsize=(15,5))

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(t, r_arr)
ax1.set_title("Elastic Pendulum Length")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Length (m)")

ax2.plot(t, a_arr)
ax2.set_title("Elastic Pendulum Angle")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Angle (Rad)")

plt.show()
