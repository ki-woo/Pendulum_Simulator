# Pendulum Simulator

**Kiwoo** | Pendulum Simulator (to learn Lagrangian and RK4)

Date : **Nov20-28 2025** (9 days)

Assist: **BaumKim**


## 개발 동기
- 심심해서
- 라그랑지안 배워보려고

## 설명
- 진자운동을 시뮬레이션하는 프로그램입니다.
- 단진자, 이중진자, 탄성진자가 있습니다.
- 초기상태는 코드를 직접 수정해서 입력해야 합니다.
- matplotlib animation 저장경로를 설정해 주어야 합니다. (기본적으로 주석처리 되어있음)
- 사용된 라이브러리는 numpy, matplotlib만 존재합니다.
- 개인적으로 만든거라 코드가 깔끔하지 않습니다.

## 원리

- **오일러-라그랑주 방정식** (Euler-Lagrange Equation)
    ---
    
    오일러-라그랑주 방정식을 쓰면 스칼라인 에너지를 사용해 물체의 운동을 기술할 수 있기에 사용되었다.

    Formula:

    $\mathcal{L}≡T−U$
    
    - $\mathcal{L}$ is Lagrangian.
    - $T$ is Kinetic energy.
    - $U$ is Potential energy.

    $\frac{\partial \mathcal{L}}{\partial x_i} - \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{x}_i} = 0$

    - $x_i$ is generalized coordinates.
    - $\dot{x}_i = \frac{d}{dt}x_i \\ \ddot{x}_i = \frac{d^2}{dt^2}x_i$


- **룽게-쿠타 방법** (Runge-Kutta Method)
    ---

    물체의 복잡한 운동을 근사시키기 위해 RK4가 사용되었다.

    Formula:

    
    $\frac{dy}{dt} = f(t,y)$ \
    $y(t_0) = y_0$
    

    $k_1 = f(t_n,                \ y_n                   )$ \
    $k_2 = f(t_n + \frac{h}{2},  \ y_n + h\frac{k_1}{2}  )$ \
    $k_3 = f(t_n + \frac{h}{2},  \ y_n + h\frac{k_2}{2}  )$ \
    $k_4 = f(t_n + h,            \ y_n + hk_3            )$
    
    $y_{n + 1} = y_n + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4)$ \
    $t_{n + 1} = t_n + h$

    - $h$ is interval. \
    - $t_0$ and $y_0$ is initial condition.

- **단진자** (Simple Pendulum)
    ---

    진자를 계산할 때는 편의를 위해 극좌표를 사용한다.

    **Simple pedulum** motion equation:

    $\frac{d^2\theta}{dt^2} = -\frac{g}{l}\sin\theta$

    - *It is sencond-order differential equation.*

    \
    But the RK4 only works for **first-order differential equations**.

    Therefore, the equation must be converted into a system of first-order differential equations.

    Converted equation:

    
    $\theta' = v$ \
    $v' = -\frac{g}{l}\sin\theta$
    
    
    - $v$ is angular velocity.
    - $X'$ mean $\frac{d}{dt}X$

    \
    Applying **RK4**:

    $\frac{d\theta}{dt} = f_{\theta}(t,\ \theta,\ v) = v$ \
    $\frac{dv}{dt} = f_{v}(t,\ \theta,\ v) = -\frac{g}{l}\sin\theta$

    $k_{v1} = f_{\theta}(t_n,                \ \theta_n,                     \ v_n                       )$ \
    $k_{v2} = f_{\theta}(t_n + \frac{h}{2},  \ \theta_n + h\frac{k_{v1}}{2}, \ v_n + h\frac{k_{a1}}{2}   )$ \
    $k_{v3} = f_{\theta}(t_n + \frac{h}{2},  \ \theta_n + h\frac{k_{v2}}{2}, \ v_n + h\frac{k_{a2}}{2}   )$ \
    $k_{v4} = f_{\theta}(t_n + h,            \ \theta_n + hk_{v3},           \ v_n + hk_{a3}             )$

    $k_{a1} = f_v(t_n,                \ \theta_n,                     \ v_n                       )$ \
    $k_{a2} = f_v(t_n + \frac{h}{2},  \ \theta_n + h\frac{k_{v1}}{2}, \ v_n + h\frac{k_{a1}}{2}   )$ \
    $k_{a3} = f_v(t_n + \frac{h}{2},  \ \theta_n + h\frac{k_{v2}}{2}, \ v_n + h\frac{k_{a2}}{2}   )$ \
    $k_{a4} = f_v(t_n + h,            \ \theta_n + hk_{v3},           \ v_n + hk_{a3}             )$

    $\theta_{n + 1} = \theta_n + \frac{h}{6} (k_{v1} + 2k_{v2} + 2k_{v3} + k_{v4})$ \
    $v_{n + 1} = v_n + \frac{h}{6} (k_{a1} + 2k_{a2} + 2k_{a3} + k_{a4})$ \
    $t_{n + 1} = t_n + h$

    - 코드에서 $t$나 $k_v$에서의 $\theta$, $k_a$에서의 $v$는 사용되지 않아 매개변수에서 삭제되었다.
    - 또한 $h$는 미리 $k$에 곱했다.

    \
    Transforming to **Cartesian coordinates**:
    
    $x_n = l\sin\theta_n$ \
    $y_n = -l\cos\theta_n$

    ---
    
    | 기호      |물리량                      | 변수/상수 |
    | -         | -                         | :-:      |
    | $\theta$  | Angle                     | Variable |
    | $l$       | String Length             | Constant |
    | $m$       | Mass                      | Constant |
    | $g$       | Gravitational Constant    | Constant |


