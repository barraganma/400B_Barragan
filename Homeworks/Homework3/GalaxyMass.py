import numpy as np
import astropy.units as u
from ReadFile import Read

def ComponentMass(filename,ptype):
    time,npart,data = Read(filename)
