# handypy
Quick atsonomy and atmospheric science calculators for students

In this folder find multiple independent python scripts for solving common problems with VSTAR, producing inputs to VSTAR, 
and calculating useful values.
These scripts are intended primarily for my own use and the use of my students.  Please excuse their sometimes rough nature
and the obvious progress in my learning (some of these are old, from when I was first learning python).


Codes:

calcmeanmolweight.py

This code produces a value for the mean molecular weight (an input varaiable for VSTAR when providing an external atmosphere 
(mixing ratios) file) based on an atmosphere file formatted for VSTAR.
Species included are appropriate for most terrestrial planets.  You may need to add molecular weights for other species if they 
are included in your input atmosphere.
User inputs are the path to the atmosphere file, the gravity on the planet, and the T_eff if you wish to have the scale height 
calculated also.  It is important to note that ALL species must be included in the input atmosphere, i.e. do not leave out N2 
just because it has no lines of interest.

spectrumconverterwnwl.py

This interactive code converts a spectrum in spectral irradiance (flux density per wavelength) from wavelength to wavenumber or vice versa. Thus it converts not only the x-axis but also y as the value is scaled by the x-axis value.  The code takes user "raw" (screen) input for the x- and y-axis units, the path to the spectrum to be converted, and offers options to plot
the spectrum and/or write it to a new file.

