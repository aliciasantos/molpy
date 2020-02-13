import os
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D



def distance(point1, point2):
    """
    Calculate distance between two points.

    Parameters
    ----------
    point1 : array_like
        The first point.
    point2 : array_like
        The second point.

    Returns
    -------
    float
        The distance between point1 and point2.
    """

    point1 = np.asarray(point1)
    point2 = np.asarray(point2)
    return np.linalg.norm(point1 - point2)


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
