#!/usr/bin/env python
from __future__ import division

from math import exp
from random import random

# For this project we're assuming the box has a edge length of 1

BETA = 4
EPSILON = 0.2
NUMBER_OF_MOLECULES = 10
NUMBER_OF_SWEEPS = 100000


class ThreeD(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def as_tuple(self):
        return (self.x, self.y, self.z)


class Position(ThreeD):
    pass


class Momentum(ThreeD):
    pass


class Molecule(object):
    def __init__(self, position, momentum):
        self.position = position
        self.momentum = momentum

    @property
    def kinetic_energy(self):
        return .5 * sum(map(lambda x: x ** 2, self.momentum.as_tuple()))

    @property
    def potential_energy(self):
        return self.position.z

    @property
    def total_energy(self):
        return self.kinetic_energy + self.potential_energy


def create_initial_ensemble(no_of_molecules):
    initial_position = Position(0.5, 0.5, 0)
    initial_momentum = Momentum(0, 0, 0)
    return [Molecule(initial_position, initial_momentum)] * no_of_molecules


def calculate_total_energy_for(ensemble):
    total_energy = 0
    for molecule in ensemble:
        total_energy += molecule.total_energy
    return total_energy


def randomly_vary_numbers(numbers):
    # TODO: We need to take into consideration the boundaries
    new_numbers = []
    for n in numbers:
        new_numbers.append(n + (random() - .5) * EPSILON)
    return tuple(new_numbers)


def create_trial_molecule(molecule):
    new_position = Position(
        *randomly_vary_numbers(molecule.position.as_tuple())
    )
    new_momentum = Momentum(
        *randomly_vary_numbers(molecule.momentum.as_tuple())
    )
    return Molecule(new_position, new_momentum)


def has_greater_energy(trial_molecule, molecule):
    return trial_molecule.total_energy >= molecule.total_energy


def get_probability_distribution(ensemble):
    return exp(-BETA * calculate_total_energy_for(ensemble))


def roll_the_dice(ensemble, trial_molecule, molecule):
    index = ensemble.index(molecule)
    trial_ensemble = list(ensemble)  # Copy the original ensemble
    trial_ensemble[index] = trial_molecule
    current_p = get_probability_distribution(ensemble)
    trial_p = get_probability_distribution(trial_ensemble)
    if current_p:
        return trial_p / current_p >= random()
    else:
        return False


def keep_or_replace_molecule(ensemble, molecule):
    trial_molecule = create_trial_molecule(molecule)
    if has_greater_energy(trial_molecule, molecule):
        return trial_molecule
    if roll_the_dice(ensemble, trial_molecule, molecule):
        return trial_molecule
    return molecule


def sweep(ensemble):
    new_ensemble = []
    for molecule in ensemble:
        new_ensemble.append(keep_or_replace_molecule(ensemble, molecule))
    return new_ensemble


def main():
    ensemble = create_initial_ensemble(NUMBER_OF_MOLECULES)
    system_energies = [calculate_total_energy_for(ensemble)]
    for i in xrange(NUMBER_OF_SWEEPS):
        ensemble = sweep(ensemble)
        system_energies.append(calculate_total_energy_for(ensemble))
    print(system_energies)


if __name__ == '__main__':
    main()
