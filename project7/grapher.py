import LT.box as B
import matplotlib.pyplot as plt
from numpy import sin, cos


# retrieve the data
system_data = B.get_file('comet.data')

# put the data into arrays
radius = B.get_data(system_data,'radius')
velocity_r = B.get_data(system_data,'velocity_r')
phi = B.get_data(system_data,'phi')
velocity_phi = B.get_data(system_data,'velocity_phi')

# make and save plots
orbit_plot = plt.plot(radius, phi, '-', label='theta')

plt.title('Comet Orbit in the Polar Plane')
#plt.xlabel('time (seconds)')
#plt.ylabel('')
#plt.legend() # shows legned
#plt.legend(loc=0) # shows legned, loc is location code

plt.savefig('Orbit.pdf')
