# import  the toolbox and call it B
import LT.box as B
import numpy as np

# read the data
mf = B.get_file('my_exp_1.data')

# get the data into arrays
t = B.get_data(mf, 'time')
dexp = B.get_data(mf,'dist')
derr = B.get_data(mf, 'd_err')

# print the values in a for loop
for i, D in enumerate(dexp):
    # indentation is important
    print 'time = ', t[i], 'distance = ', D, 'error = ', derr[i]
# end of the loop = end of indentation
# plot the data
B.plot_exp(t, dexp, derr)

# fit a line
fit = B.linefit(t, dexp, derr)

# draw the fit result
B.plot_line(fit.xpl, fit.ypl)

# add the labels
B.pl.xlabel('t (sec)')
B.pl.ylabel('Distance (m)')
B.pl.title('Distance vs time exp.')

# save the plot
B.pl.savefig('my_plot.pdf')

# print the covariance matrix:
print "The Convariance Matrix is : ", fit.cov
