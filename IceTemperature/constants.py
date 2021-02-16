#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## some constants for glacier ice
kelvin         = 273.15      # K
lapse_rate     = 7.1/1000.   # degrees per meter
conductivity   = 2.10        # W/m/K
diffusivity    = 34.4        # m2/yr
surface_temp   = -20.        # K
rho            = 910.        # kg/m3
gravity        = 9.81        # m/s2
#rate_factor    = 1e-7        # kPa-3 yr-1
rate_factor    = 5e-8        # kPa-3 yr-1 corresponding to -10 C
beta           = 7.42e-8     # K/Pa
eps            = 1e-10       # --
heat_capacity  = 2097.       # J/kg/K
latent_fusion  = 335.        # kJ/kg
y2s            = 365*24*3600.
n_glen         = 3.          # exponent of Glen's flow law
M_dot          = 0.3         # m/yr
Length         = 750e3       # m
numElems       = 750
GHF            = 0.05        # W/m2
GAMMA          = 1.397       # constant exponent of the (z/H)**GAMMA as the best SIA fit
GAMMA_OPTIMAL  = 1.532       # constant exponent of the (z/H)**GAMMA as the optimal value for temperature
COEFF_FIT      = 1.          # FIXME: this is not necessary - can be removed in the future

