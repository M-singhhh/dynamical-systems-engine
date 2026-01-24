#In this file i will do physics related work and particularly in this one i will do harmonic oscillator work
import numpy as np

def sho_dynamics(state, t, omega=1.0):
    """
    Simple Harmonic Oscillator:
    dx/dt = v
    dv/dt = -omega^2 * x
    """
    x, v = state
    dxdt = v
    dvdt = -omega ** 2 * x
    return np.array([dxdt, dvdt])
