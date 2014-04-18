#!/usr/bin/env python

from __future__ import division

from pylab import *
#from numpy import cross, dot, sin, cos, linspace, sqrt, array
from math import acos
from scipy.integrate import odeint


NUMBER_OF_STEPS = 100


def initial_conditions_in_earth_sun_plane():
    position = (0.3170787, -1.887907, 0.2396305) # in AU
    velocity = (0.008180196, 0.01188029, 0.0006081217) # in AU/day
    position_magnitude = sqrt( sum(map(lambda x: x ** 2, position)) )
    initial_system = {
        'position': position, 
        'velocity': velocity, 
        'position_magnitude': position_magnitude}
    return initial_system


def get_angular_momentum(position, velocity):
    l_vector = cross(position, velocity)
    l_magnitude = sqrt(sum(map(lambda x: x ** 2, l_vector)))
    return {'vector': l_vector, 'magnitude': l_magnitude}


def transform_to_comet_sun_plane(vector):
    x = initial_conditions_in_earth_sun_plane()['position']
    v = initial_conditions_in_earth_sun_plane()['velocity']
    l_unit_vector = get_angular_momentum(x,v)['vector'] / get_angular_momentum(x,v)['magnitude']

    """use z component of l hat to get theta, x component to get phi"""
    theta = acos( l_unit_vector[2] )
    phi = acos( l_unit_vector[0] / sin(theta) )

    rotation_matrix = array([
        [ cos(theta) * cos(phi) , cos(theta) * sin(phi) , sin(theta)],
        [ -sin(phi), cos(phi), 0],
        [ -sin(theta) * cos(phi), -sin(theta) * sin(phi) , cos(theta)]
        ])

    rotated_vector = dot( rotation_matrix, vector )
    magnitude =  sqrt(sum(map(lambda x: x ** 2, rotated_vector)))
    return {'vector': rotated_vector, 'magnitude': magnitude}


def get_velocities(position, velocity, angular_momentum):
    transformed_velocity = transform_to_comet_sun_plane(velocity)['vector']
    transformed_position = transform_to_comet_sun_plane(position)['vector']
    transformed_angular_momentum = transform_to_comet_sun_plane(angular_momentum)['vector']

    position_magnitude = initial_conditions_in_earth_sun_plane()['position_magnitude']
    phi_vector = cross(transformed_angular_momentum, transformed_position)
    phi_magnitude = sqrt(sum(map(lambda x: x ** 2, phi_vector)))

    radial_velocity = dot( transformed_position / position_magnitude , transformed_velocity )
    azimuthal_velocity = dot( phi_vector / phi_magnitude, transformed_velocity )

    return {'velocity_r': radial_velocity, 'velocity_phi': azimuthal_velocity}


# set up arguments in earth sun plane means earth sun plane
position_ES = array(initial_conditions_in_earth_sun_plane()['position'])
velocity_ES = array(initial_conditions_in_earth_sun_plane()['velocity'])
angular_momentum_ES = get_angular_momentum(position_ES, velocity_ES)['vector']

# set up initial conditions in comet sun plane
angular_momentum_magnitude = get_angular_momentum(position_ES, velocity_ES)['magnitude']
initial_radius = initial_conditions_in_earth_sun_plane()['position_magnitude']
initial_velocity_r = get_velocities(position_ES, velocity_ES, angular_momentum_ES)['velocity_r']
initial_phi = 0
initial_velocity_phi = get_velocities(position_ES, velocity_ES, angular_momentum_ES)['velocity_phi']

# set up ODE solver arguments
y = zeros(4)
y[0] = initial_radius
y[1] = initial_velocity_r
y[2] = initial_phi
y[3] = initial_velocity_phi

time = linspace(0, 10, NUMBER_OF_STEPS) # (start, stop, num of equal spaced steps)

def differential_equations(y, time):
    g0 = y[1]
    g1 = ( (- angular_momentum_magnitude ** 2) / (y[0] ** 3)) + (1 / (y[0] ** 2))
    g2 = y[3] / (y[0] ** 2)
    g3 = 0
    return array([g0, g1, g2, g3])

answer = odeint(differential_equations, y, time)

# convet to cartesian
xdata = (answer[:,0]) * cos(answer[:,2])
ydata = (answer[:,0]) * sin(answer[:,2])

plot(xdata, ydata, 'r-')
xlabel("Horizontal Position")
ylabel("Vertical Position")
show()

#    return (g0, g1, g2, g3)
#
#
#def main():
#    answer = odeint(comet, y, time)
#    for row in xrange(NUMBER_OF_STEPS):
#        print answer[row, 0], answer[row, 1], answer[row, 2], answer[row, 3]
#
#
#if __name__ == '__main__':
#    main()

