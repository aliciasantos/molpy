import os
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

%matplotlib notebook


def read_xyz(filename):
    with open(filename, "r") as handle:
        data = handle.readlines()
    data=data[2:]
    data=[x.split() for x in data]
    symbols=[x[0] for x in data]
#    xyz=np.array([[float(y) for y in x[1:]] for x in data])

    xyz=[]
    for line in data:
        xyz.append([float(line[1]), float(line[2]), float(line[3])])

    print(xyz)
    print('\n')

    return {'symbols': np.array(symbols), 'geometry':xyz}


#def open_xyz(file_location):


    # Open an xyz file and return symbols and coordinates.
#    xyz_file = np.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
#    symbols = xyz_file[:,0]
#    coords = (xyz_file[:,1:])
#    coords = coords.astype(np.float)
#    return symbols, coords
