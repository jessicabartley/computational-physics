# script to try out histogramming
import LT.box as B

# get the file
mcf = B.get_file('counts.data')

# see what is in there
mcf.show_keys()

# get some data
ne = B.get_data(mcf, 'n')
counts = B.get_data(mcf, 'counts')

# make a hisrogram of the values
hh = B.histo(counts, range = (120., 180.), bins = 60)

# set the initial values for fitting
hh.A.set(2)
hh.mean.set(140)
hh.sigma.set(10)

# fit the peak
hh.fit()

# plot the histogram
hh.plot()
B.pl.show()

# plot the fit
hh.plot_fit()
B.pl.show()


