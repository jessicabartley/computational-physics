import LT.box as B
import matplotlib.pyplot as plt


# retrieve the data
system_data = B.get_file('system.data')

# put the data into arrays
time = B.get_data(system_data,'time')
angle = B.get_data(system_data,'angle')
angular_velocity = B.get_data(system_data,'velocity')

# make and save plots
angle_plot = plt.plot(time, angle, '-', label='theta')
angular_velocity_plot = plt.plot(time, angular_velocity, '-', label='d theta / d t')

plt.title('Pendulum System: driving amplitude=0.1, freqeuncy=5')
plt.xlabel('time (seconds)')
plt.ylabel('')
plt.legend() # shows legned
plt.legend(loc=0) # shows legned, loc is location code

plt.savefig('Angle_And_Velocity_Plot.pdf')

# make second plot
plt.clf() # clears current figure
plt.cla() # clears current axis settings

phase_plot = plt.plot(angle, angular_velocity, '-')
plt.title('Theta dot vs theta: driving amplitude=0.1, freqeuncy=5')
plt.xlabel('theta')
plt.ylabel('d theta / d t')
plt.legend() # shows legned

plt.savefig('Angle_Vs_Velocity_Plot.pdf')
