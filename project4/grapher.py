import LT.box as B


# get file
data_file = B.get_file('data/estimatevolume.data')

# get data
no_dimension = B.get_data(data_file, 'dimension')
pi_estimate = B.get_data(data_file, 'volestimate')
error = B.get_data(data_file, 'error')

# make a plot
B.plot_exp(no_dimension, pi_estimate, error)

# add the labels
B.pl.xlabel('Number of dimensions')
B.pl.ylabel('Estimator for Volume of N Sphere')
B.pl.title('Volume of N Sphere Estimated')

# save the plot
B.pl.savefig('vol_plot.png')