import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib as mpl
import numpy as np
import math

def robin_temperature(b_dot, thk, H_flux, T_S):	
    """Robin 1955 analytical solution for the heat equation
    Parameters
    ----------
    b_dot : surface vertical velocity
        assumed to be the same as SMB [m/yr]
    thk : ice thickness [m]
    H_flux : geothermal heat flux [W/m2]
    T_S : surface Dirichlet temperature [C]
    nz : no. of points on a vertical axis

    Returns
    -------
    temp : temp. profile at depth
    depth : depth array 
    """

    # define constants
    diffusivity = 34.4   # m2/yr
    conductivity = 2.10  # W/m/K
    nz = 30 

    # linear depth profile
    depth = np.linspace(0, thk, nz)

    # Array to fill with data
    nsteps = len(depth)    
    temp = np.zeros(nsteps)

    # calculate Q term 
    q_sqrd = abs(b_dot/2./thk/diffusivity)    
    q_term = math.sqrt(q_sqrd)

    # calculate temperature
    for i in range(len(depth)):
        temp[i] = T_S - H_flux*math.sqrt(math.pi)/(2. * conductivity * q_term) * \
                (math.erf(depth[i] * q_term) - math.erf(thk * q_term))
    return temp, depth






















