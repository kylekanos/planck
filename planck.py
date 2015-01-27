import matplotlib.pyplot as plt
import numpy as np
import math

# all values SI
h=6.62606957e-34
c=2.9979e8
kB=1.3806488e-23
coef=2.0*h/(c*c)

# actual planck function here
def Planck(nu,T):
    x=h*nu/(kB*T)
    y=nu**3
    ex = math.exp(x)-1.0
    return coef*y/ex
    
# number of cells in computing Bnu & nu
ncell = 1000

# arrays of size ncell
Bnu=np.zeros(ncell)
nu = np.zeros(ncell)

# run frequency bins from 800 Hz to 2x10**15 Hz
nu_lo = 8.0e2
nu_hi = 2.0e15
dnu = (nu_hi - nu_lo)/(ncell-1)

nu[0] = nu_lo
for i in range(1,ncell):
    nu[i] = nu[i-1] + dnu
    
# main looop, use T=4000 K here)
for i in range(0,ncell):
    Bnu[i] = Planck(nu[i],3000.0)
    
# plot it all
plt.plot(nu,Bnu)
plt.show()
