import numpy as np
import astropy.units as u

# A function that outputs useful values from a simulation data file

def Read(filename):
    # Inputs:
    # filename is the name of the text file that is to be read
    # Return:
    # time is the instance of the simulation that the file represents
    # particles is the total number of particles the file has values for
    # data is a 2D array that has an array of values (type, mass, distance and velocity in x,y,z) for each particle

    # Open the file
    file = open(filename,'r')

    # Read the first line of the file and store the time (Myr)
    line1 = file.readline()
    label, value = line1.split()
    time = float(value)*u.Myr

    # Read the second line of te file and store the total number of particles
    line2 = file.readline()
    label, value = line2.split()
    particles = int(value)

    # Close the file
    file.close()

    # Store remaining values of the file
    data = np.genfromtxt(filename,dtype=None,names=True,skip_header=3)

    return time,particles,data
