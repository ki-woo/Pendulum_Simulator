import numpy as np
import matplotlib.pyplot as plt
import math as m

def f_p(v1, v2):
    return [h * v1, h * v2]

def f_v(p1, p2, v1, v2):
    cos_s = m.cos(p1 - p2)
    sin_s = m.sin(p1 - p2)

    A = (m_1 + m_2) * l_1 ** 2
    B = m_2 * l_1 * l_2 * cos_s
    C = -(m_1 + m_2) * l_1 * g * m.sin(p1) - m_2 * l_1 * l_2 * (v2 ** 2) * sin_s
    D = m_2 * l_2 ** 2
    E = -m_2 * l_2 * g * m.sin(p2)  + m_2 * l_1 * l_2 * (v1 ** 2) * sin_s

    M = (B ** 2) - A * D

    return [h * (B * E - C * D) / M, h * (B * C - A * E) / M]

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

m_1 = 1
l_1 = 1
p_1 = 1/4 * m.pi
v_1 = 0

m_2 = 1
l_2 = 1
p_2 = 1/4 * m.pi
v_2 = 0

t = np.arange(0, 10, h)
p1 = np.array([])
p2 = np.array([])

for i in t:
    result = RK4(p_1, p_2, v_1, v_2)
    p_1 = result[0]
    p_2 = result[1]
    v_1 = result[2]
    v_2 = result[3]
    p1 = np.append(p1, p_1)
    p2 = np.append(p2, p_2)
    
# 그래프
plt.plot(t, p1)
plt.plot(t, p2)
plt.title("Double Pendulum")
plt.xlabel("Time (s)")
plt.ylabel("Angle (Rad)")
plt.show()
