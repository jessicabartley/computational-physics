import LT.box as B
#import numpy as np
#import matplotlib as mpl
#import mathplotlib.pyplot as plt


# get file
data_file = B.get_file('estimatepi.data')

# get data
no_dimension = B.get_data(data_file, 'dimension')
pi_estimate = B.get_data(data_file, 'piestimate')
error = B.get_data(data_file, 'error')

# make a plot
B.plot_exp(no_dimension, pi_estimate, error)

# add the labels
B.pl.xlabel('Number of dimensions')
B.pl.ylabel('Estimator for pi')
B.pl.title('Pi estimated')

# save the plot
B.pl.savefig('pi_plot.png')