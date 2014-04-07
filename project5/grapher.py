import LT.box as B
import matplotlib.pyplot as plt


# retrieve the data
energy_data = B.get_file('data/energy.data')

# put the data into arrays
sweep = B.get_data(energy_data,'sweep')
total_energy = B.get_data(energy_data,'total_energy')
kinetic_energy = B.get_data(energy_data,'kinetic_energy')
potential_energy = B.get_data(energy_data,'potential_energy')

# make and save plots
total_energy_plot = plt.plot(sweep,total_energy, '-', label='Total Energy')
kinetic_energy_plot = plt.plot(sweep,kinetic_energy, '-', label='Kinetic Energy')
potential_energy_plot = plt.plot(sweep,potential_energy, '-', label='Potential Energy')

plt.title('Equilibrium Energy for Noninteracting Gas, N=100')
plt.xlabel('Number of Sweeps in Markov Chain')
plt.ylabel('Energy')
plt.legend() # shows legned
plt.legend(loc=4) # shows legned, loc is location code

plt.savefig('PlotEnergy.pdf')
