import numpy as np
import astropy.units as u
from astropy.table import Table
from ReadFile import Read

# Create a function that outputs the total mass of each particle of a desired particle type (1=DarkMatter,2=DiskStars,3=BulgeStars)

def ComponentMass(filename,ptype):
    # Inputs:
    #    filename is the name of the text file
    #    ptype is the number that represents the particle type (1=DarkMatter,2=DiskStars,3=BulgeStars)
    # Return:
    #    mtot is the total mass of the galaxy component dictated my ptype (Msun*10e12)

    # Function from "ReadFile.py" used to store time, number of particles and data from the file.
    # Only data is needed, which stores the desired values (type, mass, distance and velocity in x,y,z) for each particle
    time,particlenumber,data = Read(filename)

    # Filter out all other types
    index = np.where(data['type'] == ptype)

    # Create a new list of values for the filtered type
    # Store new values of mass (10e10 Msun)
    mnew = data['m'][index]

    # Sum all elemants of mass and store
    mtot = np.around(np.sum(mnew)/100, 3)

    return mtot


# Store Names
name = ['MW','M31','M33','Local Group']

# Store total component masses of MW
MWhalo =     ComponentMass('MW_000.txt',1)
MWdisk =     ComponentMass('MW_000.txt',2)
MWbulge =    ComponentMass('MW_000.txt',3)
MWtot =      np.around(MWhalo + MWdisk + MWbulge,3)
MWstellar =  MWdisk + MWbulge
MWfbar =     np.around(MWstellar/MWtot,3)

# Store total component masses of M31
M31halo =    ComponentMass('M31_000.txt',1)
M31disk =    ComponentMass('M31_000.txt',2)
M31bulge =   ComponentMass('M31_000.txt',3)
M31tot =     np.around(M31halo + M31disk + M31bulge,3)
M31stellar = M31disk + M31bulge
M31fbar =    np.around(M31stellar/M31tot,3)

# Store total component masses of M33 (no bulge)
M33halo =    ComponentMass('M33_000.txt',1)
M33disk =    ComponentMass('M33_000.txt',2)
M33bulge =   0
M33tot =     np.around(M33halo + M33disk,3)
M33stellar = M33disk + M33bulge
M33fbar =    np.around(M33stellar/M33tot,3)

# Store total mass components of the Local Group
localtot =   np.around(MWtot + M31tot + M33tot,3)
totstellar = MWstellar + M31stellar + M33stellar
localfbar =  np.around(totstellar/localtot,3)

# Store halo, disk, and bulge masses seperately in order. Used for Table
halo =       np.array([MWhalo, M31halo, M33halo, 0])
disk =       np.array([MWdisk, M31disk, M33disk, 0])
bulge =      np.array([MWbulge,M31bulge,M33bulge,0])
tot =        np.array([MWtot,  M31tot,  M33tot,  localtot])
fbar =       np.array([MWfbar, M31fbar, M33fbar, localfbar])

# Make a table with name, halo, disk, bulge elements
t = Table([name,halo,disk,bulge,tot,fbar], names=('Galaxy Name','Halo Mass (10^12 Msun)','Disk Mass (10^12 Msun)','Bulge Mass (10^12 Msun)','Total Mass (10^12 Msun)','Baryon Fraction'))

# Show table
print(t)


# -----------------Questions----------------------------

# 1)How does the total mass of the MW and M31 compare in this simulation? What galaxy component dominates this total mass?
MassRatio = np.around(MWtot/M31tot,3)
print("Questions:")
print("\n1)")
print("Mass ratio of MW vs M31: ", MassRatio)
print("The dark matter dominates the total mass.")

# 2)How does the stellar mass of the MW and M31 compare in this simulation?
StellarRatio = np.around(MWstellar/M31stellar,3)
print("\n2)")
print("Stellar mass ratio of MW vs M31: ",StellarRatio)
print("MW should be more luminous.")

# 3)How does the total dark matter mass of the MW and M31 compare in this simulation? Is it surprising, given their difference in stellar mass?
DarkRatio = np.around(MWhalo/M31halo,3)
print("\n3)")
print("Dark matter mass ratio of MW vs M31: ",DarkRatio)
print("This is surprising given their difference in stellar mass. \nM31 has much more stellar mass than MW yet has similar dark matter masses.")

# 4)What is the ratio of stellar mass to total mass for each galaxy? In the Universe, 16% of all mass is locked up in baryons vs darkmatter.
# How does this ratio compare to the baryon fraction you computed for each galaxy? Given that the total mass in the disks of these galaxies
# is negligible compared to the stellar mass, any ideas why the universal baryon fraction might differ from that in these galaxies?
print("\n4)")
print("Baryon fractions:")
print("MW  ",MWfbar)
print("M31 ",M31fbar)
print("M33 ",M33fbar)
print("These are all much smaller that the Universe's 16%")
print("There is a LOT more dark matter than baryon matter in the Universe.")
