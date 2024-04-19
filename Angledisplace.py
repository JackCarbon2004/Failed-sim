import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



#defining the function
def pendulum_eq(y, t, l, g, lam):
    theta, omega = y
    dydt = [omega, -lam*omega - (g/l)*np.sin(theta) + 2*np.sin(t)]
    return dydt

def solve_pendulum(l, g, lam, t):
    y0 = [1, 0]  # initial conditions
    sol = odeint(pendulum_eq, y0, t, args=(l, g, lam))
    return sol

#parameters 
g = 9.81  # acceleration due to gravity
lam = 0   # moment of inertia
t = np.linspace(0, 30, 1000)  # time array



lengths = [4, 8, 10, 15]  # pendulum lengths to test

#plots

plt.figure(figsize=(8, 6))

for l in lengths:
    sol = solve_pendulum(l, g, lam, t)
    plt.plot(t, sol[:, 0], label=f'l = {l}')

plt.xlabel('Time')
plt.ylabel('Angular Displacement')
plt.legend()
plt.grid()
plt.show()