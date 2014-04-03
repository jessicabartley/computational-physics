#!/usr/bin/env python
from __future__ import division

from math import exp
from random import random

# For this project we're assuming the box has a edge length of 1

BETA = 4
EPSILON = 0.2
NUMBER_OF_MOLECULES = 10


def create_initial_ensemble(no_molecules):
    x = [0.5, 0.5, 0]   # space
    p = [0, 0, 0]       # momenta
    initial_ensemble = {}
    initial_column = [x[0], x[1], x[2], p[0], p[1], p[2]]
    for i in xrange(no_molecules):
        make_column = {i : initial_column}
        initial_ensemble.update(make_column)
    return initial_ensemble


def get_potential_energy(ensemble):
    potential_energy = 0
    for molecule in ensemble.itervalues():
        potential_energy += molecule[2]
    return potential_energy


def get_kinetic_energy(no_molecules, ensemble):
    kinetic_energy = 0
    for i in xrange(no_molecules):
        kinetic_energy += 0.5 * (ensemble[i][3] ** 2 + ensemble[i][4] ** 2 + ensemble[i][5] ** 2) 
    return kinetic_energy


def generate_trial_column(no_molecules, column_number):
    ensemble = create_initial_ensemble(no_molecules)
    for i in xrange(6):
        ensemble[column_number][i] = ensemble[column_number][i] + (random() - 0.5) * EPSILON
        if ensemble[column_number][i] > 1:
            ensemble[column_number][i] = 1
        if ensemble[column_number][i] < 0:
            ensemble[column_number][i] = 0
    trial_column = ensemble[column_number]
    return trial_column


def compute_hamiltonian(no_molecules, ensemble):
    hamiltonian = get_potential_energy(no_molecules, ensemble) + get_kinetic_energy(no_molecules, ensemble)
    return hamiltonian

def get_probability_distribution(no_molecules, ensemble):
    probability_distribution = exp(-BETA * compute_hamiltonian(no_molecules, ensemble))
    return probability_distribution


def create_updated_ensemble(no_molecules, ensemble):
    ensemble = create_initial_ensemble(no_molecules)
    for i in xrange(no_molecules):
        trial_column = generate_trial_column(no_molecules, i)
        trial_ensemble = ensemble[i][trial_column]
        if get_probability_distribution(no_molecules, trial_ensemble) >= get_probability_distribution(no_molecules, ensemble):
            ensemble = trial_ensemble
        elif get_probability_distribution(no_molecules, trial_ensemble) / get_probability_distribution(no_molecules, ensemble) >= random():
            ensemble = trial_ensemble              
    return ensemble


ensemble = create_initial_ensemble(NUMBER_OF_MOLECULES)
newcolumn = generate_trial_column(NUMBER_OF_MOLECULES, 0)
potential = get_potential_energy(NUMBER_OF_MOLECULES, ensemble)
kinetic = get_kinetic_energy(NUMBER_OF_MOLECULES, ensemble)
H = compute_hamiltonian(NUMBER_OF_MOLECULES, ensemble)
boltzman_dist = get_probability_distribution(NUMBER_OF_MOLECULES, ensemble)
print(newcolumn, potential, kinetic, H, boltzman_dist)