- **이중진자** (Double Pendulum)
    ---
    The variable are set to $\theta_1$, $\theta_2$.
    
    **Positions and Velocities**:

    $P_1(l_1 \sin \theta_1,\ -l_1 \cos \theta_1)$ \
    $V_1(l_1 \cos \theta_1 \dot{\theta}_1,\ l_1 \sin \theta_1 \dot{\theta}_1)$
    
    $P_2(l_1 \sin \theta_1 + l_2 \sin \theta_2,\ -l_1 \cos \theta_1,\ -l_2 \cos \theta_2)$ \
    $V_2(l_1 \cos \theta_1 \dot{\theta}_1 + l_2 \cos \theta_2 \dot{\theta}_2,\ l_1 \sin \theta_1 \dot{\theta}_1,\ l_2 \sin \theta_2 \dot{\theta}_2)$

    - $P$ is position (Cartesian coordinates)
    - $V$ is velocity

    \
    **Lagrangian**:
    
    $T_1 = \frac{1}{2}m_1(l_1^2 \dot{\theta}_1^2)$ \
    $T_2 = \frac{1}{2}m_2(l_1^2 \dot{\theta}_1^2 + l_2^2 \dot{\theta}_2^2 + 2 l_1 l_2 \dot{\theta}_1 \dot{\theta}_2 \cos(\theta_1 - \theta_2))$ \
    $U_1 = -m_1 g l_1 \cos \theta_1$ \
    $U_2 = -m_2 g (l_1 \cos \theta_1 + l_2 \cos \theta_2)$

    - $T = \frac{1}{2}mv^2$
    - $U = mgh$

    $\mathcal{L} = T_1 + T_2 - U_1 - U_2$ \
    $\ \ \ \ = \frac{1}{2}m_1(l_1^2 \dot{\theta}_1^2) + \frac{1}{2}m_2(l_1^2 \dot{\theta}_1^2 + l_2^2 \dot{\theta}_2^2 + 2 l_1 l_2 \dot{\theta}_1 \dot{\theta}_2 \cos(\theta_1 - \theta_2)) + m_1 g l_1 \cos \theta_1 + m_2 g (l_1 \cos \theta_1 + l_2 \cos \theta_2)$

    \
    Substitute into the **Euler-Lagrange equation**:

    $\theta_1 : \frac{\partial \mathcal{L}}{\partial \theta_1} - \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{\theta}_1} = 0$ \
    $\theta_2 : \frac{\partial \mathcal{L}}{\partial \theta_2} - \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{\theta}_2} = 0$

    $\theta_1 : (m_1 + m_2) l_1^2 \ddot{\theta}_1 + m_2 l_1 l_2 \cos (\theta_1 - \theta_2) \ddot{\theta}_2 + (m_1 + m_2) g l_1 \sin \theta_1 + m_2 l_1 l_2 \dot{\theta}_2^2 \sin (\theta_1 - \theta_2) = 0$ \
    $\theta_2 : m_2 l_1 l_2 \cos (\theta_1 - \theta_2) \ddot{\theta}_1 + m_2 l_2^2 \ddot{\theta}_2 - m_2 l_1 l_2 \dot{\theta}_1^2 \sin (\theta_1 - \theta_2) + m_2 g l_2 \sin \theta_2 = 0$

    \
    Solution to the simultaneous equation:

    $A = (m_1 + m_2) l_1^2$ \
    $B = m_2 l_1 l_2 \cos (\theta_1 - \theta_2)$ \
    $C = -(m_1 + m_2) g l_1 \sin \theta_1 - m_2 l_1 l_2 \dot{\theta}_2^2 \sin (\theta_1 - \theta_2)$ \
    $D = m_2 l_2^2$ \
    $E = m_2 l_1 l_2 \dot{\theta}_1^2 \sin (\theta_1 - \theta_2) - m_2 g l_2 \sin \theta_2$

    $A\ddot{\theta}_1 + B\ddot{\theta}_2 = C$ \
    $B\ddot{\theta}_1 + D\ddot{\theta}_2 = E$

    $\ddot{\theta}_1 = \frac{BE - DC}{B^2 - AD}$ \
    $\ddot{\theta}_2 = \frac{BC - AE}{B^2 - AD}$

    \
    이후 과정은 단진자에서처럼 RK4에 적용하고 좌표변환을 하면 된다.

    ---
    
    | 기호          |물리량                              | 변수/상수 |
    | -             | -                                 | :-:      |
    | $\theta_1$    | **Angle** (First Object)          | Variable |
    | $\theta_2$    | **Angle** (Second Object)         | Variable |
    | $l_1$         | **String Length** (First Object)  | Constant |
    | $l_2$         | **String Length** (Second Object) | Constant |
    | $m_1$         | **Mass** (First Object)           | Constant |
    | $m_2$         | **Mass** (Second Object)          | Constant |
    | $g$           | **Gravitational Constant**        | Constant |
    
    

