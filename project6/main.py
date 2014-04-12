#!/usr/bin/env python

from __future__ import division

from math import cos, sin

DRIVING_FREQENCY = 5
DRIVING_AMPLITUDE = .1
STEP = 0.005  # step forward in time
TIME_STOP = 2000


def initial_angles():
    initial_angle_1 = {'time': - STEP, 'angle': 0}
    initial_angle_2 = {'time': 0, 'angle': 0}
    return {'first_point': initial_angle_1, 'second_point': initial_angle_2}


def initial_velocities():
    initial_velocity_1 = {'time': - STEP, 'velocity': 0}
    initial_velocity_2 = {'time': 0, 'velocity': 0}
    return {
        'first_point': initial_velocity_1,
        'second_point': initial_velocity_2
    }


def create_time_sequence():
    t = 0
    time_sequence = []
    for i in xrange(TIME_STOP):
        t += STEP
        time_sequence.append(t)
    return time_sequence


def get_next_angle(angle, velocity):
    return 2 * STEP * velocity + angle


def get_next_velocity(time, angle, velocity):
    return 2 * STEP * (
        -sin(angle) + DRIVING_AMPLITUDE * cos(DRIVING_FREQENCY * time)
    ) + velocity


def drive_the_system(time_sequence):
    angle = [
        initial_angles()['first_point']['angle'],
        initial_angles()['second_point']['angle']
    ]

    velocity = [
        initial_velocities()['first_point']['velocity'],
        initial_velocities()['second_point']['velocity']
    ]

    time = [
        initial_angles()['first_point']['time'],
        initial_angles()['second_point']['time']
    ]

    first_angle = angle[0]
    second_angle = angle[1]
    first_velocity = velocity[0]
    second_velocity = velocity[1]

    for t in time_sequence:

        next_angle = get_next_angle(first_angle, second_velocity)
        next_velocity = get_next_velocity(t, second_angle, first_velocity)

        angle.append(next_angle)
        velocity.append(next_velocity)
        time.append(t)

        first_angle = second_angle
        second_angle = next_angle
        first_velocity = second_velocity
        second_velocity = next_velocity

    system = {'time': time, 'angle': angle, 'velocity': velocity}
    return system


def main(time_sequence):
    for i in xrange(time_sequence):
        time = drive_the_system(create_time_sequence())['time']
        angle = drive_the_system(create_time_sequence())['angle']
        velocity = drive_the_system(create_time_sequence())['velocity']
        data = zip(time, angle, velocity)
        print data[i][0], data[i][1], data[i][2]


if __name__ == '__main__':
    main(TIME_STOP)
