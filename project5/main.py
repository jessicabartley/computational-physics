#!/usr/bin/env python
from __future__ import division, print_function

from collections import namedtuple
from math import exp
from random import random
import argparse

# For this project we're assuming the box has a edge length of 1

BETA = 4
BOX_LENGTH = 1
EPSILON = 0.2


Position = namedtuple('Position', 'x y z')
Momentum = namedtuple('Momentum', 'x y z')


class Molecule(object):
    def __init__(self, position, momentum):
        self.position = position
        self.momentum = momentum

    @property
    def kinetic_energy(self):
        return .5 * sum(map(lambda x: x ** 2, self.momentum))

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
        *randomly_vary_numbers(molecule.position)
    )
    new_momentum = Momentum(
        *randomly_vary_numbers(molecule.momentum)
    )
    return Molecule(new_position, new_momentum)


def has_greater_energy(trial_molecule, molecule):
    return trial_molecule.total_energy >= molecule.total_energy


def calculate_total_energy_for(ensemble):
    total_energy = 0
    for molecule in ensemble:
        total_energy += molecule.total_energy
    return total_energy


def get_probability_distribution(molecule):
    # We can simplify this to molecular level, since we're only tweaking one
    # molecule at a time.
    return exp(-BETA * molecule.total_energy)


def feeling_lucky(trial_molecule, molecule):
    current_p = get_probability_distribution(molecule)
    trial_p = get_probability_distribution(trial_molecule)
    if current_p:
        return current_p / trial_p >= random()
    else:
        return False


def keep_or_replace_molecule(molecule):
    trial_molecule = create_trial_molecule(molecule)
    if has_greater_energy(trial_molecule, molecule):
        return trial_molecule
    if feeling_lucky(trial_molecule, molecule):
        return trial_molecule
    return molecule


def sweep(ensemble):
    new_ensemble = []
    for molecule in ensemble:
        new_ensemble.append(keep_or_replace_molecule(molecule))
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
    return parser


def main():
    parser = setup_parser()
    args = parser.parse_args()

    ensemble = create_initial_ensemble(args.no_of_molecules)
    print(calculate_total_energy_for(ensemble))
    for i in xrange(args.iterations):
        ensemble = sweep(ensemble)
        print(calculate_total_energy_for(ensemble))


if __name__ == '__main__':
    main()
