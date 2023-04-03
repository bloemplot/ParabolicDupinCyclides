# -*- coding: utf-8 -*-

import numpy as np
import pyvista as pv

#%% Data
f = 0.1 # this determines the radius of inner circle 1
x, y, z = 2*np.mgrid[-0.5:0.5:100j, -1:1:100j, -1:1:100j]

def vol(a):
    vol_0 = (x + (f/2 - 1)*a)*(x**2+y**2+z**2 - (f**2*a**2)/4) + a*z**2 
    grid = pv.StructuredGrid(x, y, z)
    grid["vol"] = vol_0.flatten()
    contours = grid.contour([0])
    return contours

def vol_up(a,d):
    vol_0 = (-(x+d) + (f/2 - 1)*a)*((x+d)**2+y**2+z**2 - (f**2*a**2)/4) + a*y**2 
    grid = pv.StructuredGrid(x, y, z)
    grid["vol"] = vol_0.flatten()
    contours = grid.contour([0])
    return contours

# a determines the size of inner circle 2
a = 2

# Plotting our surface
pv.set_plot_theme('document')
p = pv.Plotter()
p.add_mesh(vol(a),color='w', show_scalar_bar=False)
p.add_mesh(vol_up(a,-1/2),color='cyan', show_scalar_bar=False)
p.show()
