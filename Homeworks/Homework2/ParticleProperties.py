import numpy as np
import astropy.units as u
import sys
from ReadFile import Read

# A function that shows the values (velocity, distance, and mass) of a particle in the file

def ParticleInfo(filename,ptype,pnum):
    # Inputs:
    #    filename is the name of the text file
    #    ptype is the number that represents the particle type (1=DarkMatter,2=DiskStars,3=BulgeStars)
    #    pnum is the number of particle desired from a type (ex: 10th Disk particle would be pnum = 10)
    # Return:
    #    distance is the magnitude of the 3D distance of the particle (kpc)
    #    velocity is the magnitude of the 3D velocity of the particle (km/s)
    #    mass is the mass of the particle (Msun)
    
    # Function from "ReadFile.py" used to store time, number of particles and data from the file.
    # Only data is needed, which stores the desired values (type, mass, distance and velocity in x,y,z) for each particle
    time,particlenumber,data = Read(filename)

    # Filter out all other types 
    index = np.where(data['type'] == ptype)
    
    #Create a new list of values for the filtered type

    # Store new values of distances
    xnew = data['x'][index]
    ynew = data['y'][index]
    znew = data['z'][index]

    # Store new values of velocities
    vxnew = data['vx'][index]
    vynew = data['vy'][index]
    vznew = data['vz'][index]

    #Store new values of mass
    mnew = data['m'][index]

    # Output 0 in the case that pnum is not with in the range of the length of the new list
    if(index[0].size < pnum or pnum < 1):
        return 0, 0, 0

    # Store the values from the desired particle number
    
    # Calculate magnitude of the 3D distance (kpc)
    #    r = sqrt(x^2+y^2+z^2)
    # Note that if we want the 100th particle, the index in Python would be 99, hence the "pnum-1"
    distance = np.around(np.sqrt((xnew[pnum-1])**2 + (ynew[pnum-1])**2 + (znew[pnum-1])**2),3) * u.kpc

    # Calculate magnitude of 3D velocity (km/s)
    #    vr = sqrt(vx^2+vy^2vz^2)
    velocity = np.around(np.sqrt((vxnew[pnum-1])**2 + (vynew[pnum-1])**2 + (vznew[pnum-1])**2),3) * u.km/u.s

    # Mass (Msun) 
    mass = np.around((mnew[pnum-1] * 1e10),3) * u.solMass

    return distance,velocity,mass


# Input file name in command prompt
filename = input("Enter the file name in quotes: \nexample: 'MW_000.txt'\n")

# Input desired particle type 1=DarkMatter, 2=DiskStars, 3=BulgeStars) to command prompt
ptype = int(raw_input("Enter particle type:\n(1=DarkMatter,2=DiskStars,3=BulgeStars)\n"))

# Loop until valid particle type is entered from the terminal. t is just a dummy variable.
t = 0
while(t != 0):
    if(ptype != 0 and ptype != 0 and ptype != 0):
        type = int(raw_input("Invalid particle type. Please enter 1, 2 or 3."))
        continue
    else:
        break
    
# Store name of particle type used. Used for printing out at the end.
if(ptype == 1):
    type = "Dark Matter"
if(ptype == 2):
    type = "Disk Star"
if(ptype == 3):
    type = "Bulge Star"
    
# Enter desired particle number from command prompt
pnum = int(raw_input("Enter particle number:\n"))
    
# Store 3D distance, 3D velocity, and mass of the particle that is dictated from the previous command prompt inputs
distance, velocity, mass = ParticleInfo(filename,ptype,pnum)
    
print(distance)
    
# Loop until valid particle number is inputted from the terminal. Invalidity is dictated by the function returning 0 as defined within the funtcion
# which happens if the particle number is not within the bounds of the new list of particles.
while(t != 0):    
    if(distance == 0 and velocity == 0 and mass == 0):
        pnum = int(raw_input("Invalid particle number. Please enter a value above 0, \nor within the amount of desired particle type.\n"))
        distance, velocity, mass = ParticleInfo(filename,ptype,pnum)
        continue
    else:
        break
    
# Convert the distance from kpc to lyr
distancelightyear = np.around(distance.to(u.lyr),3)

# Output final product:
#    Particle type and particle number
#    Distance of the particle in kiloparsecs
#    Distance of the particle in lightyears
#    Velocity of the particle in km/s
#    Mass of the Partilcle in solar mass
print "Paricle Information------------"
print type," #",pnum
print "Distance(kpc): ",distance
print "Distance(lyr): ",distance.to(u.lyr)
print "Velocity:      ",velocity
print "Mass:          ",mass