- **탄성진자** (Elastic Pendulum)
    ---

    The variable are set to $\theta$, $r$.
    
    **Positions and Velocities**:

    $P(r \sin \theta,\ -r \cos \theta)$ \
    $V(\dot{r}\sin \theta + r\cos \theta \ \dot{\theta},\ -\dot{r}\cos \theta + r\sin \theta \ \dot{\theta})$

    - $P$ is position (Cartesian coordinates)
    - $V$ is velocity

    \
    **Lagrangian**:
    
    $T = \frac{1}{2}m(\dot{r}^2 + r^2 \dot{\theta}^2)$ \
    $U = \frac{1}{2}k(r - r_0)^2 - mgr \cos \theta$

    - $T = \frac{1}{2}mv^2$
    - $U = \frac{1}{2}kx^2 + mgh$

    $\mathcal{L} = T - U$ \
    $\ \ \ \ = \frac{1}{2}m(\dot{r}^2 + r^2 \dot{\theta}^2) - \frac{1}{2}k(r - r_0)^2 + mgr \cos \theta$

    \
    Substitute into the **Euler-Lagrange equation**:

    $\theta : \frac{\partial \mathcal{L}}{\partial \theta} - \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{\theta}} = 0$ \
    $r : \frac{\partial \mathcal{L}}{\partial r} - \frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{r}} = 0$

    $\theta : g \sin \theta + 2 \dot{r} \dot{\theta} + r \ddot{\theta} = 0$ \
    $r : r\dot{\theta}^2 - \frac{k}{m}(r - r_0) + g \cos \theta - \ddot{r} = 0$    

    \
    Solution to the simultaneous equation:

    $\ddot{\theta} = -\frac{1}{r}(g \sin \theta + 2 \dot{r} \dot{\theta})$ \
    $\ddot{r} = r\dot{\theta}^2 - \frac{k}{m}(r - r_0) + g \cos \theta$

    \
    이후 과정은 단진자에서처럼 RK4에 적용하고 좌표변환을 하면 된다.

    ---
    
    | 기호      |물리량                          | 변수/상수 |
    | -         | -                             | :-:      |
    | $\theta$  | **Angle**                     | Variable |
    | $r$       | **String Length**             | Variable |
    | $r_0$     | **Original String Length**    | Constant |
    | $m$       | **Mass**                      | Constant |
    | $g$       | **Gravitational Constant**    | Constant |
    | $k$       | **Elastic Modulus**           | Constant |
