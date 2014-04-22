#!/usr/bin/env python

from __future__ import division

from math import acos
from numpy import array, cos, cross, dot, linspace, sin
from numpy.linalg import norm
from pylab import plot, show, xlabel, ylabel
from scipy.integrate import odeint


NUMBER_OF_STEPS = 2000


def initialize_earth_sun_plane():
    position = array((0.3170787, -1.887907, 0.2396305))  # in AU
    velocity = array((0.008180196, 0.01188029, 0.0006081217))  # in AU/day
    initial_system = {
        'position': position,
        'velocity': velocity,
        'position_magnitude': norm(position)
    }
    return initial_system


def get_angular_momentum(position, velocity):
    l_vector = cross(position, velocity)
    return {'vector': l_vector, 'magnitude': norm(l_vector)}


def transform_to_comet_sun_plane(vector):
    x = initialize_earth_sun_plane()['position']
    v = initialize_earth_sun_plane()['velocity']
    angular_momentum = get_angular_momentum(x, v)
    l_unit_vector = angular_momentum['vector'] / angular_momentum['magnitude']

    # use z component of l hat to get theta, x component to get phi
    theta = acos(l_unit_vector[2])
    phi = acos(l_unit_vector[0] / sin(theta))

    rotation_matrix = array([
        [cos(theta) * cos(phi), cos(theta) * sin(phi), sin(theta)],
        [-sin(phi), cos(phi), 0],
        [-sin(theta) * cos(phi), -sin(theta) * sin(phi), cos(theta)]
    ])

    rotated_vector = dot(rotation_matrix, vector)
    return {'vector': rotated_vector, 'magnitude': norm(rotated_vector)}


def get_velocities(position, velocity, angular_momentum):
    transformed_velocity = transform_to_comet_sun_plane(velocity)['vector']
    transformed_position = transform_to_comet_sun_plane(position)['vector']
    transformed_angular_momentum = transform_to_comet_sun_plane(
        angular_momentum
    )['vector']

    position_magnitude = initialize_earth_sun_plane()['position_magnitude']
    phi_vector = cross(transformed_angular_momentum, transformed_position)
    phi_magnitude = norm(phi_vector)

    radial_velocity = dot(
        transformed_position / position_magnitude, transformed_velocity
    )
    azimuthal_velocity = dot(phi_vector / phi_magnitude, transformed_velocity)

    return {'velocity_r': radial_velocity, 'velocity_phi': azimuthal_velocity}


def differential_equations(y, time, angular_momentum_magnitude):
    g0 = y[1]
    g1 = -((angular_momentum_magnitude ** 2) / (y[0] ** 3)) + \
        (1 / (y[0] ** 2))
    g2 = y[3] / (y[0] ** 2)
    g3 = 0
    return array([g0, g1, g2, g3])


def main():
    # set up inital conditions in earth sun plane
    initial_earth_sun_plane = initialize_earth_sun_plane()
    es_position = initial_earth_sun_plane['position']
    es_velocity = initial_earth_sun_plane['velocity']
    es_angular_momentum = get_angular_momentum(es_position, es_velocity)

    # set up initial conditions in comet sun plane
    initial_radius = initial_earth_sun_plane['position_magnitude']
    initial_velocity = get_velocities(
        es_position, es_velocity, es_angular_momentum['vector']
    )
    initial_velocity_r = initial_velocity['velocity_r']
    initial_phi = 0
    initial_velocity_phi = initial_velocity['velocity_phi']

    # set up ODE solver arguments
    y = array(
        [initial_radius, initial_velocity_r, initial_phi, initial_velocity_phi]
    )

    time = linspace(0, 10, NUMBER_OF_STEPS)
    answer = odeint(
        differential_equations, y, time,
        args=(es_angular_momentum['magnitude'],)
    )

    # convert to cartesian
    xdata = (answer[:, 0]) * cos(answer[:, 2])
    ydata = (answer[:, 0]) * sin(answer[:, 2])

    plot(xdata, ydata, 'r-')
    xlabel("radius")
    ylabel("angle")
    show()


if __name__ == '__main__':
    main()
