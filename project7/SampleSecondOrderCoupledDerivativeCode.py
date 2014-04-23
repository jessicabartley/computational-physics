# http://bulldog2.redlands.edu/facultyfolder/deweerd/tutorials/Tutorial-ODEs.pdf

from scipy.integrate import odeint
from pylab import * # for plotting commands 
 
def deriv(z,t): # return derivatives of the array z 
 a = -2.0 
 b = -0.1 
 c = 1.0
 return array([ z[1], a*z[2], z[3], b+c*z[1] ]) 
 
time = linspace(0.0,10.0,1000) 
zinit = array([0.0005,0.2,0.03,0.04]) # initial values 
z = odeint(deriv,zinit,time) 

import pdb
pdb.set_trace()
 
figure() 
plot(time,z[:,0]) # z[:,0] is the first column of z 
xlabel('t') 
ylabel('z') 
show() 