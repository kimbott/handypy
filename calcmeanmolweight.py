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
#inputfile = "/Users/z3320600/vstar/applications/Earth/T1e_waterclear.atm" #full path to atm file, should not matter if it is tab or space delimited
inputfile = "/Users/z3320600/Dropbox/T1e_waterclear.atm"

### READ IN 3rd LINE OF ATM FILE (SPECIES)###
    
f=open(inputfile)
lines=f.readlines()
print lines[2]
species2 = re.split('\t|\n| ',lines[2])

species = np.atleast_1d(species2)
print species
print species[3]

### READ IN LINE 4 TO INFINITY OF ATM FILE (ABUNDANCES) ###

with open(inputfile) as textFile:
        abuns2 = [line.split() for line in textFile]
#print abuns
abuns = array(abuns2[3:])
print abuns[3,3]


### AVERAGE OF COLUMN ###


print abuns[:,3]
abuns = abuns.astype(float)
print len(abuns[1,:])-3

averages = []
#averages = np.empty(len(abuns[1,:])-3, dtype=object)
for n in range(3,len(abuns[1,:])): #n is the column you compute for
        avs = sum(abuns[:,n])/len(abuns[:,n])
        averages.append(avs)
        
print "averages", averages


### LIST OF MOL WEIGHTS OF HITRAN NUMBERS ### H2O, 02, CO, CH4, CO2, SO2, O3, N2
MW = [ 
[1,18.01528],
[7,31.9988],
[5,28.0101],
[6,16.04246],
[2,44.0095],
[9,64.0638],
[3,47.9982],
[22,28.0134]
 ]

MW = np.array(MW)
print MW[1,1]

### GIVEN THE VALUE IN species AT COLUMN n, TAKE THE AVERAGE AT n ###
### AND MATCH THE 3rd LINE VALUE TO THE HITRAN MMW LIST ###
### MULTIPLY THE AVERAGE BY THE MMW FOR EACH COLUMN ###
weights = []
for n in range(3,len(abuns[1,:])):
		print n
#		print species[n]
#		print MW[1,0]
		index = np.where(MW[:,0]==int(species[n])) #at what index (row) does the value from species' nth column match the value in the 0 column of the mean mol weights
#		print index
		MWn = MW[index,1]
#		print MWn
		print "ave", averages[n-3]
		specweight = MWn*averages[n-3] #needs to be shifted bc read in 4th line on with first 3 columns included... lost them somewhere for line 3
		print specweight
		weights.append(specweight)
#		MW[0,:].index(species[n])


### SUM THESE FOR THE ATM MMW###
print weights
atmMMW = sum(weights)
print "Mean Mol weight of this atmosphere is", atmMMW

### FIN ###
