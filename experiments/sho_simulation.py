#This is the file i will be using to simulate stuffs

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
"""this will allow me to import from core and systems directories"""




import numpy as np
import matplotlib.pyplot as plt

from core.integrators import euler_step
from systems.harmonic_oscillator import sho_dynamics

# Simulation parameters
dt = 0.1
t_max = 20.0
omega = 1.0

# Initial state (position=1, velocity=0)
state = np.array([1.0, 0.0])

states = []
times = []

t = 0.0
while t < t_max:
    states.append(state.copy())
    times.append(t)
    state = euler_step(
        lambda x, t: sho_dynamics(x, t, omega),
        state, t, dt
    )
    t += dt

states = np.array(states)

# Plotting
plt.plot(times, states[:, 0], label="Position")
plt.plot(times, states[:, 1], label="Velocity")
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Simple Harmonic Oscillator (Euler Integration)")
plt.legend()
plt.show()
