#For VSTAR: "The input file should be a list of wavenumbers(cm-1) and fluxes in Wm-2/cm-1 
#(e.g. the solar file Kuruczcm-1_susim_atlas2.dat) at 1 AU distance"

#forematter
import numpy as np
import pylab
import matplotlib.pyplot as plt 

################### USER INPUTS ######################
# user input what is the x axis in (wl nm, um, wn? choose 1, 2 3) what is the y axis second column in
# note: if from Castelli Kurucz prob in wn, if from VPL prob in um

wltype = raw_input("""What is the x-axis (1st column, wavelength) in?  
nm - 1
um - 2
wn (cm-1) - 3
""")

print "You chose option ", wltype

fluxtype = raw_input("""What is the y-axis (2nd column, irradiance) in?  
W/m^2/nm - 1
W/m^2/um - 2
Wm-2/cm-1 (W/m2*cm) - 3
Something else - 4
""")

print "You chose option ", fluxtype, "; those should have been the same number..."
if fluxtype=='4':
	print "Not one of those 3?  Bummer... can't help you with that."
	exit()

# user input what would you like to convert it to default is cm-1 and Wm-2/cm-1 ???

print "nm and um are converted to wn, wn is converted to um"


################### READ IN FILE AS ARRAY ######################
filepath = raw_input("Filename? (give full path if not in same directory): ")

# !! I am keeping copies of these options here for reference ! #

#option 1 doesn't split the columns
#with open(filepath) as textFile:
#        spec = [line.split() for line in textFile]

#print spec[1]

#option 2 doesn't split the columns
#f = open(filepath, 'r')
#spec = f.read().splitlines()
#f.close()

#option 3 doesn't split the columns but is fastest
#spec = map(str.split("\t"), open(filepath))

#option 4 jfc finally
spec = np.genfromtxt(filepath) # if you're seeing an error for too many columns you may have comments you need to delete in your file

specarr = np.asarray(spec)
#print specarr.shape
#print specarr[1,1]



################### OPTIONS ######################


################### from nm to wn AND W/m2/nm to Wm-2/cm-1  #####################

if wltype=='1' and fluxtype=='1':
	newspec1 = 10000000/specarr[:,0]
	xax = "Wavenumber (cm^-1)"
	yax = "Spectral Irradiance (Wm^-2/cm^-1)"
	
################### from um to wn AND W/m2/um to Wm-2/cm-1  #####################

elif wltype=='2' and fluxtype=='2':
	newspec1 = 10000/specarr[:,0]
	xax = "Wavenumber (cm^-1)"
	yax = "Spectral Irradiance (Wm^-2/cm^-1)"
	
################### from wn to um AND Wm-2/cm-1 to W/m2/um (reverse of above)  #####################

elif wltype=='3' and fluxtype=='3':
	newspec1 = 10000/specarr[:,0] # conversion is the same for the wl column in either direction. seperated for declarations of variables
	xax = "Wavelength (microns, um)"
	yax = "Spectral Irradiance (Wm^-2um^-1)"
	
###################
else: 
	print "Either your wavelength and flux types don't match or perhaps you mistyped earlier."
	
			
#print newspec1
#print newspec1.shape

# multiply each value in $2 by the value in $1 in specarr
newspec2a = specarr[:,1]*specarr[:,0]
#print newspec2a
#print newspec2a.shape

#divide each value in newspec2a by the corresponding value is newspec1

newspec2b = newspec2a/newspec1
#print newspec2b
#print newspec2b.shape

#"concatenate" (stack) to a 2D array
#newspec1 = np.asarray(newspec1)
#newspec2b = np.asarray(newspec2b)

newspec = np.column_stack((newspec1,newspec2b))
print "New spectrum looks like this: \n", newspec
#print newspec.shape


################### PLOT ######################
makeplotq = raw_input("Do you want to plot the new spectrum? (Y/N)")
if makeplotq in ["y","Y","yes","Yes","Yass"]:
#if makeplotq=="Y" or "yes" or "Yes" or "Yass" or "y":
	pylab.figure(0,figsize=(20,10))
	plots2 = pylab.plot(newspec[:,0], newspec[:,1], color='#df6747', linewidth='3')
	pylab.xlabel(xax); pylab.ylabel(yax)
	plt.suptitle('Converted stellar spectrum', fontsize=20)
	pylab.show()
elif makeplotq in["N","no","No","Nah","n"]:
	print "No worries."
else:
	print "Excuse me?"

################### OUTPUT TO FILE ######################

makefileq = raw_input("Do you want to write the new spectrum to a file? (Y/N)")
if makefileq in ["y","Y","yes","Yes","Yass"]:
	ofilename = raw_input("What should the new file be named (with extension)? e.g. sunspectrumcm-1.dat :")
	print "This will take a minute or two..."
	with open(ofilename, 'w') as outfile:
		for item in newspec:
			str_item = str(item)[1:-1]
			outfile.write("%s\n" % str_item)
elif makefileq in["N","no","No","Nah","n"]:
	print "No worries. Bye forever."
	exit()
else:
	exit()

# /Users/z3320600/vstar/applications/Earth/trappist1Lincowskicm-1.dat
# /Users/z3320600/vstar/applications/Earth/Kurucz1cm-1_susim_atlas2.dat