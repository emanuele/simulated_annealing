import numpy as np
from sys import stdout

def anneal(initial_state, energy_function, neighbour, transition_probability, temperature, max_steps, energy_max):
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
    energy = energy_function(state)
    state_best = state
    energy_best = energy
    k = 0
    while k < max_steps and energy > energy_max:
        T = temperature(k, max_steps)
        state_new = neighbour(state)
        energy_new = energy_function(state_new)
        p = transition_probability(energy, energy_new, T)
        if transition_probability(energy, energy_new, T) > np.random.rand():
            state = state_new
            energy = energy_new

        if energy_new < energy_best:
            state_best = state_new
            energy_best = energy_new
            print k, ")", energy_best, p

        # if (k % 1000) == 0:
        #     print k, ")", energy_best, p
        #     stdout.flush()
            
        k += 1

    return state_best, energy_best
        
