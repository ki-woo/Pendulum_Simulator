import numpy as np
import matplotlib.pyplot as plt
import math as m

g = 9.8 # 중력가속도
l = 1   # 진자 길이
h = 0.01

t = np.arange(0, 10, h)
p = np.array([])

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
p_0 = 1/6 * m.pi
v_0 = 0

for i in t:
    result = RK4(p_0, v_0)
    p_0 = result[0]
    v_0 = result[1]
    p = np.append(p, p_0)
    
# 그래프
plt.plot(t, p)
plt.title("Simple Pendulum")
plt.xlabel("Time (s)")
plt.ylabel("Angle (Rad)")
plt.show()
