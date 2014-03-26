import LT.box as B
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# get the data to plot
data_file_Ca = B.get_file('ResultsConstantsCalcium.data')
data_file_Fe = B.get_file('ResultsConstantsIron.data')
data_file_Cu63 = B.get_file('ResultsConstantsCopper63.data')
data_file_Cu65 = B.get_file('ResultsConstantsCopper65.data')
data_file_Au = B.get_file('ResultsConstantsGold.data')
data_file_Pb = B.get_file('ResultsConstantsLead.data')
data_file_U = B.get_file('ResultsConstantsUranium.data')

# get the data into arrays
node = range(1,17)
Constants_Ca = B.get_data(data_file_Ca,'C')
Constants_Fe = B.get_data(data_file_Fe,'C')
Constants_Cu63 = B.get_data(data_file_Cu63,'C')
Constants_Cu65 = B.get_data(data_file_Cu65,'C')
Constants_Au = B.get_data(data_file_Au,'C')
Constants_Pb = B.get_data(data_file_Pb,'C')
Constants_U = B.get_data(data_file_U,'C')



# make and save plots

Ca_plot = plt.plot(node,Constants_Ca, '-.o', label='Calcium')
Fe_plot = plt.plot(node,Constants_Fe, '-.o', label='Iron')
Cu63_plot = plt.plot(node,Constants_Cu63, '-.o', label='Copper63')
Cu65_plot = plt.plot(node,Constants_Cu65, '-.o', label='Copper65')
Au_plot = plt.plot(node,Constants_Au, '-.o', label='Gold')
Pb_plot = plt.plot(node,Constants_Pb, '-.o', label='Lead')
U_plot = plt.plot(node,Constants_U, '-.o', label='Uranium')

plt.title('Normalization Constant vs Node Number')
plt.legend() # shows legned
plt.axis([0,16,-1,18]) # plt.axis([xmin,xmax,ymin,ymax])
plt.savefig('PlotConstants.pdf')
