import numpy as np
from sys import stdout

def transition_probability(energy, energy_new, T):
    """Returns the transition probability given the energy of two
    states and the current temperature.
    """
    if energy_new < energy:
        return 1.0
    else:
        return np.exp(-(energy_new - energy) / T)
        

def temperature_cauchy(k, T0):
    """Cauchy schedule to update tempertature at step k.
    """
    T_new = T0 / (1 + k)
    return T_new


def temperature_boltzmann(k, T0):
    """Boltzmann schedule to update tempertature at step k.
    """
    T_new = T0 / np.log(1 + k+1)
    return T_new


def anneal(initial_state, energy_function, neighbour, transition_probability, temperature, max_steps, energy_max, T0, log_every=1000, args=[]):
    """Simulated annealing optimization.

    initial_state
    energy_function
    neighbour
    transition_probability
    temperature
    max_steps
    energy_max
    """
    state = initial_state
    energy = energy_function(state, *args)
    state_best = state
    energy_best = energy
    energy_old = energy
    k = 0
    print "Step) Energy \t Prob. \t Temp. \t (E'-E) \t BEST"
    while k < max_steps and energy > energy_max:
        T = temperature(k, T0)
        state_new = neighbour(state)
        energy_new = energy_function(state_new, *args)
        p = transition_probability(energy, energy_new, T)
        if p > np.random.rand():
            state = state_new
            energy_old = energy
            energy = energy_new
        if energy_new < energy_best:
            state_best = state_new
            energy_best = energy_new
            print "* %s) %s \t %s \t %s \t %s \t %s" % (k, energy_best, p, T, energy_old, energy_new)

        if (k % log_every) == 0:
            print "%s) %s \t %s \t %s \t %s \t %s" % (k, energy, p, T, energy_new - energy_old, energy_best)
            stdout.flush()
            
        k += 1

    return state_best, energy_best
        
