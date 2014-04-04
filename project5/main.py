#!/usr/bin/env python
from __future__ import division, print_function

from math import exp
from random import random
import argparse
import os

# For this project we're assuming the box has a edge length of 1

BETA = 4
BOX_LENGTH = 1
EPSILON = 0.2


class ThreeD(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def tuple(self):
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
        return .5 * sum(map(lambda x: x ** 2, self.momentum.tuple))

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


def randomly_vary_numbers(numbers):
    new_numbers = []
    for n in numbers:
        n = n + (random() - .5) * EPSILON
        # Take into consideration cube boundaries
        n = min(n, BOX_LENGTH)
        n = max(n, 0)
        new_numbers.append(n)
    return tuple(new_numbers)


def create_trial_molecule(molecule):
    new_position = Position(
        *randomly_vary_numbers(molecule.position.tuple)
    )
    new_momentum = Momentum(
        *randomly_vary_numbers(molecule.momentum.tuple)
    )
    return Molecule(new_position, new_momentum)


def has_greater_energy(trial_molecule, molecule):
    return trial_molecule.total_energy >= molecule.total_energy


def calculate_total_energy_for(ensemble):
    total_energy = 0
    for molecule in ensemble:
        total_energy += molecule.total_energy
    return total_energy


def get_probability_distribution(ensemble):
    return exp(-BETA * calculate_total_energy_for(ensemble))


def feeling_lucky(ensemble, trial_molecule, molecule):
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
    if feeling_lucky(ensemble, trial_molecule, molecule):
        return trial_molecule
    return molecule


def sweep(ensemble):
    new_ensemble = []
    for molecule in ensemble:
        new_ensemble.append(keep_or_replace_molecule(ensemble, molecule))
    return new_ensemble


def setup_parser():
    """
    Setup the command line utility.
    """
    desc = (
        'Deriving the equilibrium energy of an ideal gas using markov chains'
    )
    parser = argparse.ArgumentParser(
        description=desc,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-n', '--molecules', metavar='NO_OF_MOLECULES', type=int, default=10,
        dest='no_of_molecules', help='the number of molecules in the system'
    )
    parser.add_argument(
        '-i', '--iterations', metavar='ITERATIONS', type=int,
        default=1000, help='the number of sweeps'
    )
    parser.add_argument(
        '-o', '--output', metavar='FILENAME', default=os.devnull,
        help='the output file of the result'
    )
    return parser


def output(content, file):
    print(content)
    print(content, file=file)


def main():
    parser = setup_parser()
    args = parser.parse_args()

    ensemble = create_initial_ensemble(args.no_of_molecules)
    with open(args.output, 'w+') as of:
        output(calculate_total_energy_for(ensemble), of)
        for i in xrange(args.iterations):
            ensemble = sweep(ensemble)
            output(calculate_total_energy_for(ensemble), of)


if __name__ == '__main__':
    main()
