### FOREMATTER ###
# This code takes an atmosphere file and calculates the mean molecular weight for the atmosphere
# Currently this will only work for earth-like planets but for a different atmosphere just add the relevant species to the MMW list
# The atm file input should include ALL species incl bulk (like N2, aka HITRAN 22)
# This is for the atm style for VSTAR, for SMART's version just change the first two reads to take line 2 and then 3-infinity

import numpy as np #for mathematical functions and arrays
import pylab
from numpy import array
import itertools
import re

### USER INPUTS ###
#inputfile = "/Users/path/T1e_waterclear.atm" #full path to atm file, should not matter if it is tab or space delimited
inputfile = "/Users/YOURPATH/IG_waterclear_superE.atm"

### READ IN 3rd LINE OF ATM FILE (SPECIES)###
    
f=open(inputfile)
lines=f.readlines()
print lines[2]
species2 = re.split('\t|\n|\r| ',lines[2])

species = np.atleast_1d(species2)
species = [i for i in species if i] 
print species #it's fine if some spaces are read in
print species[3] #is this the 4th listed species?

### READ IN LINE 4 TO INFINITY OF ATM FILE (ABUNDANCES) ###

with open(inputfile) as textFile:
        abuns2 = [line.split() for line in textFile]
#print abuns
abuns = array(abuns2[3:])
print abuns[3,3] #should match the 4th value in the next print statement


### AVERAGE OF COLUMN ###


print abuns[:,3] #so this should be column 4 (the first species)
abuns = abuns.astype(float)
print 'Calculating for', len(abuns[1,:])-3 , 'species'

averages = []
#averages = np.empty(len(abuns[1,:])-3, dtype=object)
for n in range(3,len(abuns[1,:])): #n is the column you compute for
        avs = sum(abuns[:,n])/len(abuns[:,n])
        averages.append(avs)
        
print "averages", averages #you could check this in excel if worried


### LIST OF MOL WEIGHTS OF HITRAN NUMBERS ### H2O, CO2, O3, CO, CH4, O2, SO2, N2
# Frequently we will need to add species to this array.  To do so match HITRAN numbers here https://hitran.org/docs/molec-meta/
# and then calculate (for unionized, primary isotopes) the # of X atoms * their mass + # of Y atoms * their mass =
# For example for water 2 * 1.00794u + 1 * 15.999 u = 18.01488 (atomic masses are typically weighted for isotopic abundances on Earth; it's probably fine to use this in most cases since we don't have very exact mixing ratios anyway)
MW = [ 
[1,18.01488],
[2,44.0095],
[3,47.9982],
[5,28.0101],
[6,16.04246],
[7,31.9988],
[9,64.0638],
[22,28.0134],
[102,4.0026]
 ]

MW = np.array(MW)
print MW[1,1] #should print the weight of the second species (prob = 44.0095 for co2)

### GIVEN THE VALUE IN species AT COLUMN n, TAKE THE AVERAGE AT n ###
### AND MATCH THE 3rd LINE VALUE TO THE HITRAN MMW LIST ###
### MULTIPLY THE AVERAGE BY THE MMW FOR EACH COLUMN ###
weights = []
for n in range(3,len(abuns[1,:])):
		print len(abuns[1,:]) #this should be 3+ number of species in your model
		print "for species in column", n+1
		print species[n-3]
#		print MW[1,0]
		index = np.where(MW[:,0]==int(species[n-3])) #at what index (row) in the molecular mass array does the value from species at the nth column match the value in the 0 column of the mean mol weights array
#		print index
		MWn = MW[index,1]
#		print MWn
		print "...the average is", averages[n-3]
		specweight = MWn*averages[n-3] #needs to be shifted bc read in 4th line on with first 3 columns included... lost them somewhere for line 3
		print "and the species' MMW is", specweight
		weights.append(specweight)
#		MW[0,:].index(species[n])


### SUM THESE FOR THE ATM MMW###
print weights
atmMMW = sum(weights)
print "Mean Mol weight of this atmosphere is", atmMMW

### FIN ###
