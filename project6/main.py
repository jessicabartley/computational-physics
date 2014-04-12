#!/usr/bin/env python

from __future__ import division

from math import cos, sin

DRIVING_FREQENCY = 5
DRIVING_AMPLITUDE = .1
STEP = 0.005  # step forward in time
TIME_STOP = 2000


def add_node_to_the_system(the_system, node):
    """node comes in the form of `(angle, velocity, time)`"""
    a, v, t = node
    the_system.append({'angle': a, 'velocity': v, 'time': t})


def initialize_the_system():
    initial_data = ((0, 0, -STEP), (0, 0, 0))
    initial_system = []
    for node in initial_data:
        add_node_to_the_system(initial_system, node)
    return initial_system


def get_next_angle(angle, velocity, step):
    return 2 * step * velocity + angle


def get_next_velocity(time, angle, velocity, step, amplitude, frequency):
    return 2 * step * (
        -sin(angle) + amplitude * cos(frequency * time)
    ) + velocity


def drive_the_system(iterations, step, amplitude, frequency):
    # Represent the system data structure as
    # [{'angle': x, 'velocity': y, 'time': z}, ...]
    the_system = initialize_the_system()

    angle1 = the_system[0]['angle']
    angle2 = the_system[1]['angle']
    velocity1 = the_system[0]['velocity']
    velocity2 = the_system[1]['velocity']

    for i in xrange(1, iterations + 1):
        t = step * i
        next_angle = get_next_angle(angle1, velocity2, step)
        next_velocity = get_next_velocity(
            t, angle2, velocity1, step, amplitude, frequency
        )
        add_node_to_the_system(the_system, (next_angle, next_velocity, t))

        angle1 = angle2
        angle2 = next_angle
        velocity1 = velocity2
        velocity2 = next_velocity

    return the_system


def main():
    the_system = drive_the_system(
        TIME_STOP, STEP, DRIVING_AMPLITUDE, DRIVING_FREQENCY
    )
    for node in the_system:
        print(node['time']),
        print(node['angle']),
        print(node['velocity'])


if __name__ == '__main__':
    main()
