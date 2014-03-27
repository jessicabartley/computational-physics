import LT.box as B
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# retrieve the data
data_file_Ca = B.get_file('ResultsConstantsCalcium.data')
data_file_CaRMS = B.get_file('ResultsRadiusCalcium.data')

data_file_Fe = B.get_file('ResultsConstantsIron.data')
data_file_FeRMS = B.get_file('ResultsRadiusIron.data')

data_file_Cu63 = B.get_file('ResultsConstantsCopper63.data')
data_file_Cu63RMS = B.get_file('ResultsRadiusCopper63.data')

data_file_Cu65 = B.get_file('ResultsConstantsCopper65.data')
data_file_Cu65RMS = B.get_file('ResultsRadiusCopper65.data')

data_file_Au = B.get_file('ResultsConstantsGold.data')
data_file_AuRMS = B.get_file('ResultsRadiusGold.data')

data_file_Pb = B.get_file('ResultsConstantsLead.data')
data_file_PbRMS = B.get_file('ResultsRadiusLead.data')

data_file_U = B.get_file('ResultsConstantsUranium.data')
data_file_URMS = B.get_file('ResultsRadiusUranium.data')

# put the data into arrays
node = range(1,17)

Constants_Ca = B.get_data(data_file_Ca,'C')
RMS_Ca = B.get_data(data_file_CaRMS,'rms')

Constants_Fe = B.get_data(data_file_Fe,'C')
RMS_Fe = B.get_data(data_file_FeRMS,'rms')

Constants_Cu63 = B.get_data(data_file_Cu63,'C')
RMS_Cu63 = B.get_data(data_file_Cu63RMS,'rms')

Constants_Cu65 = B.get_data(data_file_Cu65,'C')
RMS_Cu65 = B.get_data(data_file_Cu65RMS,'rms')

Constants_Au = B.get_data(data_file_Au,'C')
RMS_Au = B.get_data(data_file_AuRMS,'rms')

Constants_Pb = B.get_data(data_file_Pb,'C')
RMS_Pb = B.get_data(data_file_PbRMS,'rms')

Constants_U = B.get_data(data_file_U,'C')
RMS_U = B.get_data(data_file_URMS,'rms')

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

plt.clf() # clears current figure
plt.cla() # clears current axis settings
Ca_plot = plt.plot(node,RMS_Ca, '-.o', label='Calcium')
Fe_plot = plt.plot(node,RMS_Fe, '-.o', label='Iron')
Cu63_plot = plt.plot(node,RMS_Cu63, '-.o', label='Copper63')
Cu65_plot = plt.plot(node,RMS_Cu65, '-.o', label='Copper65')
Au_plot = plt.plot(node,RMS_Au, '-.o', label='Gold')
Pb_plot = plt.plot(node,RMS_Pb, '-.o', label='Lead')
U_plot = plt.plot(node,RMS_U, '-.o', label='Uranium')
plt.title('RMS Radius vs Node Number')
plt.legend(loc=4) # shows legned, loc is location code
plt.savefig('PlotRadii.pdf')



