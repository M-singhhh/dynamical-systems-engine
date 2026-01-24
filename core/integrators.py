#In this file i will do numerics related work and particularly in integrators.py i will do intregators work

import numpy as np

def euler_step(f, x, t, dt):
    """
    Simple Euler integration:
    x_{n+1} = x_n + dt * f(x_n, t_n)
    """
    return x + dt * f(x, t)
